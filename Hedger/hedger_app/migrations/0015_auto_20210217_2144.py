# Generated by Django 2.2.17 on 2021-02-18 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hedger_app', '0014_balances_api_reply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balances',
            name='date_time',
            field=models.CharField(default='hold', max_length=60),
        ),
    ]