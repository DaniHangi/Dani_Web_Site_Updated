# Generated by Django 5.0.6 on 2024-05-18 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twomodels', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='developer',
            name='profile_picture_url',
        ),
    ]