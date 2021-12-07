import cv2
from preprocessing import preprocessing

if __name__ == '__main__':
    file_name = './test_images/img4.jpeg'
    image = cv2.imread(file_name)

    resize_ratio = 500 / image.shape[0]

    result = preprocessing.preprocessing(image, resize_ratio)

    print(result)

    cv2.imshow('abc', result)
    cv2.waitKey()

    print('test')