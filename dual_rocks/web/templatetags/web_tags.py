from django import template


register = template.Library()


@register.simple_tag(takes_context=True)
def get_picture_url(context, profile):
    return profile.get_picture_url(user=context.request.user)
