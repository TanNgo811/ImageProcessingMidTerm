import cv2
from preprocessing import preprocessing
from ocr import FinalOCR
from data_extraction import data_extraction
import time

if __name__ == '__main__':
    file_name = './test_images/img6.jpeg'
    image = cv2.imread(file_name)
    start_time = time.time()

    # resize_ratio = 500 / image.shape[1]
    myocr = FinalOCR()

    resize_ratio = 1

    # Preprocess Image
    pre_image = preprocessing.preprocessing(image, resize_ratio)

    # OCR
    result, image_framed = myocr.ocr(pre_image)

    # Data Extraction

    data = ''

    for key in result:
        data = data + result[key][1] + ' '
        print(result[key][1])
        
    print(data_extraction.data_extraction(data))

    run_time = time.time() - start_time

    print("Run time: ", run_time)

    cv2.imshow('abc', image_framed)
    cv2.waitKey()

