# Generated by Django 4.0.3 on 2022-06-18 05:26

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpostmodel',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True, verbose_name='Post Address'),
        ),
    ]
