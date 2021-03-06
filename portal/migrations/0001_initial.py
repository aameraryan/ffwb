# Generated by Django 2.0 on 2019-05-02 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('abbrevation', models.CharField(max_length=8)),
                ('details', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PhotoPosition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('abbrevation', models.CharField(max_length=8)),
                ('details', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('headline', models.CharField(max_length=32)),
                ('details', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('actual_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('preference', models.IntegerField(default=10)),
                ('colors', models.ManyToManyField(to='portal.Color')),
            ],
        ),
        migrations.CreateModel(
            name='ProductPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='products/product_photos/')),
                ('preference', models.PositiveIntegerField(default=10)),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='portal.Color')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='portal.PhotoPosition')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='portal.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('abbrevation', models.CharField(max_length=8)),
                ('length', models.CharField(max_length=16)),
                ('unit', models.CharField(max_length=16)),
                ('details', models.TextField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='sizes',
            field=models.ManyToManyField(to='portal.Size'),
        ),
    ]
