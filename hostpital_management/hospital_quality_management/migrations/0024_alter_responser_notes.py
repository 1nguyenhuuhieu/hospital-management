# Generated by Django 4.1.7 on 2023-04-02 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_quality_management', '0023_responser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='responser',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]