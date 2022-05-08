from inky import InkyPHAT, InkyWHAT
from PIL import Image, ImageDraw, ImageFont
from font_fredoka_one import FredokaOne


inky_palettes=  {'black': (255, 255, 255,
                           0, 0, 0,
                           255, 255, 255) + (0, 0, 0) * 254,
                 'red': (255, 255, 255,
                         0, 0, 0,
                         255, 0, 0,
                         255, 255, 255) + (0, 0, 0) * 253,
                 'yellow': (255, 255, 255,
                            0, 0, 0,
                            255, 255, 0,
                            255, 255, 255) + (0, 0, 0) * 253}


def get_default_font_size(inky_display):
    '''
    Hardcoded default font sizes, because rescaling is annoying with PIL!
    '''
    if inky_display.HEIGHT < 200: # smaller font for inky pHAT
        default_font_size = 20
    else:
        default_font_size = 36
    return default_font_size


def format_line(font, msg, inky_display):
    '''
    This splits a given line of text into multiple lines if necessary.
    Should be modified to truncate a given field (i.e. the event name) if too long
    to fit on two lines of the InkypHAT
    '''
    lines = []
    w, h = font.getsize(msg)
    if w <= inky_display.WIDTH:
        lines.append(msg)
    else:
        toks = msg.split()
        cur_line = ''
        for tok in toks:
            cur_w, _ = font.getsize(cur_line + tok + ' ')
            if cur_w <= inky_display.WIDTH:
                cur_line = cur_line + tok + ' '
            else:
                lines.append(cur_line)
                cur_line = tok + ' '
        lines.append(cur_line)
    return lines


def get_text_image(inky_display, full_text):
    '''
    This formats the font to be nicely centered
    with appropriate line breaks due to event properties
    '''
    fontsize = get_default_font_size(inky_display)
    font = ImageFont.truetype(FredokaOne, fontsize)
    lines = []
    for line in full_text:
        lines.extend(format_line(font, line, inky_display))
    _, line_height = font.getsize(lines[0])
    centered_y = (inky_display.HEIGHT / 2) - ((line_height * len(lines)) / 2)
    height_counter = centered_y
    img = Image.new("RGB", (inky_display.WIDTH, inky_display.HEIGHT), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    for i in range(0, len(lines)):
        msg = lines[i]
        w, h = font.getsize(msg)
        x = (inky_display.WIDTH / 2) - (w / 2)
        y = height_counter
        draw.text((x, y), msg, (0, 0, 0), font)
        height_counter += h
    return img


def rgb_to_inky(inky_display, img):
    '''
    To set an image to the limited inky palette, it needs to be transformed
    from RGB 
    '''
    pal_img = Image.new("P", (1, 1))
    colour = inky_display.colour
    pal_img.putpalette(inky_palettes[colour])
    img = img.convert("RGB").quantize(palette=pal_img)
    # rotate image if necessary due to power cord
    # img = img.rotate(180, expand=True)
    inky_display.set_image(img)
    inky_display.show()
