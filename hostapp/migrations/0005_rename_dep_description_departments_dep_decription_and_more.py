# Generated by Django 4.2 on 2023-06-05 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostapp', '0004_booking'),
    ]

    operations = [
        migrations.RenameField(
            model_name='departments',
            old_name='dep_description',
            new_name='dep_decription',
        ),
        migrations.AlterField(
            model_name='booking',
            name='p_phone',
            field=models.CharField(max_length=10),
        ),
    ]
