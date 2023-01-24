# Generated by Django 4.1.5 on 2023-01-24 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0008_party_state_ward_pollingunit_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="agentname",
            old_name="pollingunit_uniqueid",
            new_name="pollingunit",
        ),
        migrations.RenameField(
            model_name="lga",
            old_name="state_id",
            new_name="state",
        ),
        migrations.RenameField(
            model_name="pollingunit",
            old_name="lga_id",
            new_name="lga",
        ),
        migrations.RenameField(
            model_name="pollingunit",
            old_name="ward_id",
            new_name="ward",
        ),
        migrations.RenameField(
            model_name="ward",
            old_name="lga_id",
            new_name="lga",
        ),
    ]
