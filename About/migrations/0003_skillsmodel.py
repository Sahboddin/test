# Generated by Django 5.1.4 on 2024-12-25 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('About', '0002_aboutmodel_background_img_aboutmodel_profile_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='SkillsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skillName', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
