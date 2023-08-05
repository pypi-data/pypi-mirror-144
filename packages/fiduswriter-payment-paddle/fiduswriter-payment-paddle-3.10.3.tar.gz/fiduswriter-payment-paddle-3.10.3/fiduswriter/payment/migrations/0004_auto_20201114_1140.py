# Generated by Django 3.1.2 on 2020-11-14 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("payment", "0003_auto_20191201_0339"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="status",
            field=models.CharField(
                choices=[
                    ("active", "Active"),
                    ("trialing", "Trialing"),
                    ("paste_due", "Past due"),
                    ("deleted", "Deleted"),
                ],
                max_length=9,
            ),
        ),
    ]
