# Generated by Django 3.1.7 on 2021-06-25 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0014_property_price_us'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='price_us',
            field=models.IntegerField(null=True),
        ),
    ]