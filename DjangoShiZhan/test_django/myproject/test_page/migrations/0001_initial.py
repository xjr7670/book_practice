# Generated by Django 4.2 on 2023-04-23 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Department",
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
                (
                    "dep_name",
                    models.CharField(
                        max_length=32, unique=True, verbose_name="Department Name"
                    ),
                ),
                (
                    "dep_script",
                    models.CharField(max_length=60, null=True, verbose_name="Comment"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Person",
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
                ("name", models.CharField(max_length=32, verbose_name="姓名")),
                ("email", models.EmailField(max_length=254, verbose_name="Email")),
                ("salary", models.DecimalField(decimal_places=2, max_digits=8)),
                (
                    "dep",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="test_page.department",
                    ),
                ),
            ],
        ),
    ]