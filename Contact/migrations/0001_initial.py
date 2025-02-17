# Generated by Django 5.1.4 on 2024-12-31 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SocialInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=1000, null=True)),
                ('description', models.TextField(blank=True, max_length=5000, null=True)),
                ('github', models.URLField(blank=True, help_text='Your GitHub profile link', max_length=300, null=True)),
                ('twitter', models.URLField(blank=True, help_text='Your Twitter profile link', max_length=300, null=True)),
                ('linkedin', models.URLField(blank=True, help_text='Your LinkedIn profile link', max_length=300, null=True)),
                ('phone_number', models.CharField(blank=True, help_text='Your phone number', max_length=15, null=True)),
                ('email', models.EmailField(blank=True, help_text='Your email address', max_length=100, null=True)),
                ('address', models.TextField(blank=True, help_text='Your address', null=True)),
            ],
        ),
    ]
