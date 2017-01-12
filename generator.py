text_content="database_data"

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import random
import os

dummy_data = [(12, (123, 156, 2), "kutya"), (10, (12, 234, 243), "macska"), (34, (12, 0, 243), "majom"), (56, (123, 80, 243), "tigris"), (22, (123, 0, 43), "teve")]


def draw_image(data):
    # init
    img = Image.new("RGB", (400, 400), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    draw = ImageDraw.Draw(img)

    random_font = "fonts/" + random.choice(os.listdir("fonts"))

    for i in range(len(data)):
        text_options = {'fill': (data[i][1][0], data[i][1][1], data[i][1][2])}
        size = data[i][0]
        font = ImageFont.truetype(random_font, size)
        string = data[i][2]
        x = random.randint(10, 390)
        y = random.randint(10, 390)
        drawer = ImageDraw.Draw(img)
        size = drawer.textsize(string, font=font)
        x = random.randint(0, (img.size[0] - text.size[0]))
        y = random.randint(0, (img.size[1] - text.size[1]))

        draw.text((x, y), string, font= font, **text_options)

        img.save('kep.png')

draw_image(dummy_data)

def color_converter(d3_hex):
    if d3_hex is None:
        return (0,0,0)
    else:
        d6_hex = list(d3_hex)[1] * 2 + list(d3_hex)[2] * 2 + list(d3_hex)[3] * 2
        return tuple(int(d6_hex[i:i + 2], 16) for i in (0, 2, 4))

