from django.db import models
from Accounts.models import User
import uuid
class Group(models.Model):
    groupid = models.UUIDField(default=uuid.uuid4,null=True, blank=True, editable=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.name

class Expense(models.Model):
    expenseid = models.UUIDField(default=uuid.uuid4,null=True, blank=True, editable=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE,null=True,blank=True)
    paid_by = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class ExpenseItem(models.Model):
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    user = models.ManyToManyField(User)
    # You can add more fields specific to the expense item

    def __str__(self):
        return f"{self.description}"
    
class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    expense_item = models.ForeignKey(ExpenseItem, on_delete=models.CASCADE)
    amount_to_pay = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)
    # You can add more fields specific to the payment

    def __str__(self):
        return f"{self.user.name} - {self.expense_item.description} - Paid: {self.paid}"
