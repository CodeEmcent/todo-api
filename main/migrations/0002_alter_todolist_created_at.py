# Generated by Django 5.1.3 on 2024-11-20 10:50

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todolist",
            name="created_at",
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]