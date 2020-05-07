from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    email=models.EmailField(max_length=254)
    def __str__(self):
        return f'{self.username} Profile'