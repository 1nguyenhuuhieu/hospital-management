# Generated by Django 4.1.7 on 2023-04-04 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_quality_management', '0049_selfassessmentcondition'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='selfassessmentcondition',
            options={'verbose_name': 'tự đánh giá', 'verbose_name_plural': 'tự đánh giá'},
        ),
        migrations.RenameField(
            model_name='proof',
            old_name='user',
            new_name='staff',
        ),
        migrations.RemoveField(
            model_name='proof',
            name='condition',
        ),
        migrations.RemoveField(
            model_name='proof',
            name='is_pass',
        ),
        migrations.AddField(
            model_name='proof',
            name='selfassessment_condition',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hospital_quality_management.selfassessmentcondition', verbose_name='tiểu mục'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='selfassessmentcondition',
            name='proofs',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hospital_quality_management.proof', verbose_name='bằng chứng đánh giá'),
        ),
    ]
