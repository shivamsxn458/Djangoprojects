# Generated by Django 4.1.7 on 2023-04-06 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_alter_product_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(blank=True, default='onesize', max_length=50),
        ),
    ]
