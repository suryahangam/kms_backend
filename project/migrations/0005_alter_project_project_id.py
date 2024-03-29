# Generated by Django 5.0 on 2024-01-17 11:25

import kms.utils
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("project", "0004_alter_project_project_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="project_id",
            field=models.CharField(
                default=kms.utils.generate_unique_ID, max_length=50, unique=True
            ),
        ),
    ]
