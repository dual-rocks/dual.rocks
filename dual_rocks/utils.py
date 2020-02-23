from PIL import (
    Image,
    ImageDraw,
    ImageFont,
    ImageFilter
)

WATERMARK_TEXT_FONT = ImageFont.truetype('./fonts/coolvetica.ttf', 14)
WATERMARK_FONT = ImageFont.truetype('./fonts/coolvetica.ttf', 12)
SPACING = 15


def apply_watermark(image, text):
    text = text.upper()
    out = image.convert('RGBA')
    watermark = Image.new('RGBA', out.size, (255, 255, 255, 0))

    stamp = Image.new('RGBA', out.size, (255, 255, 255, 0))
    drawer = ImageDraw.Draw(stamp)
    drawer.text(
        (SPACING + 1, SPACING + 1),
        text,
        font=WATERMARK_TEXT_FONT,
        fill=(0, 0, 0, 75)
    )
    drawer.text(
        (SPACING - 1, SPACING - 1),
        text,
        font=WATERMARK_TEXT_FONT,
        fill=(255, 255, 255, 150)
    )
    text_w, text_h = drawer.textsize(text, font=WATERMARK_TEXT_FONT)
    stamp = stamp.crop(
        (
            0,
            0,
            text_w + SPACING * 2,
            text_h + SPACING * 2,
        )
    ).rotate(10, expand=True, resample=Image.BICUBIC)
    drawer = ImageDraw.Draw(stamp)
    drawer.text(
        (7, 7),
        'dual.rocks',
        font=WATERMARK_FONT,
        fill=(0, 0, 0, 75)
    )
    drawer.text(
        (5, 5),
        'dual.rocks',
        font=WATERMARK_FONT,
        fill=(255, 255, 255, 150)
    )

    out_w, out_h = out.size
    stamp_w, stamp_h = stamp.size

    for j in range((out_h // stamp_h) + 1):
        for i in range((out_w // stamp_w) + 1):
            watermark.paste(stamp, (i * stamp_w, j * stamp_h))

    out.alpha_composite(watermark)
    out = out.convert('RGB')
    return out


def apply_blur(image):
    return image.filter(ImageFilter.GaussianBlur(20))
