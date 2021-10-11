# type: ignore

from PIL import Image
from datim import b15_int, setup

bev = setup()
image = Image.open(bev.input)
pax = image.load()

rhex = ""

for ph in range(image.size[0]):
    for pw in range(image.size[1]):
        r, g, b = pax[pw, ph]  # type: ignore
        rhex += f"{r:02x}{g:02x}{b:02x}"

hdr, rdat = rhex.split("f", 1)
length = b15_int(hdr)

print(f"(read-header) Header: {hdr}, Length: {length}")
