from sys import argv
from reframe import process_image, load_image
import cv2


def main():
    path = argv[1]
    image = load_image(path)
    output = process_image(image)
    show_image(output)
    save_image(output, 'output.png')


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
