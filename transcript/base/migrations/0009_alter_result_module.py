# Generated by Django 5.0 on 2024-02-08 15:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_alter_result_module'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='module',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.module'),
        ),
    ]