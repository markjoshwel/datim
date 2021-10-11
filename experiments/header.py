# type: ignore

from math import ceil, sqrt
from datim import setup
from PIL import ImageColor


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


bev = setup()
inf = open(bev.input, "rb")
dat = inf.read().hex()
nop = len(dat) / 6
cnp = ceil(nop)
lpi = int((cnp - 1) * 6)
ims = ceil(sqrt(cnp))
imp = ims * ims
lpr = ImageColor.getcolor(f"#{dat[lpi:]:0<6}", "RGB")
lhh = int_b15(len(dat)) + "F"
rlh = b15_int(lhh[:-1])

print(
    f"""
length                : {len(dat)}
length header         : {lhh}
length from b15 hex   : {rlh}

number of pixels      : {nop}
number of pixels ceil : {cnp}

image size            : {ims}
pixels in image       : {imp}
pix diff              : {imp - cnp}

last pixel index      : {lpi}
last pixel (lpi)      : {dat[lpi:]}
last pixel (-6)       : {dat[-6:]}
last pixel (lpi) rgb  : {lpr}
"""
    if not bev.silent
    else ""
)

inf.close()
