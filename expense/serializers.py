
from rest_framework import serializers
from.models import Expense, ExpenseCategory, ExpenseDetail


class ExpenseDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExpenseDetail
        fields = '__all__'
        

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ExpenseCategory
        fields = "__all__"


class ExpenseSerializer(serializers.ModelSerializer):
    expense_detail= ExpenseDetailSerializer(many = True)
    class Meta:
        model = Expense
        fields = '__all__'


