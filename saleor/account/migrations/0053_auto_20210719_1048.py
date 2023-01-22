# Generated by Django 3.2.5 on 2021-07-19 10:48

import django.contrib.postgres.indexes
from django.db import migrations

import saleor.account.models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0052_customerevent_app"),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name="user",
            name="account_use_email_d707ff_gin",
        ),
        migrations.AlterField(
            model_name="address",
            name="phone",
            field=saleor.account.models.PossiblePhoneNumberField(
                blank=True, db_index=True, default="", max_length=128, region=None
            ),
        ),
        migrations.AddIndex(
            model_name="address",
            index=django.contrib.postgres.indexes.GinIndex(
                fields=["first_name", "last_name", "city", "country"],
                name="address_search_gin",
                opclasses=[
                    "gin_trgm_ops",
                    "gin_trgm_ops",
                    "gin_trgm_ops",
                    "gin_trgm_ops",
                ],
            ),
        ),
        migrations.AddIndex(
            model_name="user",
            index=django.contrib.postgres.indexes.GinIndex(
                fields=["email", "first_name", "last_name"],
                name="user_search_gin",
                opclasses=["gin_trgm_ops", "gin_trgm_ops", "gin_trgm_ops"],
            ),
        ),
    ]
