# Generated by Django 4.1.7 on 2023-04-24 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0042_rename_image1_sellenquiry_product_image1_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='sellenquiry',
            unique_together={('Contact_Number', 'Product_Selected', 'product_image1', 'product_image2', 'product_image3')},
        ),
    ]
