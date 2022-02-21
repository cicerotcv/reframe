from pytest import approx
from reframe.helpers import (apply_blur, crop_aspect, get_aspect, get_blur_frames, get_shape,
                             rescale)
from reframe.main import (create_background)

from .auxiliar import create_image


def test_get_shape():
    tmp_image = create_image(w=100, h=200, c=3)
    shape = get_shape(tmp_image)
    assert shape == (100, 200)


def test_get_aspect_lesser_than_one():
    tmp_image = create_image(w=100, h=200, c=3)
    aspect = get_aspect(tmp_image)
    assert aspect == 0.5


def test_get_aspect_equals_one():
    tmp_image = create_image(w=100, h=100, c=3)
    aspect = get_aspect(tmp_image)
    assert aspect == 1


def test_get_aspect_greater_than_one():
    tmp_image = create_image(w=200, h=100, c=3)
    aspect = get_aspect(tmp_image)
    assert aspect == 2


def test_crop_aspect_lesser_than_one():
    tmp_image = create_image(w=100, h=200, c=3)
    output = crop_aspect(tmp_image, 0.5)
    aspect = get_aspect(output)
    assert aspect == approx(0.5, 0.1)


def test_crop_aspect_equals_one():
    tmp_image = create_image(w=100, h=200, c=3)
    output = crop_aspect(tmp_image, 1)
    aspect = get_aspect(output)
    assert aspect == approx(1)


def test_crop_aspect_greater_than_one():
    tmp_image = create_image(w=1000, h=2000, c=3)
    output = crop_aspect(tmp_image, 1.5)
    aspect = get_aspect(output)
    assert aspect == approx(1.5, abs=0.1)


def test_rescale():
    tmp_image = create_image(w=100, h=200, c=3)
    output = rescale(tmp_image, 2)
    assert get_shape(output) == (200, 400)


def test_get_blur_frames():
    tmp_image = create_image(w=100, h=100, c=3)
    tmp_background = create_background(tmp_image, 2)
    img_shape = get_shape(tmp_image)
    bg_shape = get_shape(tmp_background)

    frame1, frame2 = get_blur_frames(img_shape, bg_shape)

    assert frame1 == ((0, 0), (50, 100))
    assert frame2 == ((150, 0), (200, 100))


def test_apply_blur():
    tmp_image = create_image(w=100, h=200, c=3)
    full_frame = ((0, 0), (100, 200))
    output = apply_blur(tmp_image, 20, full_frame)
    assert tmp_image.shape == output.shape
