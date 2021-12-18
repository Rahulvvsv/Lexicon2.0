# Generated by Django 4.0 on 2021-12-18 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agri', '0016_remove_crop_arrivals_crop_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='crop',
            name='climate',
            field=models.TextField(default=1, max_length=2000),
        ),
        migrations.AddField(
            model_name='crop',
            name='soil_info',
            field=models.TextField(default=1, max_length=1000),
        ),
    ]