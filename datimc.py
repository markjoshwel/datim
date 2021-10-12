"""
datimc (datim compiled)
-----------------------

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org/>
"""

from argparse import ArgumentParser
from math import ceil, sqrt
from pathlib import Path
from os import _exit

from typing import Dict, Union, Tuple, NamedTuple

from lz4.frame import compress, decompress  # type: ignore
from PIL import Image  # type: ignore

try:
    from tqdm import trange  # type: ignore

except ImportError:
    TQDM_AVAILABLE = False

else:
    TQDM_AVAILABLE = True


c16: Dict[str, int] = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "a": 10,
    "b": 11,
    "c": 12,
    "d": 13,
    "e": 14,
    "f": 15,
}


# TODO: Revert on mypy 0.920 (mypyc#861)
#       Once done adjust pyproject.toml
#
# class Behaviour(NamedTuple):
#     input: Path
#     output: Path
#     overwrite: bool
#     tqdm: bool
#     compress: bool = True
#     alpha: bool = True

Behaviour = NamedTuple(
    "Behaviour",
    [
        ("input", Path),
        ("output", Path),
        ("overwrite", bool),
        ("tqdm", bool),
        ("compress", bool),
        ("alpha", bool),
    ],
)


def h6_rgba(
    h: str, alpha: bool = True
) -> Union[Tuple[int, int, int], Tuple[int, int, int, int]]:
    r: int = 0
    g: int = 0
    b: int = 0

    rlh: str = h[::-1].lower()

    # aabbggrr
    # 87654321

    for bpl, chr in enumerate(rlh[-2:]):
        r += (16 ** bpl) * c16[chr]

    for bpl, chr in enumerate(rlh[-4:-2]):
        g += (16 ** bpl) * c16[chr]

    for bpl, chr in enumerate(rlh[-6:-4]):
        b += (16 ** bpl) * c16[chr]

    if alpha:
        a: int = 0

        for bpl, chr in enumerate(rlh[:-6]):
            a += (16 ** bpl) * c16[chr]

        return (r, g, b, a)

    else:
        return (r, g, b)


def int_b15(n: int) -> str:
    res: str = ""
    rem: int = 0
    c15: str = "0123456789abcde"

    while n > 0:
        rem = n % 15
        res = c15[rem] + res
        n //= 15

    return res


def b15_int(h: str) -> int:
    res: int = 0

    for plv, chr in enumerate(h[::-1]):
        res += (15 ** plv) * c16[chr]

    return res


def gen(h: str = "", alpha: bool = True) -> str:
    h += "0" * ((8 if alpha else 6) - len(h))
    return h


def setup(desc: str = ""):
    parser = ArgumentParser(description=desc)

    parser.add_argument("input", type=str, help="input file path")
    parser.add_argument("output", type=str, help="output file path")
    parser.add_argument(
        "-o", "--overwrite", action="store_true", help="overwrite without confirmation"
    )
    parser.add_argument(
        "-np",
        "--no-progress",
        dest="progress",
        action="store_false",
        help="do not use tqdm",
    )
    parser.add_argument(
        "-nc",
        "--no-compress",
        dest="compress",
        action="store_false",
        help="do not compress data",
    )
    parser.add_argument(
        "-na",
        "--no-alpha",
        dest="alpha",
        action="store_false",
        help="do not use alpha channel",
    )
    args = parser.parse_args()

    ip: Path = Path(args.input)
    op: Path = Path(args.output)

    if not ip.is_file():
        if ip.is_dir():
            print(f"input file '{ip}' is a directory")
            _exit(-1)

        else:
            print(f"input file '{ip}' does not exist")

    if op.is_file():
        if args.overwrite:
            query = input(f"overwrite {op}? [Y/N]: ")

            if not (query == "Y" or query == "y"):
                _exit(-1)

    elif op.is_dir():
        print(f"output file '{op}' is a directory")
        _exit(-1)

    return Behaviour(
        input=ip,
        output=op,
        overwrite=args.overwrite,
        tqdm=(True if TQDM_AVAILABLE and args.progress else False),
        compress=args.compress,
        alpha=args.alpha,
    )


def datim(bev: Behaviour) -> None:
    inp = bev.input.open("rb")
    dat = inp.read()

    if bev.compress:
        cdat = compress(dat).hex()
        fdat = int_b15(len(cdat)) + "f" + cdat

    else:
        hdat = dat.hex()
        fdat = int_b15(len(hdat)) + "f" + hdat

    pxl: int = 8 if bev.alpha else 6  # pixel length
    isz: int = ceil(sqrt(ceil(len(fdat) / pxl)))
    img: Image.Image = Image.new(mode="RGBA" if bev.alpha else "RGB", size=(isz, isz))
    pax = img.load()  # type: ignore

    lb = 0
    ub = pxl

    rng = trange(img.size[0]) if bev.tqdm else range(img.size[0])

    for y in range(img.size[1]):
        for x in rng:
            if lb > len(fdat):  # out of data
                pax[x, y] = (0, 0, 0, 0) if bev.alpha else (0, 0, 0)  # type: ignore

            elif ub > len(fdat):  # last pixel
                lpi = int((ceil(len(fdat) / pxl) - 1) * pxl)
                pax[x, y] = h6_rgba(gen(fdat[lpi:], alpha=bev.alpha), alpha=bev.alpha)  # type: ignore

            else:
                pax[x, y] = h6_rgba(fdat[lb:ub], alpha=bev.alpha)  # type: ignore

            lb += pxl
            ub += pxl

    img.save(str(bev.output.absolute()))
    img.close()
    inp.close()


def imdat(bev: Behaviour) -> None:
    img: Image.Image = Image.open(bev.input)
    rha: str = ""  # recovered/reversed hex array
    pax = img.load()  # type: ignore

    if not (img.mode == "RGB" or img.mode == "RGBA"):
        print(f"input file '{bev.input}' is not RGB or RGBA")
        exit(-1)

    alpha: bool = True if len(pax[0, 0]) == 4 else False  # type: ignore

    rng = trange(img.size[0]) if bev.tqdm else range(img.size[0])

    for y in range(img.size[1]):
        for x in rng:
            clr = pax[x, y]  # type: ignore
            rha += f"{clr[0]:02x}{clr[1]:02x}{clr[2]:02x}"

            if alpha:
                rha += f"{clr[3]:02x}"

    hed, rem = rha.split("f", 1)
    dat: bytes = bytes.fromhex(rem[: b15_int(hed)])

    with bev.output.open("wb") as of:
        try:
            of.write(decompress(dat))

        except RuntimeError:
            of.write(dat)

    img.close()
