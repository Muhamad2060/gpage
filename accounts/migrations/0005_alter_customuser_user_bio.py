# Generated by Django 4.2.6 on 2023-11-29 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_rename_user_profile_customuser_user_profile_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_bio',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
