from django.db import models
from datetime import datetime

# Create your models here.

class Stock(models.Model):
    ticker = models.CharField(max_length=6)
    open_price = models.FloatField()
    close_price = models.FloatField()
    volume = models.IntegerField()

    def __str__(self):
        return self.ticker
