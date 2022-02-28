from django.contrib import admin

from expense.models import Expense, ExpenseCategory, ExpenseDetail

admin.site.register(Expense)
admin.site.register(ExpenseCategory)
admin.site.register(ExpenseDetail)
