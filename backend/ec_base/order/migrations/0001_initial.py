# Generated by Django 4.0.6 on 2022-09-07 07:54

import django.db.models.deletion
from django.db import migrations, models

import ec_base.common.constant.db_table
import ec_base.common.models.base


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("master", "0001_initial"),
        ("customer", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "created_by",
                    ec_base.common.models.base.CurrentUserField(
                        null=True,
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="%(app_label)s_%(class)s_created_by",
                        to="customer.customer",
                    ),
                ),
                (
                    "payment_status",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name=ec_base.common.constant.db_table.DBTable["ORDER"],
                        to="master.masterpaymentstatus",
                    ),
                ),
                (
                    "shipping_status",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name=ec_base.common.constant.db_table.DBTable["ORDER"],
                        to="master.mastershippingstatus",
                    ),
                ),
                (
                    "status",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name=ec_base.common.constant.db_table.DBTable["ORDER"],
                        to="master.masterorderstatus",
                    ),
                ),
                (
                    "updated_by",
                    ec_base.common.models.base.CurrentUserField(
                        null=True,
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="%(app_label)s_%(class)s_updated_by",
                        to="customer.customer",
                    ),
                ),
            ],
            options={
                "db_table": ec_base.common.constant.db_table.DBTable["ORDER"],
            },
        ),
    ]
