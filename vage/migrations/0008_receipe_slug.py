# Generated by Django 4.2.6 on 2023-11-22 09:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vage', '0007_alter_reportcard_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipe',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2023, 11, 22, 9, 52, 29, 117221, tzinfo=datetime.timezone.utc), unique=True),
            preserve_default=False,
        ),
    ]
