# Generated by Django 4.1.7 on 2023-05-17 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('human_resource_management', '0007_rename_staffdetail_department_remove_staff_avatar_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='birth_date',
            field=models.DateField(blank=True, null=True, verbose_name='ngày sinh'),
        ),
    ]
