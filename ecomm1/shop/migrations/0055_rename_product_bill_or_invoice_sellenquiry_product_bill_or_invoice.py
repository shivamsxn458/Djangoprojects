# Generated by Django 4.1.7 on 2023-04-25 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0054_sellenquiry_product_bill_or_invoice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sellenquiry',
            old_name='product_Bill_or_invoice',
            new_name='product_Bill_or_Invoice',
        ),
    ]