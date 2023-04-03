# Generated by Django 4.1.7 on 2023-04-03 14:43

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_quality_management', '0033_image_alter_chapter_options_alter_condition_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selfassessment',
            name='evaluation_criteria',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='hospital_quality_management.evaluationcriteria', verbose_name='tiêu chí'),
        ),
        migrations.AlterField(
            model_name='selfassessment',
            name='note',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Ghi chú'),
        ),
    ]
