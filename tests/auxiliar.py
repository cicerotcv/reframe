import numpy as np
from reframe.helpers import load_image

IMAGE_PATH = 'tests/test.png'
image = load_image(IMAGE_PATH)


def create_image(w, h, c):
    return np.ones((h, w, c))*255
