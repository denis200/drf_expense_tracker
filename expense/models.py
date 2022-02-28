from django.db import models
from django.utils import timezone

from users.models import User

class ExpenseCategory(models.Model):
    name = models.CharField(max_length=100,unique=True)
    icon = models.CharField(max_length=100,blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2,default=0)

    def __str__(self):
        return self.name


class ExpenseDetail(models.Model):
    title = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    expense = models.ForeignKey("Expense",on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} | {self.expense}"


class Expense(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')
    category = models.ForeignKey(ExpenseCategory,on_delete=models.CASCADE,related_name='expense_category')
    date = models.DateTimeField(default=timezone.now())
    note = models.CharField(max_length=250,blank=True)

    def __str__(self):
        formated_date = self.date.strftime( "%d/%m/%y %H:%M")
        return f"{formated_date} {self.user.user_name}"

    class Meta:
        ordering = ['date']