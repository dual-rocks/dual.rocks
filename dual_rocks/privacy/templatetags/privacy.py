from django import template
from dual_rocks.privacy.models import ImageWithPrivacy


register = template.Library()


@register.simple_tag(takes_context=True)
def image_with_privacy(context, instance, field):
    return ImageWithPrivacy.get_or_create(
        context.request.user,
        instance,
        field
    )
