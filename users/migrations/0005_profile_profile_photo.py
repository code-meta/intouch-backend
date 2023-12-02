# Generated by Django 4.2.7 on 2023-12-02 17:47

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_profile_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_photo',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='profile_photo'),
        ),
    ]