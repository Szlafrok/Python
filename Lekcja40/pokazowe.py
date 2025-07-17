filepath = "Lekcja40/"

import cv2
import numpy as np
from PIL import Image

def show_image(img):
    cv2.imshow("Obrazek", img) # Argumenty: nazwa okna, obiekt obrazka.
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def read_image_cv(path):
    img = cv2.imread(path, cv2.IMREAD_COLOR) # BGR
    print(img) 
    print(img.shape)
    print(type(img))
    return img

img_obj = read_image_cv(f"{filepath}goku.jpg")
show_image(img_obj)

def read_image_pil(path):
    im = Image.open(path)
    try:
        print(im)
    except:
        print(type(im))
    im.show()
    return im
#read_image_pil(f"{filepath}goku.jpg")

def reverse_image(img):
    new_img = []
    for row in range(img.shape[0] - 1, -1, -1):
        new_img.append(img[row])
    return np.array(new_img)

show_image(reverse_image(img_obj))


def grayscale(img):
    for row in range(img.shape[0]):
        for column in range(img.shape[1]):
            pixel = img[row][column].astype(np.uint16)
            gray = int(sum(pixel) / 3)
            img[row][column] = np.array([gray, gray, gray])
    return np.array(img, dtype = np.uint8)

img = grayscale(img_obj)
show_image(img)