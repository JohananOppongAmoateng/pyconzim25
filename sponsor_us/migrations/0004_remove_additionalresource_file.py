# Generated by Django 5.0.2 on 2024-03-05 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("sponsor_us", "0003_alter_sponsorshiptier_amount"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="additionalresource",
            name="file",
        ),
    ]