# Generated by Django 2.2.13 on 2021-09-08 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stregsystem', '0013_mobilepayment_permission_20201123_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobilepayment',
            name='customer_name',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
