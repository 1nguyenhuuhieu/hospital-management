# Generated by Django 4.1.7 on 2023-06-13 03:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_quality_management', '0002_hqmdashboard'),
    ]

    operations = [
        migrations.AddField(
            model_name='hqmdashboard',
            name='manager_ec',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='manager_ec', to='hospital_quality_management.hqmmember', verbose_name='người chịu trách nhiệm thực hiện'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hqmdashboard',
            name='member_ec',
            field=models.ManyToManyField(related_name='member_ec', to='hospital_quality_management.hqmmember', verbose_name='người phối hợp'),
        ),
        migrations.AddField(
            model_name='hqmdashboard',
            name='viewer_ec',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='viewer_ec', to='hospital_quality_management.hqmmember', verbose_name='người giám sát'),
            preserve_default=False,
        ),
    ]
