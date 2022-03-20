from django.db import models
from django.utils.timezone import now

# Create your models here.
class Expense(models.Model):
    EXPENSES_TYPES = (
        ('1', 'Mensual'),
        ('2', 'Mensual Variable'),
        ('3', 'Anual'),
        ('4', 'Anual Variable'),
        ('5', 'Único'),

    )
    name = models.CharField(max_length=200)
    start = models.DateField(default=None, blank=True, null=True)
    end = models.DateField(default=None, blank=True, null=True)
    type = models.CharField(max_length=1, choices=EXPENSES_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(default="", blank=True)

    def __str__(self):
        return self.name
        
class Payment(models.Model):
    date = models.DateField(default=now,)
    amount = models.FloatField()
    description = models.TextField(default="", blank=True)
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE, related_name='payments', blank=True, null=True)
    hoursValue = models.FloatField(default=0)
    voucher  = models.FileField(upload_to='vouchers/', blank=True, default='', null=True)
    estimated = models.FloatField(default=0)
    
    def __str__(self):
        return self.name