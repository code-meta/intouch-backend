# Generated by Django 4.2.7 on 2023-12-08 18:42

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_postimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('like_counts', models.IntegerField(default=0)),
                ('dislike_counts', models.IntegerField(default=0)),
                ('text', models.TextField()),
                ('reply_counts', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('dislikes', models.ManyToManyField(blank=True, related_name='comment_dislikes', to='users.profile')),
                ('likes', models.ManyToManyField(blank=True, related_name='comment_likes', to='users.profile')),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='users.post')),
            ],
        ),
    ]