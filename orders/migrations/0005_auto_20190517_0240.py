# Generated by Django 2.0 on 2019-05-16 21:10

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_deliveryaddress_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery_amount',
            field=models.DecimalField(decimal_places=2, default=100, max_digits=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('PL', 'Placed'), ('PK', 'Packed'), ('SH', 'Shipped')], default='PL', max_length=2),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_before',
            field=models.DateField(default=datetime.datetime(2019, 5, 21, 21, 10, 0, 716801, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_man',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='orders.DeliveryMan'),
        ),
    ]
