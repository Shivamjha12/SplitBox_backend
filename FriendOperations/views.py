# views.py
from django.shortcuts import render, get_object_or_404
from .models import Friendship
from Accounts.models import User
from django.http import JsonResponse
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Friendship
from .serializers import UserFriendListSerializer

class add_friend(APIView):
    def get(self, request, *args, **kwargs):
        current_user = request.user
        friends = Friendship.objects.filter(user=current_user)
        serializer = UserFriendListSerializer(friends, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        friend_email = request.data['email']
        user_email = request.data['user_email']
        if friend_email:
            try:
                friend = User.objects.get(email=friend_email)
                user = User.objects.get(email=user_email)
                print(friend,"---",user)
                Friendship.objects.create(user=user, friend=friend)
                return Response({"message":"User added your friend List"},status=201)
            except User.DoesNotExist:
                # Handle the case where the user with the provided email does not exist
                return Response({"message":"User is Not Registered on Platform"},status=404)
        else:
            return Response({"message":"Please Provide Email"})  
