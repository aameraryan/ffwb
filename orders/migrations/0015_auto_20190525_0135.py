# Generated by Django 2.0 on 2019-05-24 20:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0014_auto_20190521_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_before',
            field=models.DateField(default=datetime.datetime(2019, 5, 29, 20, 5, 27, 23259, tzinfo=utc)),
        ),
    ]
