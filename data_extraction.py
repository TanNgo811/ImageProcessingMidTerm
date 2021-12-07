import sys
import os
import numpy as np
from PIL import Image
from ocr import ocr
import re

def data_extraction_file(image_file):

    return


def single_pic_proc(image_file):
    image = np.array(Image.open(image_file).convert('RGB'))
    result, image_framed = ocr(image)
    return result,image_framed


if __name__ == "__main__":

    # Chinese Filter
    pattern = re.compile("[\u4E00-\u9FFF]+")

    if len(sys.argv) >= 2:
        output_folder_dir = sys.argv[1]
        filename = sys.argv[2]

        if filename.endswith('jpg') or filename.endswith('png'):
            result, image_framed = single_pic_proc(filename)

            output_file = os.path.join(output_folder_dir, filename.split('\\')[-1])

            txt_file = os.path.join(output_folder_dir, filename.split('\\')[-1].split('.')[0]+'.txt')

            print(txt_file)

            txt_f = open(txt_file, 'w')

            for key in result:
                # if 'we' in result[key][1]:
                #     print('contain')
                print(result[key][1])
                change_text = re.sub(pattern, " ", result[key][1])
                if (change_text is not None):
                    print(change_text)
                    txt_f.write(change_text + '')

            txt_f.close()