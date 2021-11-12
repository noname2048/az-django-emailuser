# Generated by Django 3.2.8 on 2021-10-24 14:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="myuser",
            options={"verbose_name": "myuser", "verbose_name_plural": "myusers"},
        ),
        migrations.AddField(
            model_name="myuser",
            name="date_joined",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="date joined"
            ),
        ),
    ]