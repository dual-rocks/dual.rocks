from datetime import datetime
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.urls import reverse
from dual_rocks.authentication.models import User


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

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
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

    def __str__(self):
        return '{} profile'.format(self.user)

    def get_absolute_url(self):
        return reverse('web:profile', kwargs={'at': self.user.at})
