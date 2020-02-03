from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class ForbiddenValuesValidator:
    message = _('"%(value)s" é um valor proibido.')
    forbidden_values = None

    def __init__(self, forbidden_values=None, message=None):
        self.message = message or self.message
        assert forbidden_values
        self.forbidden_values = forbidden_values

    def __call__(self, value):
        if value in self.forbidden_values:
            raise ValidationError(
                self.message,
                params={'value': value}
            )
