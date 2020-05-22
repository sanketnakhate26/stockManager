# Generated by Django 3.0.6 on 2020-05-21 23:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('quantity', models.IntegerField()),
                ('buy_price', models.FloatField()),
                ('sell_price', models.FloatField()),
                ('trade_type', models.CharField(choices=[('delivery', 'DELIVERY'), ('intraday', 'INTRADAY')], default='DELIVERY', max_length=25)),
                ('date_buy', models.DateTimeField(default=datetime.datetime.now)),
                ('date_sell', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Overview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('quantity', models.IntegerField()),
                ('buy_price', models.FloatField()),
                ('trade_type', models.CharField(choices=[('delivery', 'DELIVERY'), ('intraday', 'INTRADAY')], default='DELIVERY', max_length=25)),
                ('date_buy', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
