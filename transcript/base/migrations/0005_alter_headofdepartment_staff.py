# Generated by Django 5.0 on 2024-02-06 12:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_class_created_at_class_graduated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headofdepartment',
            name='staff',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='base.staff'),
        ),
    ]
