# Generated by Django 3.2.18 on 2023-07-26 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("device", "0002_auto_20230723_1743"),
    ]

    operations = [
        migrations.AddField(
            model_name="device",
            name="price",
            field=models.IntegerField(default=67, verbose_name="价格"),
        ),
    ]
