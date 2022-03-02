from django.contrib import admin
from django.urls import include, path

from expense.views import ExpenseCategoryView, ExpenseDetailView, ExpenseView

urlpatterns = [
    path('expense/', ExpenseView.as_view()),
    path('expense/detail/', ExpenseDetailView.as_view()),
    path('expense/add_category/', ExpenseCategoryView.as_view()),
]