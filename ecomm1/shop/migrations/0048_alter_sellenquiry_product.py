# Generated by Django 4.1.7 on 2023-04-24 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0047_remove_sellenquiry_dropdown_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellenquiry',
            name='product',
            field=models.CharField(default='', max_length=50),
        ),
    ]