# Generated by Django 4.1.7 on 2023-05-04 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0070_rename_customer_purchaseenquiry'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseenquiry',
            name='Status',
            field=models.CharField(default='', max_length=20),
        ),
    ]