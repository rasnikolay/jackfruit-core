# Generated by Django 3.1.4 on 2021-02-18 22:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodDelivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_creation', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Изменен')),
                ('date', models.DateTimeField(verbose_name='Дата и время поставки')),
                ('is_urgently_deactivated', models.BooleanField(default=False, verbose_name='Срочно выключить')),
                ('state', models.CharField(choices=[('collecting', 'Сбор заявок'), ('processing', 'Обработка заявок'), ('processing', 'Обработка заявок'), ('finished', 'Заказы доставлены'), ('suspended', 'Сбор заявок приостановлен'), ('cancelled', 'Отменена')], default='collecting', max_length=80, verbose_name='Статус доставки')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_creation', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Изменен')),
                ('location_type', models.CharField(choices=[('private', 'частный'), ('office', 'офис')], default='private', max_length=10, verbose_name='Тип адреса')),
                ('name', models.CharField(max_length=200, verbose_name='Имя')),
                ('phone', models.CharField(max_length=15, verbose_name='Телефон')),
                ('office_name', models.TextField(blank=True, default='', max_length=8, verbose_name='Короткое название офиса')),
                ('city_type', models.CharField(choices=[('city', 'город'), ('settlement', 'поселок'), ('village', 'деревня')], default='city', max_length=100, verbose_name='Тип населенного пункта')),
                ('city_value', models.CharField(default='Минск', max_length=200, verbose_name='Населенный пункт')),
                ('city_district', models.CharField(blank=True, choices=[('angarskaya', 'Ангарская'), ('zelonyy_lug', 'Зелёный Луг')], default='', max_length=200, verbose_name='Микрорайон')),
                ('street_type', models.CharField(choices=[('street', 'улица'), ('proezd', 'проезд'), ('avenue', 'проспект'), ('square', 'площадь'), ('side_street', 'переулок'), ('other', 'другое')], default='street', max_length=40, verbose_name='Тип участка города')),
                ('street_value', models.CharField(max_length=300, verbose_name='Название улицы/площади/проезда')),
                ('building', models.CharField(max_length=15, verbose_name='Дом/Строение (с корпусом)')),
                ('porch', models.CharField(blank=True, default='', max_length=15, verbose_name='Подъезд')),
                ('floor', models.CharField(blank=True, default='', max_length=5, verbose_name='Этаж')),
                ('room', models.CharField(blank=True, default='', max_length=10, verbose_name='Помещение/квартира')),
                ('sort_key', models.PositiveIntegerField(default=0, verbose_name='Сортировка')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FoodProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_creation', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Изменен')),
                ('name', models.CharField(max_length=250, verbose_name='Название продукта')),
                ('quantity_per_price', models.CharField(choices=[('kg', 'кг'), ('gm', 'гр.'), ('100gm', '100 гр.'), ('pс', 'шт.'), ('L.', 'л')], default='kg', max_length=20, verbose_name='Количество за указанную цену')),
                ('min_weight', models.PositiveIntegerField(blank=True, null=True, verbose_name='Минимальная масса продукта (г.)')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Цена')),
                ('image', models.ImageField(blank=True, max_length=255, upload_to='products', verbose_name='Изображение продукта')),
                ('is_visible', models.BooleanField(default=True, verbose_name='Включен')),
                ('description', models.TextField(blank=True, verbose_name='Описание продукта')),
                ('packaging', models.TextField(choices=[('not_known', 'не известно'), ('no_packaging', 'без упаковки'), ('paper_bag', 'бумажный пакет')], default='не известно', max_length=20, verbose_name='Упаковка')),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Фермер')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
