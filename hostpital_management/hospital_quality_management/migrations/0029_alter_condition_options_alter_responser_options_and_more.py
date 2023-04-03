# Generated by Django 4.1.7 on 2023-04-03 04:13

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hospital_quality_management', '0028_alter_responsercondition_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='condition',
            options={'verbose_name': 'Tiểu mục trong tiêu chí', 'verbose_name_plural': 'Tiểu mục trong tiêu chí'},
        ),
        migrations.AlterModelOptions(
            name='responser',
            options={'verbose_name': 'Người phụ trách tiêu chí', 'verbose_name_plural': 'Người phụ trách tiêu chí'},
        ),
        migrations.CreateModel(
            name='SelfAssessment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now_add=True, null=True)),
                ('date_updated', models.DateField(auto_now=True, null=True)),
                ('is_apply', models.BooleanField(default=False)),
                ('note', ckeditor.fields.RichTextField()),
                ('evaluation_criteria_level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital_quality_management.level', verbose_name='Mức tiêu chí')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Người đánh giá')),
            ],
        ),
    ]
