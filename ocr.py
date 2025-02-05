import cv2
from math import *
import numpy as np
from detect.ctpn_predict import *
from recognize.crnn_recognizer import PytorchOcr

def dis(image):
    cv2.imshow('image', image)
    cv2.waitKey(0)

def sort_box(box):
        """
        Detect Text Box
        """
        box = sorted(box, key=lambda x: sum([x[1], x[3], x[5], x[7]]))
        return box

def dumpRotateImage(img, degree, pt1, pt2, pt3, pt4):
        height, width = img.shape[:2]
        heightNew = int(width * fabs(sin(radians(degree))) + height * fabs(cos(radians(degree))))
        widthNew = int(height * fabs(sin(radians(degree))) + width * fabs(cos(radians(degree))))
        matRotation = cv2.getRotationMatrix2D((width // 2, height // 2), degree, 1)
        matRotation[0, 2] += (widthNew - width) // 2
        matRotation[1, 2] += (heightNew - height) // 2
        imgRotation = cv2.warpAffine(img, matRotation, (widthNew, heightNew), borderValue=(255, 255, 255))
        pt1 = list(pt1)
        pt3 = list(pt3)

        [[pt1[0]], [pt1[1]]] = np.dot(matRotation, np.array([[pt1[0]], [pt1[1]], [1]]))
        [[pt3[0]], [pt3[1]]] = np.dot(matRotation, np.array([[pt3[0]], [pt3[1]], [1]]))
        ydim, xdim = imgRotation.shape[:2]
        imgOut = imgRotation[max(1, int(pt1[1])): min(ydim - 1, int(pt3[1])),
                max(1, int(pt1[0])): min(xdim - 1, int(pt3[0]))]

        return imgOut
class FinalOCR():
    def __init__(self, model_detect='checkpoints/CTPN.pth', model_recog='checkpoints/CRNN-1010.pth'):
        self.recognizer = PytorchOcr(model_recog)
        self.detector = PytorchDetect(model_detect)

    def charRec(self, img, text_recs, adjust=False):
        results = {}
        xDim, yDim = img.shape[1], img.shape[0]

        for index, rec in enumerate(text_recs):
            xlength = int((rec[6] - rec[0]) * 0.1)
            ylength = int((rec[7] - rec[1]) * 0.2)
            if adjust:
                pt1 = (max(1, rec[0] - xlength), max(1, rec[1] - ylength))
                pt2 = (rec[2], rec[3])
                pt3 = (min(rec[6] + xlength, xDim - 2), min(yDim - 2, rec[7] + ylength))
                pt4 = (rec[4], rec[5])
            else:
                pt1 = (max(1, rec[0]), max(1, rec[1]))
                pt2 = (rec[2], rec[3])
                pt3 = (min(rec[6], xDim - 2), min(yDim - 2, rec[7]))
                pt4 = (rec[4], rec[5])

            degree = degrees(atan2(pt2[1] - pt1[1], pt2[0] - pt1[0]))  # Góc nghiêng hình ảnh - Image tilt angle

            partImg = dumpRotateImage(img, degree, pt1, pt2, pt3, pt4)
            # dis(partImg)
            if partImg.shape[0] < 1 or partImg.shape[1] < 1 or partImg.shape[0] > partImg.shape[1]:  # Lọc hình ảnh bất thường - Filter abnormal pictures
                continue
            text = self.recognizer.recognize(partImg)
            if len(text) > 0:
                results[index] = [rec]
                results[index].append(text)  

        return results

    def ocr(self, image):
        # detect
        text_recs, img_framed, image = self.detector.get_det_boxes(image)
        text_recs = sort_box(text_recs)
        result = self.charRec(image, text_recs)
        return result, img_framed

if __name__ == '__main__':
    import sys

    myOcr = FinalOCR()

    if len(sys.argv)>=2:
        filename = sys.argv[1]
        if filename.endswith('jpg') or filename.endswith('png') or filename.endswith('jpeg'):
            img = cv2.imread(filename)
            if (img is not None):
                print('IMG Read!')
            else:
                print('IMG not Read!')

            result, image_framed = myOcr.ocr(img)

            print(result)
            for key in result:
                print(result[key][1])
            
            dis(image_framed)