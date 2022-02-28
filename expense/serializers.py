
from rest_framework import serializers
from.models import Expense, ExpenseDetail


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'


class ExpenseDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExpenseDetail
        fields = '__all__'

