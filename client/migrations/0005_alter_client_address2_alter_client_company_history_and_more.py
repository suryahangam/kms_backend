# Generated by Django 5.0 on 2024-01-17 11:25

import kms.utils
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("client", "0004_alter_client_unique_client_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="client",
            name="address2",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="client",
            name="company_history",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="client",
            name="contactTerm",
            field=models.CharField(
                choices=[
                    ("6", "6 Months"),
                    ("9", "9 Months"),
                    ("12", "12 Months"),
                    ("24", "24 Months"),
                    ("36", "36 Months"),
                    ("0", "Unlimited"),
                ],
                default=0,
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="client",
            name="unique_client_id",
            field=models.CharField(
                default=kms.utils.generate_unique_ID, max_length=50, unique=True
            ),
        ),
    ]
