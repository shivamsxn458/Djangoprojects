# Generated by Django 4.1.7 on 2023-05-18 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0086_alter_product_backimage_alter_product_sideimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='backimage',
            field=models.ImageField(blank=True, default='', upload_to='shop/images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sideimage',
            field=models.ImageField(blank=True, default='/media/bride1.jpeg', upload_to='shop/images'),
        ),
    ]
