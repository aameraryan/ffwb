# Generated by Django 2.0 on 2019-05-21 17:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_auto_20190521_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_before',
            field=models.DateField(default=datetime.datetime(2019, 5, 26, 17, 45, 4, 833646, tzinfo=utc)),
        ),
    ]
