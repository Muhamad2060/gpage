# Generated by Django 4.2.6 on 2023-10-23 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
    ]