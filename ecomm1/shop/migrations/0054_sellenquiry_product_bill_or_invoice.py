# Generated by Django 4.1.7 on 2023-04-25 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0053_alter_sellenquiry_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='sellenquiry',
            name='product_Bill_or_invoice',
            field=models.FileField(default='', upload_to='shop/sellenquiryimages'),
        ),
    ]