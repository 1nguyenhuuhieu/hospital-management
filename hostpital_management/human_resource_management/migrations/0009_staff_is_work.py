# Generated by Django 4.1.7 on 2023-05-17 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('human_resource_management', '0008_staff_birth_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='is_work',
            field=models.BooleanField(default=True, verbose_name='trạng thái làm việc'),
        ),
    ]
