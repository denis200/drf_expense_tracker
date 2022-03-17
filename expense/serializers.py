
from django.forms import CharField
from rest_framework import serializers
from.models import Expense, ExpenseCategory, ExpenseDetail


class ExpenseDetailSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source = 'title',max_length=255)
    class Meta:
        model = ExpenseDetail
        fields = ['name','quantity','price','expense']


class ExpenseSerializer(serializers.ModelSerializer):
    expense_detail= ExpenseDetailSerializer(many = True)
    class Meta:
        model = Expense
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    expense = Expense.objects.all()
    class Meta:
        model = ExpenseCategory
        fields = "__all__"




    


