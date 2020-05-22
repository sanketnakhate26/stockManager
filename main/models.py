from django.db import models
from datetime import datetime

TRADE_CHOICES = (
    ('delivery','DELIVERY'),
    ('intraday', 'INTRADAY'),
)
class Overview(models.Model):
    name = models.CharField(max_length=25)
    quantity = models.IntegerField()
    buy_price = models.FloatField()
    trade_type = models.CharField(max_length=25, choices=TRADE_CHOICES, default='DELIVERY')
    date_buy = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name

class History(models.Model):
    name = models.CharField(max_length=25)
    quantity = models.IntegerField()
    buy_price = models.FloatField()
    sell_price = models.FloatField()
    trade_type = models.CharField(max_length=25, choices=TRADE_CHOICES, default='DELIVERY')
    date_buy = models.DateTimeField(default=datetime.now)
    date_sell = models.DateTimeField(default=datetime.now)
    profit_loss = models.FloatField(default=0)

    def __str__(self):
        return self.name