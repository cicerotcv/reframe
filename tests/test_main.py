from reframe import main
import numpy as np

image = np.ones((240, 320, 3))
im_height, im_width, im_components = image.shape


def test_create_background():
    bg = main.create_background(image)
    bg_height, _, bg_components = bg.shape
    assert (bg_height, bg_components) == (im_width, im_components)


def test_apply_blur():
    blured = main.apply_blur(image, 10)
    assert blured.shape == image.shape


def test_resize():
    resized = main.resize(image)
    assert resized.shape == (im_width, round(
        im_width * im_width/im_height), im_components)


def test_reframe():
    reframed = main.reframe(image)
    assert reframed.shape == (im_height, im_height, im_components)
