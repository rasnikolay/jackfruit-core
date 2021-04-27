# Generated by Django 3.1.7 on 2021-04-26 14:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_creation', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Изменен')),
                ('photo', models.ImageField(blank=True, max_length=255, upload_to='profile_photos', verbose_name='Фото')),
                ('phone', models.CharField(max_length=255, verbose_name='Телефон')),
                ('region', models.CharField(max_length=255, verbose_name='Регион')),
                ('tg_name', models.CharField(max_length=255, verbose_name='Имя в Telegram')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
