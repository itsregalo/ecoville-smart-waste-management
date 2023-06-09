# Generated by Django 4.2 on 2023-05-10 14:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="GarbageBin",
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
                ("location", models.CharField(max_length=200)),
                ("capacity", models.PositiveIntegerField()),
                (
                    "bin_type",
                    models.CharField(
                        choices=[
                            ("recycling", "Recycling Bin"),
                            ("compost", "Compost Bin"),
                            ("landfill", "Landfill Bin"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Garbage Bins",
                "db_table": "garbage_bins",
            },
        ),
        migrations.CreateModel(
            name="WasteDisposal",
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
                ("amount", models.PositiveIntegerField()),
                (
                    "waste_type",
                    models.CharField(
                        choices=[
                            ("plastic", "Plastic"),
                            ("organic", "Organic"),
                            ("metal", "Metal"),
                            ("glass", "Glass"),
                            ("paper", "Paper"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Waste Disposals",
                "db_table": "waste_disposals",
            },
        ),
        migrations.CreateModel(
            name="Reward",
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
                ("name", models.CharField(blank=True, max_length=255, null=True)),
                ("cost", models.PositiveIntegerField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Rewards",
                "db_table": "rewards",
            },
        ),
        migrations.CreateModel(
            name="GarbageCollectionRequest",
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
                ("pickup_time", models.DateTimeField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("pending", "Pending"),
                            ("accepted", "Accepted"),
                            ("rejected", "Rejected"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "bin",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="admindashboard.garbagebin",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Garbage Collection Requests",
                "db_table": "garbage_collection_requests",
            },
        ),
        migrations.CreateModel(
            name="GarbageCollection",
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
                ("pickup_time", models.DateTimeField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("scheduled", "Scheduled"),
                            ("completed", "Completed"),
                            ("cancelled", "Cancelled"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "bin",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="admindashboard.garbagebin",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Garbage Collections",
                "db_table": "garbage_collections",
            },
        ),
        migrations.CreateModel(
            name="CreditScore",
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
                ("score", models.PositiveIntegerField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Credit Scores",
                "db_table": "credit_scores",
            },
        ),
    ]
