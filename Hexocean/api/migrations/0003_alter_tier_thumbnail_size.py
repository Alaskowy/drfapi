# Generated by Django 4.1.6 on 2023-02-14 19:42

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_image_image_alter_tier_thumbnail_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tier',
            name='thumbnail_size',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), help_text='Thumbnail sizes list', size=None),
        ),
    ]
