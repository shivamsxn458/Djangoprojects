# Generated by Django 4.1.7 on 2023-05-14 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0083_clothing_alter_sellenquiry_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellenquiry',
            name='size',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
