# Generated by Django 2.0 on 2019-05-18 19:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20190519_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_before',
            field=models.DateField(default=datetime.datetime(2019, 5, 23, 19, 25, 2, 784350, tzinfo=utc)),
        ),
    ]
