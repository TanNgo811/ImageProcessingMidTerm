#
# You can modify this files
#

import cv2
from preprocessing import preprocessing
from ocr import ocr
from data_extraction import data_extraction

class HoadonOCR:

    def __init__(self):
        # Init parameters, load model here
        self.model = None
        self.labels = ['highlands', 'starbucks', 'phuclong', 'others']

    # TODO: implement find label
    def find_label(self, img):

        resize_ratio = 1

        # Preprocess Image
        pre_image = preprocessing.preprocessing(img, resize_ratio)

        # OCR
        result, image_framed = ocr(pre_image)

        # Data Extraction

        data = ''

        for key in result:
            data = data + result[key][1] + ' '

        return data_extraction.data_extraction(data)
