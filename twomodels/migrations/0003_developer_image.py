# Generated by Django 5.0.6 on 2024-05-18 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twomodels', '0002_remove_developer_profile_picture_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='developer',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='dev_images'),
        ),
    ]
