from PIL import ImageFont, ImageDraw, Image
from inky import InkyWHAT
from font_fredoka_one import FredokaOne
from math import floor


# inky phat = 212x104 - 2.0385
# inky what = 400x300 - 1.3333

inky_display = InkyWHAT("red")

input = ("Music Consumption Group", "16:30 - 21:00", "presentation_space")

text = ""
i = 0
while i < len(input):
    text += input[i]
    if i < len(input) - 1:
        text += "\\n"
    i += 1


def find_font_size(text, font, image, target_width_ratio):
    tested_font_size = 100
    tested_font = ImageFont.truetype(font, tested_font_size)
    observed_width, observed_height = get_text_size(text, image, tested_font)
    estimated_font_size = (
        tested_font_size / (observed_width / image.width) * target_width_ratio
    )
    return floor(estimated_font_size)


def get_text_size(text, image, font):
    im = Image.new("RGB", (image.width, image.height))
    draw = ImageDraw.Draw(im)
    return draw.textsize(text, font)


img = Image.new("RGB", (inky_display.WIDTH, inky_display.HEIGHT), (255, 255, 255))

targeted_width_ratio = inky_display.WIDTH / inky_display.HEIGHT

print(find_font_size(text, FredokaOne, img, targeted_width_ratio))
