# Generated by Django 3.2.6 on 2021-10-28 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0005_alter_buyerbalance_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyerbalance',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Комментарий к заказу'),
        ),
    ]
