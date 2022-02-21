# -*- encoding::utf-8 -*-
from .helpers import apply_blur, crop_aspect, get_shape, load_image, rescale


def create_background(image, desired_aspect):

    im_width, im_height = get_shape(image)
    im_aspect = im_width/im_height

    scale = max(desired_aspect, im_aspect) / min(desired_aspect, im_aspect)

    # makes background big enough to fit the desired aspect
    background = rescale(image, scale=scale)
    background = crop_aspect(background, aspect=desired_aspect)

    kernel_size = max(get_shape(background)) // 15
    background = apply_blur(background, kernel_size)

    return background


def place_image(background, image):
    im_width, im_height = get_shape(image)
    bg_width, bg_height = get_shape(background)

    px = round((bg_height - im_height)/2)
    py = round((bg_width - im_width)/2)

    output = background.copy()

    start_col = px
    end_col = start_col + im_height

    start_row = py
    end_row = start_row + im_width

    output[start_col:end_col, start_row: end_row] = image
    return output


def process_image(path, aspect):
    image = load_image(path)
    background = create_background(image, aspect)
    return place_image(background, image)
