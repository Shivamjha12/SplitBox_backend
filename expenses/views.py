from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import *
import jwt,datetime
from rest_framework import generics
from django.http import JsonResponse
import json
import requests
from django.shortcuts import redirect
from .models import *
from rest_framework import viewsets
from .serializers import *
from FriendOperations.models import *

class group_api(viewsets.ViewSet):
    def get_group_details(self, request,groupid):
        try:
            group = Group.objects.filter(groupid=groupid).first()
            serializer = GroupSerializer(group)
            print(group,serializer.data,"--------","hereeeeeeeeeeeeeeeeeeeeeeeeeee")
            return Response(serializer.data,status=200)
        except:
            return Response({"Message":"Something went wrong"},status=401)
        
    def create_group(self, request):
        try:
            user = request.data.get('user')
            name = request.data.get('name')
            description = request.data.get('description')
            user = User.objects.get(email=user)
            Group.objects.create(user=user,name=name,description=description)
            return Response(status=201)
        except:
            return Response({"Message":"Something went wrong"},status=401)
        
    def get_user_groups(self, request,user):
        # try:
        user = User.objects.get(email=user)
        groups = Group.objects.filter(user=user)
        serializer = GroupSerializer(groups,many=True)
        return Response(serializer.data,status=200)
        # except:
        #     return Response({"Message":"Something went wrong"},status=401)
        
class ExpensesApi(viewsets.ViewSet):
    
    def get_all_expenses_of_group(self,request,groupid):
        group = Group.objects.filter(groupid=groupid).first()
        expense_items = ExpenseItem.objects.filter(expense__group=group)
        serializer = ExpenseItemSerializer(expense_items,many=True)
        return Response(serializer.data)
    
    def add_expenses(self,request):
        # try:
            current_user=request.data.get('current_user')
            groupid = request.data.get('groupid')
            title = request.data.get('title')
            description = request.data.get('description')
            amount = request.data.get('amount')
            users = request.data.get('users')
            
            users= list(map(str,users.split(',')))
            print(users,"------------------<<<<<<<<<>>>>>>>>>>>>>>>>>-----------------------")
            group = Group.objects.filter(groupid=groupid).first()
            current_user = User.objects.filter(email=current_user).first()
            expense = Expense.objects.create(group=group,paid_by=current_user,title=title,amount=amount)
            expense.save()
            amount_to_pay = int(amount)/(len(users)+1)
            user_friends = Friendship.get_friends(current_user)
            for i in users:
                if User.objects.filter(email=i).exists() and (i in user_friends):
                    continue
                else:
                    return Response({"Message":f"Your friend {i} is not in your friend list or not registered User"},status=401)
            expense_item_instance = ExpenseItem.objects.create(expense=expense,description=description)
            user_friends_instances  = []
            for i in users:
                user_friend = User.objects.filter(email=i).first()
                user_friends_instances.append(user_friend)
            
            expense_item_instance.user.add(*user_friends_instances)
            expense_item_instance.save()
            print(users,"------------------<<<<<<<<<>>>>>>>>>>>>>>>>>-----------------------")
            for i in users:
                print(i,f"<---------------User is ------------------->")
                user = User.objects.filter(email=i).first()
                payment = Payment.objects.create(user=user,amount_to_pay=amount_to_pay,expense_item=expense_item_instance)
                payment.save()
            return Response({"Message":"Succesfully Created ExpenseItem"},status=201)
        # except:
        #     return Response({"Message":"Something Went Wrong"})
        
    
    
class PaymentApi(viewsets.ViewSet):
    
    def get_all_payments(self,request,user,expense_item_id):
        expense_item = ExpenseItem.objects.filter(expenseitemid=expense_item_id).first()
        payments = Payment.objects.filter(expense_item=expense_item)
        serializer = PaymentSerializer(payments,many=True)
        return Response(serializer.data)
