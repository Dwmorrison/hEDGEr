# Generated by Django 2.2.17 on 2021-02-05 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hedger_app', '0009_auto_20210202_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apigets',
            name='date_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='balances',
            name='date_time',
            field=models.DateTimeField(),
        ),
    ]
