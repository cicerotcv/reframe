import os
from sys import argv

import cv2

from reframe import process_image


def main():
    path = argv[1]
    aspect = float(argv[2])
    output = process_image(path, aspect)
    show_image(output)
    cwd = os.getcwd()
    save_image(output, f'{cwd}/output.png')


def save_image(image, filename='output.png'):
    cv2.imwrite(filename, image)


def show_image(image):
    height, width, _ = image.shape
    aspect = height/width

    WIDTH = 400

    cv2.imshow("Image", cv2.resize(image, (WIDTH, int(WIDTH*aspect))))
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
