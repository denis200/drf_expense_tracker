from django.contrib import admin
from django.urls import include, path
from . import views
from expense.views import ExpenseCategoryView, ExpenseDetailView, ExpenseView

urlpatterns = [
    path('expense/', ExpenseView.as_view()),
    path('expense/detail/', ExpenseDetailView.as_view()),
    path('expense/category/', ExpenseCategoryView.as_view()),
    path('set_session/', views.set_session),
    path('get_products/', views.get_products),
]