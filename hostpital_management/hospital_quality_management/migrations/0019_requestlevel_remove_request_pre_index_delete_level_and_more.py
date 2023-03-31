# Generated by Django 4.1.7 on 2023-03-31 04:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_quality_management', '0018_alter_chapter_index_alter_evaluationcriteria_index_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField(choices=[(1, 'Mức 1'), (2, 'Mức 2'), (3, 'Mức 3'), (4, 'Mức 4'), (5, 'Mức 5')], verbose_name='Mức độ đánh giá')),
                ('index', models.IntegerField(verbose_name='Số yêu cầu')),
                ('title', models.TextField(verbose_name='Nội dung')),
                ('pre_index', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital_quality_management.evaluationcriteria', verbose_name='Tiêu chí')),
            ],
            options={
                'verbose_name': 'Bậc thang chất lượng',
                'verbose_name_plural': 'Bậc thang chất lượng',
            },
        ),
        migrations.RemoveField(
            model_name='request',
            name='pre_index',
        ),
        migrations.DeleteModel(
            name='Level',
        ),
        migrations.DeleteModel(
            name='Request',
        ),
    ]
