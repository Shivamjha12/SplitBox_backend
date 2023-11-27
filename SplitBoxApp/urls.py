from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-user/', include('Accounts.urls')),
    path('api-friend/', include('FriendOperations.urls')),
    path('api-main/', include('expenses.urls')),
]
