# Generated by Django 2.0.2 on 2018-09-27 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stregsystem', '0008_add_sale_products_id_timestamp_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='BreadRazzia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('members', models.ManyToManyField(to='stregsystem.Member')),
            ],
        ),
    ]