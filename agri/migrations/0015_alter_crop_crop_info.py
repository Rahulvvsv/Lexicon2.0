# Generated by Django 4.0 on 2021-12-18 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agri', '0014_alter_crop_crop_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crop',
            name='crop_info',
            field=models.TextField(max_length=3000),
        ),
    ]