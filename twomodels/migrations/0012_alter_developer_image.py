# Generated by Django 5.0.6 on 2024-05-23 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twomodels', '0011_alter_developer_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='developer',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='dev_images/'),
        ),
    ]
