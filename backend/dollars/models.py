from datetime import date
from unicodedata import name
from django.db import models
from django.utils.timezone import now

class Movement(models.Model):
    MOVEMENT_TYPES = (
        ('1', 'Credit'),
        ('2', 'Debit'),
    )

    MOVEMENT_SOURCES =(
        ('1', 'Bank'),
        ('2', 'AIRTM'),
    )

    name = models.CharField(max_length=500)
    amountInDollars = models.DecimalField(max_digits=10, decimal_places=2)
    amountInPesos = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(default=now)
    type = models.CharField(max_length=4, choices=MOVEMENT_TYPES)
    sellValue = models.CharField(max_length=4, choices=MOVEMENT_SOURCES, default='1', null=True, blank=True)

    def __str__(self):
        return self.name

class Sources (models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(default="", blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.name

class MovementDetail (models.Model):
    movement = models.ForeignKey(Movement, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    date = models.DateField(default=now)
    amountInPesos = models.DecimalField(max_digits=10, decimal_places=2)
    amountInDollars = models.DecimalField(max_digits=10, decimal_places=2)
    amountInLocal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=0)
    localCurrency = models.CharField(max_length=20, blank=True, null=True)
    localCurrencyCode = models.CharField(max_length=20, blank=True, null=True)
    def __str__(self):
        return self.movement.name + " - " + self.source.name
