# Generated by Django 4.1.7 on 2023-05-04 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0014_post_plaintext_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='cover',
            field=models.ImageField(blank=True, upload_to='covers/', verbose_name='ảnh bìa'),
        ),
    ]