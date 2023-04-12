from architecture import *
import cv2
from matplotlib import pyplot as plt

IMAGE_PATH = 'images/leaf.jpg'

def convert_truth():
    img = cv2.imread(IMAGE_PATH)
    gray_scale_img = []
    print(img.shape)
    for row in range(img.shape[0]):
        row_local = []
        for col in range(img.shape[1]):
            pixel = img[row][col]
            value = (pixel[0] << 16) + (pixel[1] << 8) + pixel[0]

            grayscale_value = architecture_truth(value)

            row_local.append(grayscale_value)
        gray_scale_img.append(row_local)
    return gray_scale_img


def convert_paper_arch():
    img = cv2.imread(IMAGE_PATH)
    gray_scale_img = []
    print(img.shape)
    for row in range(img.shape[0]):
        row_local = []
        for col in range(img.shape[1]):
            pixel = img[row][col]
            value = (pixel[0] << 16) + (pixel[1] << 8) + pixel[0]

            grayscale_value = architecture_paper(value)

            row_local.append(grayscale_value)
        gray_scale_img.append(row_local)
    return gray_scale_img


def convert_arch1():
    img = cv2.imread(IMAGE_PATH)
    gray_scale_img = []
    print(img.shape)
    for row in range(img.shape[0]):
        row_local = []
        for col in range(img.shape[1]):
            pixel = img[row][col]
            value = (pixel[0] << 16) + (pixel[1] << 8) + pixel[0]

            grayscale_value = architecture_1(value)

            row_local.append(grayscale_value)
        gray_scale_img.append(row_local)
    return gray_scale_img


def convert_arch2():
    img = cv2.imread(IMAGE_PATH)
    gray_scale_img = []
    print(img.shape)
    for row in range(img.shape[0]):
        row_local = []
        for col in range(img.shape[1]):
            pixel = img[row][col]
            value = (pixel[0] << 16) + (pixel[1] << 8) + pixel[0]

            grayscale_value = architecture_2(value)

            row_local.append(grayscale_value)
        gray_scale_img.append(row_local)
    return gray_scale_img


if __name__ == "__main__":
    # read image as RGB
    truth = convert_truth()
    paper = convert_paper_arch()
    arch1 = convert_arch1()
    arch2 = convert_arch2()
    
    plt.subplot(1, 4, 1)
    plt.imshow(truth, cmap='gray')
    plt.subplot(1, 4, 2)
    plt.imshow(paper, cmap='gray')
    plt.subplot(1, 4, 3)
    plt.imshow(arch1, cmap='gray')
    plt.subplot(1, 4, 4)
    plt.imshow(arch2, cmap='gray')
    plt.show()

