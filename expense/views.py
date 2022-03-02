from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.views import APIView
from .models import Expense, ExpenseCategory, ExpenseDetail
from rest_framework import generics
from .serializers import CategorySerializer, ExpenseDetailSerializer, ExpenseSerializer
from rest_framework.permissions import IsAuthenticated


class ExpenseView(APIView):
    permission_classes = [IsAuthenticated]
    serialezer_class = [ExpenseSerializer]

    def get(self,request):
        user_expenses = Expense.objects.filter(user=request.user)
        return Response({"Expenses":ExpenseSerializer(user_expenses,many=True).data})


class ExpenseDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request):
        detail = request.data.get('detail')
        seriazizer = ExpenseDetailSerializer(data=detail)
        seriazizer.is_valid(raise_exception=True)
        saved_data = seriazizer.save()
        return Response({'Success':ExpenseDetailSerializer(saved_data).data})


class ExpenseCategoryView(generics.ListCreateAPIView):
    queryset = ExpenseCategory.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
