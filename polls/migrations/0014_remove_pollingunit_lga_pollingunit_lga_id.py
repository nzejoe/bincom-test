# Generated by Django 4.1.5 on 2023-01-24 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0013_alter_pollingunit_date_entered_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="pollingunit",
            name="lga",
        ),
        migrations.AddField(
            model_name="pollingunit",
            name="lga_id",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
