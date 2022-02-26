from django.db import models


class Expense(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    note = models.CharField(max_length=250)