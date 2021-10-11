from lz4.frame import compress, decompress  # type: ignore
from argparse import ArgumentParser
from typing import NamedTuple
from random import randint
from math import ceil, sqrt
from pathlib import Path

from PIL import Image, ImageColor  # type: ignore

try:
    from tqdm import tqdm  # type: ignore

except ImportError:
    TQDM_AVAILABLE = False

else:
    TQDM_AVAILABLE = True


def int_b15(n: int) -> str:
    res = ""
    rem = 0
    chi = "0123456789abcde"

    while n > 0:
        rem = n % 15
        res = chi[rem] + res
        n //= 15

    return res


def b15_int(h: str) -> int:
    chi = "0123456789abcde"
    res = 0

    for bpl, chr in enumerate(h[::-1]):
        res += (15 ** bpl) * chi.index(chr)

    return res


def gen(h: str = "") -> str:
    for i in range(6 - len(h)):
        h += "0123456789abcdef"[randint(0, 15)]

    return h


class Behaviour(NamedTuple):
    input: str
    output: str
    overwrite: bool
    silent: bool
    tqdm: bool
    compress: bool = True


def setup(desc: str = "turns any file into an image") -> Behaviour:
    parser = ArgumentParser(description=desc)
    parser.add_argument("input", type=str, help="input file path")
    parser.add_argument("output", type=str, help="output file path")
    parser.add_argument(
        "-o", "--overwrite", action="store_true", help="overwrite without confirmation"
    )
    parser.add_argument(
        "-s", "--silent", action="store_true", help="do not use tqdm even if available"
    )
    parser.add_argument(
        "-nc",
        "--no-compress",
        dest="compress",
        action="store_false",
        help="do not compress data",
    )
    args = parser.parse_args()

    if Path(args.output).is_file() and not args.overwrite:
        query = input(f"Overwrite {args.output}? [Y/N]: ")

        if not (query == "Y" or query == "y"):
            exit(-1)

    if Path(args.output).is_dir():
        print(f"{args.output} is a directory")
        exit(-1)

    return Behaviour(
        args.input,
        args.output,
        args.overwrite,
        args.silent,
        True if TQDM_AVAILABLE and not args.silent else False,
        args.compress,
    )


def datim(bev: Behaviour) -> None:
    # Data Read
    with open(bev.input, "rb") as input_file:
        data = input_file.read()

    # Data Compression + Header Addition
    if bev.compress:
        cdat = compress(data).hex()
        fdat = int_b15(len(cdat)) + "F" + cdat

    else:
        hdat = data.hex()
        fdat = int_b15(len(hdat)) + "F" + hdat

    # Image Generation
    if bev.tqdm:
        gbar = tqdm(total=len(fdat), desc="Image Generation")

    height = ceil(sqrt(ceil(len(fdat) / 6)))
    image = Image.new(mode="RGB", size=(height, height))

    lb = 0
    ub = 6

    for ph in range(image.size[0]):
        for pw in range(image.size[1]):
            if lb > len(fdat):  # out of data
                colour = ImageColor.getcolor(f"#{gen()}", "RGB")

            elif ub > len(fdat):  # last pixel
                lpi = int((ceil(len(fdat) / 6) - 1) * 6)
                colour = ImageColor.getcolor(f"#{gen(fdat[lpi:])}", "RGB")

            else:
                colour = ImageColor.getcolor(f"#{fdat[lb:ub]}", "RGB")

            image.putpixel((pw, ph), colour)

            lb += 6
            ub += 6

            if bev.tqdm:
                gbar.update(6)  # type: ignore

    if bev.tqdm:
        gbar.close()  # type: ignore

    image.save(bev.output)


def imdat(bev: Behaviour) -> None:
    # Image Reversal
    image = Image.open(bev.input)
    rhex = ""
    pax = image.load()

    if bev.tqdm:
        gbar = tqdm(total=image.size[0] * image.size[1], desc="Image Reversal")

    for ph in range(image.size[0]):
        for pw in range(image.size[1]):
            colour = pax[pw, ph]  # type: ignore
            rhex += f"{colour[0]:02x}{colour[1]:02x}{colour[2]:02x}"

            if bev.tqdm:
                gbar.update()  # type: ignore

    if bev.tqdm:
        gbar.close()  # type: ignore

    # Data Parsing
    hdr, rchex = rhex.split("f", 1)
    rclen = b15_int(hdr)

    rdat = bytes.fromhex(rchex[:rclen])

    # Decompression/Write out
    with open(bev.output, "wb") as of:
        try:
            of.write(decompress(rdat))

        except RuntimeError:
            of.write(rdat)


def setup_datim() -> None:
    datim(setup())


def setup_imdat() -> None:
    imdat(setup("turns previously converted images into the original file"))
