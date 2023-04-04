# Generated by Django 4.1.7 on 2023-04-04 01:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hospital_quality_management', '0038_alter_selfassessment_note'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proof',
            name='files',
        ),
        migrations.AddField(
            model_name='proof',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='proofs/files/', verbose_name='file đính kèm'),
        ),
        migrations.RemoveField(
            model_name='proof',
            name='images',
        ),
        migrations.AlterField(
            model_name='proof',
            name='notes',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='ghi chú'),
        ),
        migrations.AlterField(
            model_name='responser',
            name='notes',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='ghi chú'),
        ),
        migrations.AlterField(
            model_name='responsercondition',
            name='notes',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='ghi chú'),
        ),
        migrations.AlterField(
            model_name='responsercondition',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='người phụ trách'),
        ),
        migrations.AddField(
            model_name='proof',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='proofs/images/', verbose_name='ảnh đính kèm'),
        ),
    ]
