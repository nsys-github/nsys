# Generated by Django 2.2.3 on 2019-08-28 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0005_auto_20190827_1201'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='t_quotation',
            options={'ordering': ['-contract_date_from', 't_company_id'], 'verbose_name': '見積テーブル', 'verbose_name_plural': '見積テーブル'},
        ),
        migrations.AlterModelOptions(
            name='t_quotation_item',
            options={'ordering': ['t_staff_id'], 'verbose_name': '見積内訳テーブル', 'verbose_name_plural': '見積内訳テーブル'},
        ),
        migrations.AddField(
            model_name='t_quotation_item',
            name='unitprice_exclude_tax',
            field=models.DecimalField(blank=True, db_column='unitprice_exclude_tax', decimal_places=3, max_digits=13, null=True, verbose_name='契約単価(税抜)'),
        ),
        migrations.AlterField(
            model_name='t_quotation_item',
            name='ent_date',
            field=models.DateTimeField(db_column='ent_date', editable=False, verbose_name='登録日時'),
        ),
    ]