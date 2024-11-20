# Generated by Django 5.1.3 on 2024-11-20 10:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TodoList",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("status", models.BooleanField(default=False)),
                ("created_at", models.DateField(default=datetime.date(2024, 11, 20))),
            ],
        ),
        migrations.CreateModel(
            name="WebsiteViews",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("total_views", models.PositiveIntegerField(default=0)),
            ],
        ),
    ]