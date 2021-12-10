#
# You can modify this files
#

import cv2
from preprocessing import preprocessing
from ocr import *
from data_extraction import data_extraction

class HoadonOCR:

    def __init__(self):
        # Init parameters, load model here
        self.model = FinalOCR()
        self.labels = ['highlands', 'starbucks', 'phuclong', 'others']

    # TODO: implement find label
    def find_label(self, img):
        # return self.labels[random.randint(0, 3)]

        # resize_ratio = 500 / image.shape[0]

        resize_ratio = 1

        # Preprocess Image
        pre_image = preprocessing.preprocessing(img, resize_ratio)

        # OCR
        result, image_framed = self.model.ocr(pre_image)

        # Data Extraction

        data = ''

        for key in result:
            data = data + result[key][1] + ' '

        return data_extraction.data_extraction(data)
