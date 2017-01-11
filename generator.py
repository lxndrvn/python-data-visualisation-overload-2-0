text_content="database_data"

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import random
import os


def draw_image(data):
    # init
    img = Image.new("RGB", (400, 400), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    draw = ImageDraw.Draw(img)

    random_font = "fonts/" + random.choice(os.listdir("fonts"))

    for i in range(len(data)):
        text_options = {'fill': (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))}
        random_size = random.randint(20, 60)
        font = ImageFont.truetype(random_font, random_size)
        x = random.randint(10, 370)
        y = random.randint(10, 370)
        draw.text((x, y), data[i][2], font= font, **text_options)
        img.save('sample2.png')

        rotate_rates = [0, 90, 180, 270]
        for rotate_rate in rotate_rates:
            for text in text.data:
                picture = text.place(picture, rotate_rate)

draw_image(real_data)