from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth.base_user import (
    BaseUserManager,
    AbstractBaseUser,
)
from django.contrib.auth.models import PermissionsMixin
from django.core import validators
from django.urls import reverse


class UserManager(BaseUserManager):
    def create_user(self, password, **kwargs):
        user = self.model(**kwargs)
        user.set_password(password)
        return user.save()

    def create_superuser(self, password, **kwargs):
        return self.create_user(
            password,
            is_superuser=True,
            **kwargs
        )


class User(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'at'
    REQUIRED_FIELDS = [
        'email',
    ]

    at = models.CharField(
        _('@'),
        unique=True,
        validators=[
            validators.RegexValidator(
                r'^[\w\.\_\-]{3,16}$',
                _('Utilize apenas letras (A-Z), . (ponto), _ (underline) e/ou '
                  '- (hífen). Com no mínimo 3 caracteres e no máximo 16.')
            ),
        ],
        max_length=16
    )
    email = models.EmailField(
        _('e-mail'),
        unique=True
    )

    objects = UserManager()

    @property
    def is_staff(self): return self.is_superuser

    def get_absolute_url(self):
        return reverse('web:profile', kwargs={'at': self.at})
