# Generated by Django 4.1.7 on 2023-05-17 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('human_resource_management', '0009_staff_is_work'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='sex',
            field=models.CharField(blank=True, choices=[('m', 'Nam'), ('f', 'Nữ')], max_length=1, null=True),
        ),
    ]