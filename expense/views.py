from urllib import request
from rest_framework.response import Response
from django.http import JsonResponse

from django.shortcuts import render
from rest_framework.views import APIView

from users.models import User


from .models import Expense, ExpenseDetail
from .serializers import ExpenseDetailSerializer, ExpenseSerializer

from rest_framework.permissions import SAFE_METHODS,BasePermission , IsAuthenticated


# class UserExpensePermission(BasePermission):
#     message = 'Editing posts is restricted to ther author only'

#     def has_object_permission(self, request, view, obj):
#         if request.method in SAFE_METHODS:
#             return True
#         return obj.owner == request.user


class ExpenseView(APIView):
    permission_classes = [IsAuthenticated]
    serialezer_class = [ExpenseSerializer]
    def get(self,request):
        user_expenses = Expense.objects.filter(user=request.user)
        return Response({"Expenses":ExpenseSerializer(user_expenses,many=True).data})


class ExpenseDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        expense_detail_by_id = ExpenseDetail.objects.filter(expense=request.data.get('pk'))
        return Response({'Details':ExpenseDetailSerializer(expense_detail_by_id,many=True).data})

    def post(self,request):
        detail = request.data.get('detail')
        seriazizer = ExpenseDetailSerializer(data=detail)
        seriazizer.is_valid(raise_exception=True)
        saved_data = seriazizer.save()

        return Response({'Success':ExpenseDetailSerializer(saved_data).data})