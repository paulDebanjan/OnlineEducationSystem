# Generated by Django 4.0.3 on 2022-10-21 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizes', '0003_alter_result_quiz'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Result',
        ),
    ]