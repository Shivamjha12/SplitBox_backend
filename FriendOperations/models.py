from django.db import models
from Accounts.models import User

# Create your models here.

class Friendship(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friends')
    friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_friends')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.user.name} friend is {self.friend.name}"
    
    @classmethod
    def get_friends(self,user):
        user=User.objects.filter(email=user).first()
        friends=[]
        user_friends = Friendship.objects.filter(user=user)
        for user_friend in user_friends:
            friends.append(str(user_friend.friend.email))
        print(friends,"hereeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
        return friends
    
    

