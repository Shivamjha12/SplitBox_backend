from django.urls import path, include
from .views import *

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

create_group = group_api.as_view({'post': 'create_group',})
get_group_details = group_api.as_view({'get': 'get_group_details'})
get_user_groups = group_api.as_view({'get': 'get_user_groups'})
get_all_expenses_of_group=ExpensesApi.as_view({'get':'get_all_expenses_of_group'})
add_expenses = ExpensesApi.as_view({'post':'add_expenses'})
get_all_payments = PaymentApi.as_view({'get':'get_all_payments'})
urlpatterns = [
    path('create_group', create_group,name="create_group"),
    path('get_group_details/<str:groupid>',get_group_details,name="get_group_details"),
    path('get_user_groups/<str:user>',get_user_groups,name="get_user_groups"),
    path('get_all_expenses_of_group/<str:groupid>',get_all_expenses_of_group,name="get_all_expenses_of_group"),
    path('add_expenses',add_expenses,name="add_expenses"),
    path('get_all_payments/<str:user>/<str:expense_item_id>',get_all_payments,name="get_all_payments"),
    
]
