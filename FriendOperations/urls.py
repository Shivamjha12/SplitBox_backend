from django.urls import path, include
from .views import *

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('add_friend/', add_friend.as_view()),
    # path('friends/', add_friend.as_view()),
]