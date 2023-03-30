# Generated by Django 4.1.7 on 2023-03-30 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_quality_management', '0007_evaluationcriteria_legal_basis'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('file', models.FileField(upload_to='doccument/')),
            ],
        ),
        migrations.AddField(
            model_name='evaluationcriteria',
            name='files',
            field=models.ManyToManyField(to='hospital_quality_management.file'),
        ),
    ]