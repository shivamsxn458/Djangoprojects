# Generated by Django 4.1.7 on 2023-04-05 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_alter_product_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='url',
            field=models.URLField(blank=True, default=''),
        ),
    ]
