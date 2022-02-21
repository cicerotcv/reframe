# Python Reframe

![Tests](https://github.com/cicerotcv/reframe/actions/workflows/python-app.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3670A0?logo=python&logoColor=ffdd54)
![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?logo=opencv&logoColor=white)

Changes any supported image's aspect ratio by resizing the original image to create a blured background.

## Instalation

```shell
$ pip install -r requirements.txt
```

## Arguments

```
usage: reframe [-h] [-i INPUT] [-o OUTPUT] [-a ASPECT] [--save] [--show]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        input image
  -o OUTPUT, --output OUTPUT
                        output image destination. [Defaults to "current\dir\output.png"]
  -a ASPECT, --aspect ASPECT
                        desired aspect ration.
                        [Defaults to 1]
                        [Formats d, d.d, d/d, d:d]
                        [Exemples 1, 1.5, 16/9, 16:9]
  --save                Save output file.
  --show                Show output file.
```

## Usage

```shell
$ python -m reframe -i path/to/image.png --save --show -a 16:9
```

## Results

```shell
$ python -m reframe -i tests/test.png -o demo.png --aspect 2 --save
```

![demo image](demo.png)
