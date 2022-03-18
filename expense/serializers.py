
from django.forms import CharField
from rest_framework import serializers
from.models import Expense, ExpenseCategory, ExpenseDetail


class ExpenseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseDetail
        fields = ['title','quantity','price','expense']


class ExpenseSerializer(serializers.ModelSerializer):
    expense_detail= ExpenseDetailSerializer( many = True)
    class Meta:
        model = Expense
        fields = '__all__'

    def create(self, validated_data):
        expense_data = validated_data.pop('expense_detail')
        ser = ExpenseDetailSerializer(data = expense_data,many = True)
        ser.is_valid(raise_exception=True)
        expense = Expense.objects.create(**validated_data)
        for detail_data in expense_data:
            ExpenseDetail.objects.create( **detail_data,expense = expense)
        return expense


class CategorySerializer(serializers.ModelSerializer):
    expense = Expense.objects.all()
    class Meta:
        model = ExpenseCategory
        fields = "__all__"




    


