# Generated by Django 3.2.6 on 2021-10-29 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_rootproduct_category'),
        ('buyer', '0006_buyerbalance_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyerbalance',
            name='order',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='buyer_balance', to='store.foodorder', verbose_name='Заказ'),
        ),
    ]
