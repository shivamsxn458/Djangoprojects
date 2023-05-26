# Generated by Django 4.1.7 on 2023-05-14 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0082_remove_sellenquiry_chest_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clothing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('XS', 'Extra Small'), ('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra Large')], max_length=2)),
            ],
        ),
        migrations.AlterField(
            model_name='sellenquiry',
            name='size',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='shop.clothing'),
        ),
    ]
