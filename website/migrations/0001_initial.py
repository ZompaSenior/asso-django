# Generated by Django 4.1.3 on 2022-11-25 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Member",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("surname", models.CharField(max_length=50)),
                ("cf", models.CharField(max_length=16, unique=True)),
                ("email", models.EmailField(max_length=254)),
            ],
        ),
    ]
