# Generated by Django 5.0.6 on 2024-05-20 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twomodels', '0004_delete_contactrequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='developer',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='dani_site/dev_images/'),
        ),
    ]
