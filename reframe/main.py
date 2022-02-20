# -*- encoding::utf-8 -*-
import cv2


def load_image(path: str):
    return cv2.imread(path)


def resize(image):
    height, width, _ = image.shape

    scale = max(width, height)/min(width, height)

    new_width = round(width*scale)
    new_height = round(height*scale)
    new_shape = (new_width, new_height)

    return cv2.resize(image, new_shape)


def reframe(image):
    height, width, _ = image.shape

    size = min(width, height)

    px = round((width - size)/2)
    px = max(0, px)

    py = round((height - size)/2)
    py = max(0, py)

    output = image.copy()
    output = output[py:py + size, px: px + size]
    return output


def apply_blur(image, size):
    if size % 2 == 0:
        size += 1
    kernel_size = (size, size)
    sigma_x = 0
    image = cv2.GaussianBlur(image, kernel_size, sigma_x)
    return image


def create_background(image):
    height, width, _ = image.shape
    size = max(height, width)

    background = resize(image)
    background = reframe(background)
    background = apply_blur(background, size//15)

    return background


def place_image(background, image):
    im_height, im_width, _ = image.shape
    bg_height, bg_width, _ = background.shape

    px = round((bg_height - im_height)/2)
    py = round((bg_width - im_width)/2)

    output = background.copy()

    start_col = px
    end_col = start_col + im_height

    start_row = py
    end_row = start_row + im_width

    output[start_col:end_col, start_row: end_row] = image
    return output


def process_image(image):
    background = create_background(image)
    return place_image(background, image)
