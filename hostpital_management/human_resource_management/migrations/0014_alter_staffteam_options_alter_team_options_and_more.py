# Generated by Django 4.1.7 on 2023-05-18 00:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('human_resource_management', '0013_team_staffteam'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='staffteam',
            options={'verbose_name': 'thành viên nhóm', 'verbose_name_plural': 'thành viên nhóm'},
        ),
        migrations.AlterModelOptions(
            name='team',
            options={'verbose_name': 'nhóm', 'verbose_name_plural': 'nhóm'},
        ),
        migrations.AlterField(
            model_name='staffteam',
            name='team',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='human_resource_management.team', verbose_name='nhóm'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='staffteam',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='nhân viên'),
            preserve_default=False,
        ),
    ]
