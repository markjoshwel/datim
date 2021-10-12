"""
datimc by Mark Joshwel
----------------------

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

from random import randint
from typing import Union, Tuple


def h6_rgba(
    h: str, alpha: bool = True
) -> Union[Tuple[int, int, int], Tuple[int, int, int, int]]:
    chi: str = "0123456789abcdef"
    r: int = 0
    g: int = 0
    b: int = 0

    rlh = h[::-1].lower()

    # aabbggrr
    # 87654321

    for bpl, chr in enumerate(rlh[-2:]):
        r += (16 ** bpl) * chi.index(chr)

    for bpl, chr in enumerate(rlh[-4:-2]):
        g += (16 ** bpl) * chi.index(chr)

    for bpl, chr in enumerate(rlh[-6:-4]):
        b += (16 ** bpl) * chi.index(chr)

    if alpha:
        a: int = 0

        for bpl, chr in enumerate(rlh[:-6]):
            a += (16 ** bpl) * chi.index(chr)

        return (r, g, b, a)

    else:
        return (r, g, b)


def int_b15(n: int) -> str:
    res: str = ""
    rem: int = 0
    chi: str = "0123456789abcde"

    while n > 0:
        rem = n % 15
        res = chi[rem] + res
        n //= 15

    return res


def b15_int(h: str) -> int:
    chi: str = "0123456789abcde"
    res: int = 0

    for plv, chr in enumerate(h[::-1]):
        res += (15 ** plv) * chi.index(chr)

    return res


def gen(h: str = "") -> str:
    for _ in range(6 - len(h)):
        h += "0123456789abcdef"[randint(0, 15)]

    return h
