# Generated by Django 4.2 on 2023-05-10 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("admindashboard", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="garbagecollectionrequest",
            name="status",
        ),
        migrations.AddField(
            model_name="garbagecollectionrequest",
            name="is_picked",
            field=models.BooleanField(default=False),
        ),
    ]
