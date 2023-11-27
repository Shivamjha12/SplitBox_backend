from rest_framework import serializers
from .models import  *


class GroupSerializer(serializers.ModelSerializer):
    user=   serializers.CharField(source="user.email")
    class Meta:
        model = Group
        fields = ['name','description','user']


    
class ExpenseSerializer(serializers.ModelSerializer):
    paid_by=serializers.CharField(source="paid_by.email")
    group=serializers.CharField(source="group.name")
    class Meta:
        model = Expense
        fields = ['group', 'paid_by', 'title', 'amount', 'date']
        
class UserEmailSerializer(serializers.Serializer):
    email = serializers.EmailField()
    
class ExpenseItemSerializer(serializers.ModelSerializer):
    users = UserEmailSerializer(many=True,source="user")
    title = serializers.CharField(source="expense.title")
    expenseid = serializers.CharField(source="expense.expenseid")
    paid_by = serializers.CharField(source="expense.paid_by.email")
    amount = serializers.CharField(source="expense.amount")
    date = serializers.DateField(source="expense.date")
    class Meta:
        model = ExpenseItem
        fields = ['title','expenseid','paid_by','amount','date','description','users']
        
        
class PaymentSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.email")
    class Meta:
        model = Payment
        fields = ['user','amount_to_pay','paid']