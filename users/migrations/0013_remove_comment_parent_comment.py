# Generated by Django 4.2.7 on 2023-12-04 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='parent_comment',
        ),
    ]