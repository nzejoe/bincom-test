# Generated by Django 4.1.5 on 2023-01-24 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0010_remove_ward_lga_ward_lga_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pollingunit",
            name="polling_unit_description",
            field=models.TextField(blank=True, null=True),
        ),
    ]