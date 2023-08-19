# Generated by Django 4.1.6 on 2023-04-19 04:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="student",
            old_name="school",
            new_name="school_name",
        ),
        migrations.AddField(
            model_name="student",
            name="standard",
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]