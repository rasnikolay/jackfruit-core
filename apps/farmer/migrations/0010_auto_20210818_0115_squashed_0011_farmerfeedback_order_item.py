# Generated by Django 3.1.7 on 2021-08-18 20:59

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0009_auto_20210817_2111'),
    ]

    operations = [
        migrations.CreateModel(
            name='FarmerFeedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_creation', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Изменен')),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='Оценка')),
                ('feedback', models.CharField(blank=True, default='', max_length=2000, verbose_name='Отзыв')),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='farmer_feedback', to='farmer.farmerprofile')),
                ('order_item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='farmer_feedback', to='store.foodorderitem')),
            ],
            options={
                'verbose_name': 'Отзывы на фермера',
                'verbose_name_plural': 'Отзывы на фермеров',
            },
        ),
        migrations.DeleteModel(
            name='FarmerRating',
        ),
    ]
