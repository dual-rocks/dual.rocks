from datetime import datetime
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.urls import reverse
from django.core import validators
from django.contrib.staticfiles.storage import staticfiles_storage
from easy_thumbnails.files import get_thumbnailer
from dual_rocks.authentication.models import User
from dual_rocks.validators import ForbiddenValuesValidator
from dual_rocks.privacy.models import ImageWithPrivacy


class Profile(models.Model):
    YEAR_OF_BIRTH_CHOICES = map(
        lambda year: (year, str(year)),
        range(1900, datetime.today().year - 17)
    )

    MONTH_OF_BIRTH_CHOICES = map(
        lambda month: (month, '{0:02d}'.format(month)),
        range(1, 13)
    )

    PRONOUN_HE = 'H'
    PRONOUN_SHE = 'S'
    PRONOUN_HE_SHE = 'HS'
    PRONOUN_HE_HE = 'HH'
    PRONOUN_SHE_SHE = 'SS'
    PRONOUN_POLYAMORY = 'P'

    PRONOUN_CHOICES = [
        (PRONOUN_HE, _('ele')),
        (PRONOUN_SHE, _('ela')),
        (PRONOUN_HE_SHE, _('casal (ele e ela)')),
        (PRONOUN_HE_HE, _('casal (ele e ele)')),
        (PRONOUN_SHE_SHE, _('casal (ela e ela)')),
        (PRONOUN_POLYAMORY, _('nós (poliamor)')),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='profiles'
    )
    at = models.CharField(
        _('@'),
        unique=True,
        validators=[
            validators.RegexValidator(
                r'^[\w\.\_\-]{3,16}$',
                _('Utilize apenas letras (A-Z), . (ponto), _ (underline) e/ou '
                  '- (hífen). Com no mínimo 3 caracteres e no máximo 16.')
            ),
            ForbiddenValuesValidator(
                [
                    'admin',
                    'login',
                    'logout',
                    'register',
                    'profiles',
                    'chat',
                ],
                _('Você não pode usar "%(value)s" como @.')
            ),
        ],
        max_length=16
    )
    name = models.CharField(
        _('nome'),
        max_length=32
    )
    pronoun = models.CharField(
        _('pronome'),
        max_length=2,
        choices=PRONOUN_CHOICES
    )
    year_of_birth = models.PositiveSmallIntegerField(
        _('ano de nascimento'),
        choices=YEAR_OF_BIRTH_CHOICES,
        blank=True,
        null=True
    )
    month_of_birth = models.PositiveSmallIntegerField(
        _('mês de nascimento'),
        choices=MONTH_OF_BIRTH_CHOICES,
        blank=True,
        null=True
    )
    picture = models.ImageField(
        _('foto'),
        blank=True,
        null=True
    )
    status = models.CharField(
        _('status'),
        max_length=64,
        blank=True,
        null=False
    )
    bio = models.TextField(
        _('bio'),
        blank=True
    )

    def __str__(self):
        return '{} profile / {}'.format(self.at, self.user)

    def get_absolute_url(self):
        return reverse('web:profile:view', kwargs={'at': self.at})

    @property
    def picture_url(self):
        return self.get_picture_url()

    @property
    def chat_room_group_name(self):
        return f'chat_profile_{self.id}'

    def get_picture_url(self, user=None):
        if not self.picture:
            return staticfiles_storage.url('profile/no-avatar.jpg')
        image_with_privacy = ImageWithPrivacy.get_or_create(
            user,
            self,
            'picture'
        )
        return get_thumbnailer(
            image_with_privacy.processed_image
        )['profile_picture'].url

    @property
    def messages(self):
        from dual_rocks.chat.models import Message

        return Message.objects.filter(
            models.Q(from_profile=self) |
            models.Q(to_profile=self)
        )


class Photo(models.Model):
    class Meta:
        ordering = ['-published_at']

    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='photos'
    )
    image = models.ImageField(_('imagem'))
    published_at = models.DateTimeField(
        _('publicado em'),
        auto_now=True,
        editable=False
    )

    def __str__(self):
        return 'Photo #{} / {}'.format(self.id, self.profile)

    def get_absolute_url(self):
        return reverse('web:profile:view', kwargs={'at': self.profile.at})
