# Generated by Django 4.1.5 on 2023-01-24 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AgentName",
            fields=[
                (
                    "name_id",
                    models.IntegerField(
                        max_length=11, primary_key=True, serialize=False
                    ),
                ),
                ("firstname", models.CharField(max_length=255)),
                ("lastname", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254, null=True)),
                ("phone", models.CharField(max_length=13)),
                ("pollingunit_uniqueid", models.IntegerField(max_length=11)),
            ],
        ),
    ]