# Generated by Django 4.1 on 2024-03-08 21:17

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("taxi", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="car",
            name="drivers",
        ),
    ]
