# Generated by Django 4.1.5 on 2023-01-24 10:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0003_announcedlgaresults_alter_agentname_email"),
    ]

    operations = [
        migrations.CreateModel(
            name="AnnouncedPuResults",
            fields=[
                (
                    "result_id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False
                    ),
                ),
                ("polling_unit_uniqueid", models.CharField(max_length=50)),
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
