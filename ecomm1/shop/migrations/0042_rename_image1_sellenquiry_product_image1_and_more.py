# Generated by Django 4.1.7 on 2023-04-24 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0041_sellenquiry_image1_sellenquiry_image2_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sellenquiry',
            old_name='image1',
            new_name='product_image1',
        ),
        migrations.RenameField(
            model_name='sellenquiry',
            old_name='image2',
            new_name='product_image2',
        ),
        migrations.RenameField(
            model_name='sellenquiry',
            old_name='image3',
            new_name='product_image3',
        ),
        migrations.RenameField(
            model_name='sellenquiry',
            old_name='price',
            new_name='your_ask_price',
        ),
    ]
