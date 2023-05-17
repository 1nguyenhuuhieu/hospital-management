# Generated by Django 4.1.7 on 2023-05-17 01:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Họ và tên')),
                ('phone', models.IntegerField(blank=True, null=True, verbose_name='Số điện thoại')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars/', verbose_name='ảnh đại diện')),
                ('birth_of_date', models.DateField(blank=True, null=True, verbose_name='ngày sinh')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='tài khoản đăng nhập')),
            ],
            options={
                'verbose_name': 'thành viên',
                'verbose_name_plural': 'thành viên',
            },
        ),
    ]
