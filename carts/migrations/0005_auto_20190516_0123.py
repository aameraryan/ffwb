# Generated by Django 2.0 on 2019-05-15 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0004_auto_20190510_1952'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='order',
            name='delivery_address',
        ),
        migrations.RemoveField(
            model_name='order',
            name='delivery_man',
        ),
        migrations.DeleteModel(
            name='DeliveryAddress',
        ),
        migrations.DeleteModel(
            name='DeliveryMan',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
