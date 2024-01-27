# Generated by Django 4.1.7 on 2024-01-27 20:11

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0006_alter_pet_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
