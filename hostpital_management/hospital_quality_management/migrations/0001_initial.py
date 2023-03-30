# Generated by Django 4.1.7 on 2023-03-30 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField(max_length=1)),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='EvaluationCriteria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField(max_length=1)),
                ('title', models.TextField()),
                ('legal_basis', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField(choices=[(1, 'Mức 1'), (2, 'Mức 2'), (3, 'Mức 3'), (4, 'Mức 4'), (5, 'Mức 5'), (6, 'Mức 6'), (7, 'Mức 7'), (8, 'Mức 8'), (9, 'Mức 9'), (10, 'Mức 10')])),
                ('title', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.CharField(max_length=1)),
                ('title', models.CharField(max_length=200)),
            ],
        ),
    ]
