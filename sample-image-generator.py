from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


dummy_data = [(12, 23432, "kutya"), (10, 22, "macska"), (34, 2343342, "nyúl"), (56, 4323, "béka"), (22, 2342, "teve")]

img = Image.new("RGB", (512, 512), "red")
draw = ImageDraw.Draw(img)
# font = ImageFont.truetype(<font-file>, <font-size>)
# font = ImageFont.truetype("sans-serif.ttf", 16)
text_options = {'fill': (255, 255, 255)}
text_size = draw.textsize(text_content)
# draw.text((x, y),text_content,(r,g,b))
draw.text((0, 0), text_content, **text_options)
draw.text((0, text_size[1]), text_content, **text_options)
draw.text((text_size[0], 0), text_content, **text_options)
draw.text(text_size, text_content, **text_options)
img.save('sample-out.png')
