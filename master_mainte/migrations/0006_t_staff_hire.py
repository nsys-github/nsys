# Generated by Django 2.2.3 on 2019-08-08 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master_mainte', '0005_auto_20190808_1710'),
    ]

    operations = [
        migrations.CreateModel(
            name='t_staff_hire',
            fields=[
                ('t_staff_hire_id', models.AutoField(db_column='t_staff_hire_id', editable=False, primary_key=True, serialize=False, verbose_name='社員雇用契約ID')),
                ('change_date', models.DateField(db_column='change_date', verbose_name='変更日')),
                ('hire_type', models.CharField(choices=[('0', '無期雇用'), ('1', '有期雇用')], db_column='hire_type', default='0', max_length=1, verbose_name='有期雇用・無期雇用')),
                ('term_date_from', models.DateField(blank=True, db_column='term_date_from', null=True, verbose_name='有期雇用_開始日')),
                ('term_date_to', models.DateField(blank=True, db_column='term_date_to', null=True, verbose_name='有期雇用_終了日')),
                ('is_active', models.BooleanField(db_column='is_active', default=True, verbose_name='生存フラグ')),
                ('ent_date', models.DateTimeField(db_column='ent_date', editable=False, verbose_name='登録日時')),
                ('ent_id', models.CharField(db_column='ent_id', editable=False, max_length=6, verbose_name='登録者')),
                ('upd_date', models.DateTimeField(blank=True, db_column='upd_date', editable=False, null=True, verbose_name='更新日時')),
                ('upd_id', models.CharField(blank=True, db_column='upd_id', editable=False, max_length=6, null=True, verbose_name='更新者')),
                ('upd_cnt', models.IntegerField(db_column='upd_cnt', default=0, editable=False, verbose_name='更新回数')),
                ('t_company_id', models.ForeignKey(db_column='t_company_id', default='1', on_delete=django.db.models.deletion.PROTECT, to='master_mainte.t_company', verbose_name='会社ID')),
                ('t_staff_id', models.ForeignKey(db_column='t_staff_id', on_delete=django.db.models.deletion.PROTECT, to='master_mainte.t_staff', verbose_name='社員')),
            ],
            options={
                'verbose_name': '社員雇用契約テーブル',
                'verbose_name_plural': '社員雇用契約テーブル',
                'ordering': ['t_staff_id', '-change_date'],
                'unique_together': {('t_staff_id', 'change_date')},
            },
        ),
    ]
