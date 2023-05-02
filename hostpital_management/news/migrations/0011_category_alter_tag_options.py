# Generated by Django 4.1.7 on 2023-04-30 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_remove_post_is_pinned_remove_post_is_public_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='tên danh mục')),
            ],
            options={
                'verbose_name': 'danh mục',
                'verbose_name_plural': 'danh mục',
            },
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'thẻ', 'verbose_name_plural': 'thẻ'},
        ),
    ]