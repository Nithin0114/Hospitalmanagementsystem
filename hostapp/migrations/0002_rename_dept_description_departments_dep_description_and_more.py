# Generated by Django 4.2 on 2023-06-01 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hostapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='departments',
            old_name='dept_description',
            new_name='dep_description',
        ),
        migrations.RenameField(
            model_name='departments',
            old_name='dept_name',
            new_name='dep_name',
        ),
    ]
