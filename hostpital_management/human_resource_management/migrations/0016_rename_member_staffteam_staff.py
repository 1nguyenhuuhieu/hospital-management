# Generated by Django 4.1.7 on 2023-05-18 01:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('human_resource_management', '0015_remove_staffteam_user_staffteam_member'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staffteam',
            old_name='member',
            new_name='staff',
        ),
    ]
