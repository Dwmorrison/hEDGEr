# Generated by Django 2.2.17 on 2021-02-03 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hedger_app', '0007_apigets'),
    ]

    operations = [
        migrations.AddField(
            model_name='balances',
            name='PAX_price',
            field=models.CharField(default=0, max_length=60),
        ),
    ]