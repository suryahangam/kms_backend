# Generated by Django 5.0 on 2024-01-15 02:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("client", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="client",
            name="unique_client_id",
            field=models.CharField(default="1705286065598", max_length=50, unique=True),
        ),
    ]