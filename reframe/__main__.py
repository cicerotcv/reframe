
import os

from .helpers import save_image, show_image
from .main import process_image


def is_float(element: str) -> bool:
    try:
        float(element)
        return True
    except ValueError:
        return False


def process_aspect_arg(aspect: str):
    if is_float(aspect):
        return float(aspect)
    if '/' in aspect:
        w, h = aspect.split('/')
        return float(w)/float(h)
    if ':' in aspect:
        w, h = aspect.split(':')
        return float(w)/float(h)
    raise Exception("Unknown aspect argument format")


def get_args():
    import argparse

    parser = argparse.ArgumentParser()

    cwd = os.getcwd()
    output_destination = os.path.join(cwd, 'output.png')

    parser.add_argument('-i', '--input', type=str, help='input image')

    parser.add_argument('-o', '--output', type=str,
                        default=output_destination,
                        help=f'output image destination. [Defaults to "{output_destination}"]')

    parser.add_argument('-a', '--aspect', type=str, default=1,
                        help="desired aspect ration. [Defaults to 1]")
    parser.add_argument('--save',
                        action='store_true', help='Save output file.')
    parser.add_argument('--show',
                        action='store_true', help='Show output file.')

    args = parser.parse_args()
    args.aspect = process_aspect_arg(args.aspect)

    return args


def main():
    args = get_args()

    image = process_image(args.input, args.aspect)

    if args.show:
        show_image(image)
    if args.save:
        save_image(args.output, image)


if __name__ == "__main__":
    main()
