# Generated by Django 4.1.7 on 2023-04-06 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_alter_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(default='', max_length=50),
        ),
    ]