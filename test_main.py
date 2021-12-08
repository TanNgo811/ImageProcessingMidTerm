import cv2
from preprocessing import preprocessing
from ocr import ocr
from data_extraction import data_extraction

if __name__ == '__main__':
    file_name = './test_images/img4.jpeg'
    image = cv2.imread(file_name)

    # resize_ratio = 500 / image.shape[0]

    resize_ratio = 1

    # Preprocess Image
    pre_image = preprocessing.preprocessing(image, resize_ratio)

    # OCR
    result, image_framed = ocr(pre_image)

    # Data Extraction

    data = ''

    for key in result:
        data = data + result[key][1] + ' '
        print(result[key][1])

    print(data_extraction.data_extraction(data))

    cv2.imshow('abc', image_framed)
    cv2.waitKey()
