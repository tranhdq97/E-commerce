# Generated by Django 4.0.7 on 2022-09-05 06:45

from django.db import migrations, models
import django.db.models.deletion
import ec_base.common.constant.db_table
import ec_base.common.models.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('master', '0001_initial'),
        ('user_info', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('is_active', models.BooleanField(default=True)),
                ('is_leave', models.BooleanField(default=False)),
                ('info', models.OneToOneField(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name=ec_base.common.constant.db_table.DBTable['CUSTOMER'], to='user_info.userinfo')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name=ec_base.common.constant.db_table.DBTable['CUSTOMER'], to='master.mastercustomertype')),
            ],
            options={
                'db_table': ec_base.common.constant.db_table.DBTable['CUSTOMER'],
            },
            managers=[
                ('objects', ec_base.common.models.managers.CustomUserManager()),
            ],
        ),
    ]
