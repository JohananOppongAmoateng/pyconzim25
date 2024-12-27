# Generated by Django 5.0.2 on 2024-03-02 22:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("coc", "0002_alter_coc_id"),
        ("home", "0008_pyconevent"),
    ]

    operations = [
        migrations.AddField(
            model_name="coc",
            name="event_year",
            field=models.ForeignKey(
                default="2024",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="cocs",
                to="home.eventyear",
            ),
        ),
    ]