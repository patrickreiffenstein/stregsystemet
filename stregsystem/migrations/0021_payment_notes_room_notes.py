# Generated by Django 4.1.13 on 2024-12-09 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stregsystem", "0020_alter_member_username"),
    ]

    operations = [
        migrations.AddField(
            model_name="payment",
            name="notes",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="room",
            name="notes",
            field=models.TextField(blank=True),
        ),
    ]