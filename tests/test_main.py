from pytest import approx
from reframe.helpers import get_aspect, get_shape
from reframe.main import create_background, process_image

from .auxiliar import IMAGE_PATH, create_image


def test_create_background_aspect_lesser_than_one():
    tmp_image = create_image(100, 100, 3)
    background = create_background(tmp_image, 0.5)
    bg_aspect = get_aspect(background)
    bg_shape = get_shape(background)
    assert bg_aspect == approx(0.5, abs=0.01)
    assert bg_shape == (100, 200)


def test_create_background_aspect_one():
    tmp_image = create_image(100, 200, 3)
    background = create_background(tmp_image, 1)
    bg_aspect = get_aspect(background)
    bg_shape = get_shape(background)
    assert bg_aspect == approx(1)
    assert bg_shape == (200, 200)


def test_create_background_aspect_greater_than_one():
    tmp_image = create_image(200, 200, 3)
    background = create_background(tmp_image, 1.5)
    bg_aspect = get_aspect(background)
    bg_shape = get_shape(background)
    assert bg_aspect == approx(1.5, abs=0.01)
    assert bg_shape == (300, 200)


def test_process_image():
    output = process_image(IMAGE_PATH, aspect=1)

    out_shape = get_shape(output)
    out_aspect = get_aspect(output)

    assert out_shape == (320, 320)
    assert out_aspect == 1
