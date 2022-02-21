import cv2


def load_image(path: str):
    return cv2.imread(path)


def get_shape(image):
    height, width, _ = image.shape
    return (width, height)


def get_aspect(image):
    width, height = get_shape(image)
    return width/height


def crop_aspect(image, aspect):
    width, height = get_shape(image)
    img_aspect = width/height

    if aspect > img_aspect:
        new_height = round(width/aspect)
        py = round((height - new_height) / 2)
        return image[py:py + new_height, :]

    if aspect < img_aspect:
        new_width = round(height*aspect)
        px = round((width - new_width) / 2)
        return image[:, px:px + new_width]

    return image


def rescale(image, scale):
    width, height = get_shape(image)

    new_width = round(width*scale)
    new_height = round(height*scale)

    new_shape = (new_width, new_height)

    return cv2.resize(image, new_shape)


def apply_blur(image, size):
    if size % 2 == 0:
        size += 1
    kernel_size = (size, size)
    sigma_x = 0
    image = cv2.GaussianBlur(image, kernel_size, sigma_x)
    return image
