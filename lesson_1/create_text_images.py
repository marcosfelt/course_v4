from PIL import Image, ImageDraw, ImageFont
import lorem
import textwrap
import random
import pathlib

def create_wrapped_text(width=20)-> list:
    p = lorem.paragraph()
    return textwrap.wrap(p, width=width)    

def create_image(img: Image ,font: ImageFont=None,  margin: int=10, offset: int=10):
    draw = ImageDraw.Draw(img)
    font = font if font is not None else ImageFont.truetype('/Library/Fonts/Arial.ttf', 15)
    wt = create_wrapped_text(width=30)
    for line in wt:
        draw.text((margin, offset),line,font=font, fill=(0,0,0))
        offset += font.getsize(line)[1]
    return img

if __name__ == '__main__':
    folder = pathlib.Path("data/no_molecule")
    for i in range(10):
        img = Image.new('RGB', (256, 256), color=(255,255,255))
        margin = random.randint(1, 10)
        offset = random.randint(1, 10)
        create_image(img, margin=margin, offset=offset)
        filename = f"no_molecule_{i}.png"
        img.save(folder / filename)
