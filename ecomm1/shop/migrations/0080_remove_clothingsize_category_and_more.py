# Generated by Django 4.1.7 on 2023-05-11 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0079_alter_clothingsize_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clothingsize',
            name='category',
        ),
        migrations.RemoveField(
            model_name='clothingsize',
            name='size',
        ),
        migrations.AddField(
            model_name='clothingsize',
            name='chest',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='clothingsize',
            name='length',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='clothingsize',
            name='waist',
            field=models.CharField(default='', max_length=20),
        ),
    ]
