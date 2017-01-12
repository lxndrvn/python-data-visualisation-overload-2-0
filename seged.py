class Seged:

    #234 --> (34, 51, 68)
    def color_converter(d3_hex):
        if d3_hex is None:
            return (0,0,0)
        else:
            d6_hex = list(d3_hex)[1] * 2 + list(d3_hex)[2] * 2 + list(d3_hex)[3] * 2
            return tuple(int(d6_hex[i:i + 2], 16) for i in (0, 2, 4))

    print(color_converter('#234'))

def get_x(text_size):
    if text_size[0] >= img.size[0]:
        x = 0
    else:
        x = random.randint(0, (img.size[0]-text_size[0]))  # full width - horizontal size of text
    return x


# generating a y coordinate
def get_y(text_size):
    if text_size[1] >= img.size[1]:
        y = 0
    else:
        y = random.randint(0, (img.size[1] - text_size[1]))  # full width - horizontal size of text
    return y

