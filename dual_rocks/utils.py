from PIL import Image, ImageDraw, ImageFont

PIL_FONT = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 18)
SPACING = 10


def apply_watermark(image, text):
    out = image.convert('RGBA')
    watermark = Image.new('RGBA', out.size, (255, 255, 255, 0))

    stamp = Image.new('RGBA', out.size, (255, 255, 255, 0))
    drawer = ImageDraw.Draw(stamp)
    drawer.text(
        (SPACING, SPACING),
        text,
        font=PIL_FONT,
        fill=(255, 255, 255, 150)
    )
    text_w, text_h = drawer.textsize(text, font=PIL_FONT)
    stamp = stamp.crop(
        (
            0,
            0,
            text_w + SPACING * 2,
            text_h + SPACING * 2,
        )
    ).rotate(10, expand=True)

    out_w, out_h = out.size
    stamp_w, stamp_h = stamp.size

    for j in range((out_h // stamp_h) + 1):
        for i in range((out_w // stamp_w) + 1):
            watermark.paste(stamp, (i * stamp_w, j * stamp_h))

    out.alpha_composite(watermark)
    out = out.convert('RGB')
    return out
