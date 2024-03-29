# Generated by Django 4.1.5 on 2023-03-27 21:28
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SiteVisit",
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
                ("date", models.DateField(auto_now_add=True)),
                ("time", models.TimeField(auto_now_add=True)),
                ("location", models.TextField(blank=True, max_length=256)),
                (
                    "interaction_type",
                    models.CharField(
                        choices=[("open", "Open"), ("read", "View"), ("view", "Read")],
                        max_length=4,
                    ),
                ),
            ],
        ),
    ]
