# Generated by Django 2.0 on 2019-05-18 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='current_ocassion',
            field=models.BooleanField(default=False),
        ),
    ]
