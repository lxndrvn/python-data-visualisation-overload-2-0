import psycopg2

try:
    conn = psycopg2.connect("dbname='szilniczky' user='szilniczky' host='localhost' password='Szeder93'")
except:
    print("I am unable to connect to the database")
cur = conn.cursor()
cur.execute("""SELECT name FROM base_data WHERE name='Y-find'""")
text_content=cur.fetchall()[0]

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

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
