from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import random
import os
from db_connect import DbConnect
import math

def color_converter(d3_hex):
    print(d3_hex)
    if d3_hex is None:
        return (0,0,0)
    else:
        d6_hex=""
        for color in d3_hex:
            if color >9:
                d6_hex+=chr(color+87)*2
            else:
                d6_hex+=str(color)*2
        print(d6_hex)
        return tuple(int(d6_hex[i:i+2], 16) for i in (0, 2, 4))

def color_mixer(d3_hex):
    print(d3_hex)
    if None in d3_hex:
        return [0,0,0]
    else:
        return [int(round(sum(list(map(lambda mix: int(mix,16),color)))/len(color))) for color in list(map(list, zip(*d3_hex)))]

x_blacklist=[]
y_blacklist=[]

def target(img,size): 
    x=random.randint(0, (img.size[0] - size[0]))
    y=random.randint(0, (img.size[1] - size[1]))
    x_collision=(list(range(x,x+size[0])) and x_blacklist) != []
    y_collision=(list(range(y,y+size[1])) and y_blacklist) != []
    print(x_collision)
    print(y_collision)
    if x_collision and y_collision:
        target(img,size)
    else:
        return [x,y]

def draw_image(data):
    # init
    img = Image.new("RGB", (400, 400), (0, 0, 0))
    draw = ImageDraw.Draw(img)

    random_font = "fonts/" + random.choice(os.listdir("fonts"))
    for i in range(len(data)):
        print(data[i])
        text_options = {'fill': color_converter(color_mixer(data[i][1]))}
        fontsize = round(data[i][0])
        font = ImageFont.truetype(random_font, fontsize)
        string = data[i][2]
        drawer = ImageDraw.Draw(img)
        size = drawer.textsize(string, font=font)
        x=target(img,size)[0]
        y=target(img,size)[1]
        x_blacklist.append(x)
        y_blacklist.append(y)
        draw.text((x, y), string, font= font, **text_options)
        img.save('kep.png')
