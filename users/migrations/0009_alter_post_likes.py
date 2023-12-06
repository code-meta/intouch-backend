# Generated by Django 4.2.7 on 2023-12-04 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_post_likes_post_likes_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes', to='users.profile'),
        ),
    ]