# Generated by Django 5.1.4 on 2024-12-25 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('About', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutmodel',
            name='background_img',
            field=models.ImageField(blank=True, null=True, upload_to='background/photos'),
        ),
        migrations.AddField(
            model_name='aboutmodel',
            name='profile_img',
            field=models.ImageField(blank=True, null=True, upload_to='profile/photos'),
        ),
    ]
