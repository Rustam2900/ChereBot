# Generated by Django 5.0.6 on 2024-07-01 05:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_botcompany_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='botcompany',
            name='language',
        ),
        migrations.RemoveField(
            model_name='botuser',
            name='language',
        ),
    ]