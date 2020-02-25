# Generated by Django 3.0.3 on 2020-02-25 05:09

import django.core.validators
from django.db import migrations, models
import dual_rocks.validators


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='at',
            field=models.CharField(max_length=16, unique=True, validators=[django.core.validators.RegexValidator('^[\\w\\.\\_\\-]{3,16}$', 'Utilize apenas letras (A-Z), . (ponto), _ (underline) e/ou - (hífen). Com no mínimo 3 caracteres e no máximo 16.'), dual_rocks.validators.ForbiddenValuesValidator(['admin', 'login', 'logout', 'register', 'profiles', 'chat'], 'Você não pode usar "%(value)s" como @.')], verbose_name='@'),
        ),
    ]