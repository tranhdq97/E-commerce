# Generated by Django 4.0.6 on 2022-07-10 10:59

from django.db import migrations, models
import django.db.models.deletion
import ec_base.common.constant.db_table
import ec_base.common.constant.related_name


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MasterCity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
            options={
                'db_table': ec_base.common.constant.db_table.DBTable['MASTER_CITY'],
            },
        ),
        migrations.CreateModel(
            name='MasterDiscountType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
            options={
                'db_table': ec_base.common.constant.db_table.DBTable['MASTER_DISCOUNT_TYPE'],
            },
        ),
        migrations.CreateModel(
            name='MasterProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
            options={
                'db_table': ec_base.common.constant.db_table.DBTable['MASTER_PRODUCT_CATEGORY'],
            },
        ),
        migrations.CreateModel(
            name='MasterSex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
            options={
                'db_table': ec_base.common.constant.db_table.DBTable['MASTER_SEX'],
            },
        ),
        migrations.CreateModel(
            name='MasterStaffType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
            options={
                'db_table': ec_base.common.constant.db_table.DBTable['MASTER_STAFF_TYPE'],
            },
        ),
        migrations.CreateModel(
            name='MasterDistrict',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('is_deleted', models.BooleanField(default=False)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name=ec_base.common.constant.related_name.RelatedName['MASTER_DISTRICT'], to='master.mastercity')),
            ],
            options={
                'db_table': ec_base.common.constant.db_table.DBTable['MASTER_DISTRICT'],
            },
        ),
    ]
