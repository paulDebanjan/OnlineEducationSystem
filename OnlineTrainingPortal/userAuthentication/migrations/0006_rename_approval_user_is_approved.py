# Generated by Django 4.0.3 on 2022-06-12 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userAuthentication', '0005_user_approval'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='approval',
            new_name='is_approved',
        ),
    ]