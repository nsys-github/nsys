# Generated by Django 2.2.3 on 2019-08-09 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master_mainte', '0008_auto_20190809_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='t_manager',
            name='is_client',
            field=models.BooleanField(db_column='is_client', default=False, verbose_name='派遣先担当者フラグ'),
        ),
        migrations.AlterField(
            model_name='t_manager',
            name='is_dispatch',
            field=models.BooleanField(db_column='is_dispatch', default=False, verbose_name='派遣元担当者フラグ'),
        ),
    ]