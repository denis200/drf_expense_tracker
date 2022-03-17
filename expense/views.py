from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
import json
from expense.utils import get_products_by_code, set_session_id
from .models import Expense, ExpenseCategory, ExpenseDetail
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework import mixins
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


class ExpenseCategoryView(generics.ListCreateAPIView, mixins.UpdateModelMixin):
    queryset = ExpenseCategory.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]


@api_view(['POST'])
def set_session(request):
    if request.method == 'POST':
        set_session_id(request.POST.get('phone'))
        return Response({"success":"ok"},status=status.HTTP_200_OK)


@api_view(['POST'])
def get_products(request):
    if request.method == 'POST':
        phone =str(request.POST.get('phone'))
        qr =str(request.POST.get('qr'))
        code =str(request.POST.get('code'))
        expense_id = int(request.POST.get('expense_id'))
        response = get_products_by_code(phone,code,qr)
        items = response['ticket']['document']['receipt']['items']
        for i in items:
            i['expense'] = expense_id
        seriazizer = ExpenseDetailSerializer(data = items,many = True)
        seriazizer.is_valid(raise_exception=True)
        saved_data = seriazizer.save()
        return Response({"items":'ok'},status=status.HTTP_200_OK)

