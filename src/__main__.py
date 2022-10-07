import argparse

parser = argparse.ArgumentParser(prog="signpic-generator",
                                 description='Generate a string for the SignPic Minecraft mod.',
                                 epilog="For more information on this string format, see https://ftb.fandom.com/wiki/SignPic.")

parser.add_argument('--url', "-u",
                    metavar='url',
                    type=str,
                    help='the URL of the image to show in the sign, including http:// or https://')

parser.add_argument('--image-width', "-iw",
                    metavar='width',
                    type=str,
                    help='the width of the image to display')

parser.add_argument('--image-height', "-ih",
                    metavar='width',
                    type=str,
                    help='the height of the image to display')

parser.add_argument('--width-offset', "-wo",
                    metavar='width',
                    type=str,
                    help='the width of the image offset')

parser.add_argument('--height-offset', '-ho',
                    metavar='width',
                    type=str,
                    help='the height of the image offset')

parser.add_argument('-v', '--vertical',
                    action='store_true',
                    help='change the orientation of the image to vertical')


def string_formatter(url: str,
                     image_width: str,
                     image_height: str,
                     width_offset: str,
                     height_offset: str,
                     vertical: str
                     ):
    if vertical:
        vertical = "R"
    else:
        vertical = ""

    if url.startswith("https://"):
        secure = "$"
    else:
        secure = ""

    url = url.replace("http://", "")
    url = url.replace("https://", "")

    return f"#{secure}{url}{{{image_width}x{image_height}, {width_offset}x{height_offset}{vertical}}}"


args = parser.parse_args()

print(string_formatter(
    url=args.url,
    image_width=args.image_width,
    image_height=args.image_height,
    width_offset=args.width_offset,
    height_offset=args.height_offset,
    vertical=args.vertical
))
