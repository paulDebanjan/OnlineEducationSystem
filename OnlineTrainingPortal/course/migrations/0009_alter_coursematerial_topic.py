# Generated by Django 4.0.3 on 2022-10-28 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0008_alter_coursematerial_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursematerial',
            name='topic',
            field=models.CharField(choices=[('slide', 'Slide'), ('pdf', 'PDF'), ('video', 'Video'), ('quiz', 'Quiz')], default=None, max_length=12, verbose_name='Material Kind'),
        ),
    ]