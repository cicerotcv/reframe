from .helpers import (apply_blur, crop_aspect, get_aspect, get_blur_frames,
                      get_shape, load_image, rescale, show_image)


def create_background(image, desired_aspect):
    im_aspect = get_aspect(image)

    scale = max(desired_aspect, im_aspect) / min(desired_aspect, im_aspect)

    # makes background big enough to fit the desired aspect
    background = rescale(image, scale=scale)
    background = crop_aspect(background, aspect=desired_aspect)

    img_shape = get_shape(image)
    bg_shape = get_shape(background)

    kernel_size = max(bg_shape) // 15

    frame1, frame2 = get_blur_frames(img_shape, bg_shape)

    background = apply_blur(background, kernel_size, frame1)
    background = apply_blur(background, kernel_size, frame2)

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
