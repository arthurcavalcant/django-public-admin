# Generated by Django 3.1.2 on 2020-10-06 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Beverage",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=32)),
                ("amount", models.IntegerField()),
                ("alcoholic", models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name="Snack",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=32)),
                ("amount", models.IntegerField()),
                ("vegan", models.BooleanField()),
            ],
        ),
    ]