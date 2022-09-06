# Generated by Django 4.0.7 on 2022-09-06 06:29

import django.db.models.deletion
from django.db import migrations, models

import ec_base.common.constant.db_table


class Migration(migrations.Migration):
    dependencies = [
        ('file_management', '0001_initial'),
        ('user_info', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='photo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT,
                                    related_name=ec_base.common.constant.db_table.DBTable['USER_INFO'],
                                    to='file_management.filemanagement'),
        ),
    ]
