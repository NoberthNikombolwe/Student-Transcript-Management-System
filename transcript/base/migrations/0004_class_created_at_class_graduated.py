# Generated by Django 5.0 on 2024-02-06 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_student_date_of_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='created_at',
            field=models.DateTimeField(default='2021-10-01'),
        ),
        migrations.AddField(
            model_name='class',
            name='graduated',
            field=models.DateTimeField(default='2025-10-01'),
        ),
    ]
