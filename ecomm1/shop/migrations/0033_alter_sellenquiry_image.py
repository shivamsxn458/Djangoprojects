# Generated by Django 4.1.7 on 2023-04-22 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0032_alter_sellenquiry_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellenquiry',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to='shop/sellenquiryimages'),
        ),
    ]
