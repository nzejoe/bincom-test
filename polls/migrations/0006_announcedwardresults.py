# Generated by Django 4.1.5 on 2023-01-24 11:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0005_announcedstateresults"),
    ]

    operations = [
        migrations.CreateModel(
            name="AnnouncedWardResults",
            fields=[
                (
                    "result_id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False
                    ),
                ),
                ("ward_name", models.CharField(max_length=50)),
                ("party_abbreviation", models.CharField(max_length=4)),
                ("party_score", models.IntegerField()),
                ("entered_by_user", models.CharField(max_length=50)),
                (
                    "date_entered",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("user_ip_address", models.CharField(max_length=50)),
            ],
        ),
    ]
