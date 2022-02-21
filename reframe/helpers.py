import cv2


def load_image(path: str):
    return cv2.imread(path)


def save_image(path: str, image):
    cv2.imwrite(path, image)
    print(f'Image saved at "{path}"')


def show_image(image):
    width, height = get_shape(image)
    greater = max(width, height)
    scale = 640/greater
    cv2.imshow("Output", rescale(image, scale))
    cv2.waitKey(0)
    cv2.destroyAllWindows()


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


def get_blur_frames(img_shape, bg_shape):
    img_width, img_height = img_shape
    bg_width, bg_height = bg_shape

    img_aspect = img_width / img_height
    bg_aspect = bg_width / bg_height

    if bg_aspect > img_aspect:  # padding x
        px = round((bg_width - img_width)/2)
        frame1 = ((0, 0), (px, bg_height))
        frame2 = ((px + img_width, 0), (bg_width, bg_height))
        return frame1, frame2
    if bg_aspect < img_aspect:  # padding y
        py = round((bg_height - img_height)/2)
        frame1 = ((0, 0), (bg_width, py))
        frame2 = ((0, py + img_height), (bg_width, bg_height))
        return frame1, frame2

    frame1 = ((0, 0), (0, 0))
    frame2 = ((0, 0), (0, 0))

    return frame1, frame2


def apply_blur(image, size, frame):
    (xi, yi), (xf, yf) = frame

    if all([component == 0 for component in [xi, yi, xf, yf]]):
        return image

    if size % 2 == 0:
        size += 1

    blur_frame = image[yi:yf, xi: xf]
    kernel_size = (size, size)
    sigma_x = 0
    blur_frame = cv2.GaussianBlur(blur_frame, kernel_size, sigma_x)

    image[yi:yf, xi: xf] = blur_frame

    return image
