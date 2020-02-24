from django import template
from dual_rocks.user_profile.models import UserViewPhoto


register = template.Library()


@register.simple_tag(takes_context=True)
def get_user_view_photo(context, photo):
    return UserViewPhoto.get_or_create(context.request.user, photo)


@register.simple_tag(takes_context=True)
def get_picture_url(context, profile):
    return profile.get_picture_url(user=context.request.user)
