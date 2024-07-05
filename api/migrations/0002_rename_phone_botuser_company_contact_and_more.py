# Generated by Django 5.0.6 on 2024-06-30 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='botuser',
            old_name='phone',
            new_name='company_contact',
        ),
        migrations.RenameField(
            model_name='botuser',
            old_name='name',
            new_name='company_employee_name',
        ),
        migrations.AddField(
            model_name='botuser',
            name='company_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='botuser',
            name='employee_number',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='botuser',
            name='lifetime',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='botuser',
            name='language',
            field=models.CharField(choices=[('uz', 'Uzbek'), ('ru', 'Russian')], default='uz', max_length=2),
        ),
    ]
