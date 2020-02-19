# Generated by Django 3.0.3 on 2020-02-19 01:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0003_profile_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='imagem')),
                ('published_at', models.DateTimeField(auto_now=True, verbose_name='publicado em')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='user_profile.Profile')),
            ],
        ),
    ]