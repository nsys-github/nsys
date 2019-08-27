# Generated by Django 2.2.3 on 2019-08-09 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master_mainte', '0009_auto_20190809_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='t_manager',
            name='t_company_id',
            field=models.ForeignKey(db_column='t_company_id', limit_choices_to={'company_type': 'OT'}, on_delete=django.db.models.deletion.PROTECT, to='master_mainte.t_company', verbose_name='会社ID'),
        ),
        migrations.CreateModel(
            name='t_workplace',
            fields=[
                ('t_workplace_id', models.AutoField(db_column='t_workplace_id', editable=False, primary_key=True, serialize=False, verbose_name='就業場所ID')),
                ('workplace_name', models.CharField(db_column='workplace_name', max_length=500, verbose_name='就業場所_名称')),
                ('postcode', models.CharField(blank=True, db_column='postcode', max_length=10, null=True, verbose_name='郵便番号')),
                ('address1', models.CharField(db_column='address1', max_length=250, verbose_name='住所１')),
                ('address2', models.CharField(blank=True, db_column='address2', max_length=250, null=True, verbose_name='住所２')),
                ('tel', models.CharField(blank=True, db_column='tel', max_length=15, null=True, verbose_name='TEL')),
                ('fax', models.CharField(blank=True, db_column='fax', max_length=15, null=True, verbose_name='FAX')),
                ('station', models.CharField(blank=True, db_column='station', max_length=250, null=True, verbose_name='最寄駅')),
                ('delete_flg', models.BooleanField(db_column='delete_flg', default=False, verbose_name='削除フラグ')),
                ('ent_date', models.DateTimeField(db_column='ent_date', editable=False, verbose_name='登録日時')),
                ('ent_id', models.CharField(db_column='ent_id', editable=False, max_length=6, verbose_name='登録者')),
                ('upd_date', models.DateTimeField(blank=True, db_column='upd_date', editable=False, null=True, verbose_name='更新日時')),
                ('upd_id', models.CharField(blank=True, db_column='upd_id', editable=False, max_length=6, null=True, verbose_name='更新者')),
                ('upd_cnt', models.IntegerField(db_column='upd_cnt', default=0, editable=False, verbose_name='更新回数')),
                ('t_company_id', models.ForeignKey(db_column='t_company_id', on_delete=django.db.models.deletion.PROTECT, to='master_mainte.t_company', verbose_name='会社ID')),
            ],
            options={
                'verbose_name': '就業場所テーブル',
                'verbose_name_plural': '就業場所テーブル',
                'ordering': ['t_company_id', 'workplace_name'],
            },
        ),
    ]
