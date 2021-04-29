from PIL import ImageFont, ImageDraw, Image
from inky import InkyPHAT
from font_fredoka_one import FredokaOne
from math import floor


# inky phat = 212x104 - 2.0385
# inky what = 400x300 - 1.3333

inky_display = InkyPHAT("red")

input = ("Music Consumption Group", "16:30 - 21:00", "presentation_space")

text = ""
i = 0
while i < len(input):
    text += input[i]
    if i < len(input) - 1:
        text += "\n"
    i += 1


def find_font_size(text, font, image, target_width_ratio):
    # this needs to be refactored because it appears that having multiline text gums up the works...
    # perhaps test longest string against 1/3 of display height? we want each line to be its own thing
    # determine font size based on maximum width?
    tested_font_size = 100
    tested_font = ImageFont.truetype(font, tested_font_size)
    observed_width, observed_height = get_text_size(text, image, tested_font)
    estimated_font_size = (
        tested_font_size / (observed_width / image.width) * target_width_ratio
    )
    return floor(estimated_font_size) - 2


def get_text_size(text, image, font):
    im = Image.new("RGB", (image.width, image.height))
    draw = ImageDraw.Draw(im)
    return draw.textsize(text, font)


def get_text_image(text, text_size, image):
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(FredokaOne, text_size)
    print(text)
    draw.multiline_text((0, 0), text, font=font, fill=(0, 0, 0))
    return image


img = Image.new("RGB", (inky_display.WIDTH, inky_display.HEIGHT), (255, 255, 255))


targeted_width_ratio = inky_display.WIDTH / inky_display.HEIGHT

font_size = find_font_size(text, FredokaOne, img, targeted_width_ratio)

img = get_text_image(text, font_size, img)

img.show()
