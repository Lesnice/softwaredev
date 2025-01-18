# Generated by Django 5.1.1 on 2024-09-13 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("labbooking", "0003_rename_is_available_equipment_availability_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="chemical",
            name="concentration",
            field=models.FloatField(default=1),
        ),
        migrations.AddField(
            model_name="chemical",
            name="description",
            field=models.TextField(blank=True),
        ),
    ]
