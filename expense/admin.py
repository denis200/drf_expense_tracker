from django.contrib import admin

from expense.models import Expense, ExpenseCategory, ExpenseDetail

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ['user','amount','category','date']

admin.site.register(ExpenseCategory)
admin.site.register(ExpenseDetail)
