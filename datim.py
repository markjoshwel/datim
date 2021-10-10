from argparse import ArgumentParser, FileType
from math import ceil, sqrt
from pathlib import Path
from zlib import compress, decompress
from typing import NamedTuple

from PIL import Image, ImageColor

try:
    from tqdm import tqdm

except ImportError:
    TQDM_AVAILABLE = False

else:
    TQDM_AVAILABLE = True


class Behaviour(NamedTuple):
    input: str
    output: str
    overwrite: bool
    silent: bool
    tqdm: bool


def setup() -> Behaviour:
    parser = ArgumentParser(description="Turns any file into an image")
    parser.add_argument("input", type=str)
    parser.add_argument("output", type=str)
    parser.add_argument("-o", "--overwrite", action="store_true")
    parser.add_argument("-s", "--silent", action="store_true")
    args = parser.parse_args()

    if Path(args.output).is_file() and not args.overwrite:
        query = input(f"Overwrite {args.output}? [Y/N]: ")

        if not (query == "Y" or query == "y"):
            exit()

    if Path(args.output).is_dir():
        print(f"{args.output} is a directory")
        exit(-1)

    return Behaviour(
        args.input,
        args.output,
        args.overwrite,
        args.silent,
        True if TQDM_AVAILABLE and not args.silent else False,
    )


def datim():
    bv = setup()

    # Data Read
    with open(bv.input, "rb") as input_file:
        data = input_file.read()

    # Data Compression
    cdat = compress(data).hex()

    # Image Generation
    if bv.tqdm:
        gbar = tqdm(total=len(cdat), desc="Progress")

    height = ceil(sqrt(ceil(len(cdat) / 6)))
    image = Image.new(mode="RGB", size=(height, height))

    lb = 0
    ub = 6

    for pw in range(image.size[0]):
        for ph in range(image.size[1]):
            if ub > len(cdat):
                colour = (255, 255, 255)
            else:
                colour = ImageColor.getcolor(f"#{cdat[lb:ub]}", "RGB")

            image.putpixel((pw, ph), colour)

            lb += 6
            ub += 6

            if bv.tqdm:
                gbar.update(6)  # type: ignore

    if bv.tqdm:
        gbar.close()  # type: ignore

    image.save(bv.output)


def imdat():
    bv = setup()

    # Image Reversal
    image = Image.open(bv.input)
    rhex = ""
    pax = image.load()

    if bv.tqdm:
        gbar = tqdm(total=image.size[0] * image.size[1], desc="Progress")

    for pw in range(image.size[0]):
        for ph in range(image.size[1]):
            r, g, b = pax[pw, ph]  # type: ignore
            rhex += f"{r:02x}{g:02x}{b:02x}"

            if bv.tqdm:
                gbar.update()  # type: ignore

    if bv.tqdm:
        gbar.close()  # type: ignore

    rcdat = bytes.fromhex(rhex)

    # Data Decompression
    rdat = decompress(rcdat)

    # Data Write
    with open(bv.output, "rb") as of:
        of.write(rdat)
