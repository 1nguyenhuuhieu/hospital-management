# Generated by Django 4.1.7 on 2023-04-24 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('human_resource_management', '0001_initial'),
        ('news', '0005_remove_tag_parrent_tag_post_is_pinned_delete_slide'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='human_resource_management.staff', verbose_name='tác giả'),
        ),
    ]
