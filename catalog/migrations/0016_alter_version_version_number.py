# Generated by Django 5.1.1 on 2024-10-05 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0015_alter_version_is_current"),
    ]

    operations = [
        migrations.AlterField(
            model_name="version",
            name="version_number",
            field=models.SmallIntegerField(
                help_text="Введите номер версии", verbose_name="Номер версии"
            ),
        ),
    ]
