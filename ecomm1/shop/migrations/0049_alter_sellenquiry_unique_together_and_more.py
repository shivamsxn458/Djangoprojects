# Generated by Django 4.1.7 on 2023-04-24 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0048_alter_sellenquiry_product'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='sellenquiry',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='sellenquiry',
            name='Product_Selected',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterUniqueTogether(
            name='sellenquiry',
            unique_together={('Contact_Number', 'Product_Selected')},
        ),
        migrations.RemoveField(
            model_name='sellenquiry',
            name='product',
        ),
    ]