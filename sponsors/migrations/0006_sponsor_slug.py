# Generated by Django 5.0.2 on 2024-03-17 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sponsors", "0005_rename_type_sponsor_sponsor_type_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="sponsor",
            name="slug",
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
