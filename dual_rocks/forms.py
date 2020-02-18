import json
from PIL import Image
from io import BytesIO


def crop_image_from_data(form, field, crop_data_field):
    value = form.cleaned_data.get(field)
    if not value:
        return value
    try:
        crop_data = json.loads(form.data.get(crop_data_field, '{}'))
        x = crop_data.get('x')
        y = crop_data.get('y')
        width = crop_data.get('width')
        height = crop_data.get('height')
        if x is not None \
            and y is not None \
                and width is not None \
                and height is not None:
            image = Image.open(value.file).crop(
                (
                    x,
                    y,
                    x + width,
                    y + height
                )
            )
            fmt = value.image.format.lower()
            value.file = BytesIO()
            image.save(value.file, fmt)
        return value
    except json.JSONDecodeError:
        return value
