# Generated by Django 4.2 on 2024-10-17 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_alter_user_options_user_token"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="avatar",
            field=models.ImageField(
                blank=True, null=True, upload_to="users/", verbose_name="аватар"
            ),
        ),
    ]
