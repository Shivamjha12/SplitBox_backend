from rest_framework import serializers
from .models import Friendship
from Accounts.models import User
class UserFriendListSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="friend.email")
    
    class Meta:
        model = Friendship
        fields = [ 'user']
        
    
            