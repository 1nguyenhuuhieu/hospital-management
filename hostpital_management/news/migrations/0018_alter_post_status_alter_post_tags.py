# Generated by Django 4.1.7 on 2023-05-18 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0017_category_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(blank=True, choices=[('private', 'Chỉ mình tôi'), ('staff', 'Nhân viên'), ('public', 'Mọi người')], default='private', max_length=10, null=True, verbose_name='trạng thái bài viết'),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='news.tag', verbose_name='thẻ'),
        ),
    ]
