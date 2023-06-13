# Generated by Django 4.1.7 on 2023-06-13 03:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_quality_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HQMDashboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('previous_result', models.IntegerField(choices=[(1, 'Mức 1'), (2, 'Mức 2'), (3, 'Mức 3'), (4, 'Mức 4'), (5, 'Mức 5')], verbose_name='kết quả năm trước')),
                ('next_result', models.IntegerField(choices=[(1, 'Mức 1'), (2, 'Mức 2'), (3, 'Mức 3'), (4, 'Mức 4'), (5, 'Mức 5')], verbose_name='mục tiêu năm nay')),
                ('notes', models.TextField(verbose_name='giải pháp cần thực hiện')),
                ('deadline', models.DateField(verbose_name='Thời gian hoàn thành dự kiến')),
                ('result', models.IntegerField(choices=[(1, 'Mức 1'), (2, 'Mức 2'), (3, 'Mức 3'), (4, 'Mức 4'), (5, 'Mức 5')], verbose_name='kết quả')),
                ('evaluation_criteria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital_quality_management.evaluationcriteria', verbose_name='tiêu chí')),
            ],
        ),
    ]
