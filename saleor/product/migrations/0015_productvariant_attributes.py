# Generated by Django 1.10.3 on 2016-11-30 12:26
from __future__ import unicode_literals

import django.contrib.postgres.fields.hstore
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("product", "0014_remove_productvariant_attributes")]

    operations = [
        migrations.AddField(
            model_name="productvariant",
            name="attributes",
            field=django.contrib.postgres.fields.hstore.HStoreField(
                default="", verbose_name="attributes"
            ),
        )
    ]
