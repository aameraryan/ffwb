# Generated by Django 2.0 on 2019-05-02 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0006_auto_20190503_0231'),
    ]

    operations = [
        migrations.AddField(
            model_name='color',
            name='hex_code',
            field=models.CharField(default='#FF0000', max_length=7),
        ),
    ]
