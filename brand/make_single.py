"""Build a branded single-photo image (Instagram 4:5) with the same orange strip as the before/after posts.
Usage: python3 brand/make_single.py <photo.jpg> "<Service · Town>" <out.jpg> [cx,cy]"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw, ImageOps
from make_post import logo, strip_big


def build(photo, line, out, centre=(0.5, 0.5)):
    white, orange = logo()
    p = ImageOps.exif_transpose(Image.open(photo)).convert('RGB')
    W, H, bar = 1080, 1350, 236
    t = Image.new('RGB', (W, H), orange)
    t.paste(ImageOps.fit(p, (W, H - bar), Image.LANCZOS, centering=centre), (0, 0))
    d = ImageDraw.Draw(t)
    service, town = [x.strip() for x in line.split('·')]
    strip_big(t, d, service, town, W, H, bar, white)
    t.save(out, quality=90)


if __name__ == '__main__':
    a = sys.argv
    c = tuple(float(x) for x in a[4].split(',')) if len(a) > 4 else (0.5, 0.5)
    build(a[1], a[2], a[3], c)
