# Generated by Django 5.0.6 on 2024-07-01 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_user_country"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={
                "verbose_name": "пользователь",
                "verbose_name_plural": "пользователи",
            },
        ),
    ]
