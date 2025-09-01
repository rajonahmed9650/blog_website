from django.db import models
from accounts.models import CustomUser

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50,blank=True)
    last_name = models.CharField(max_length=50,blank=True)
    profile_image = models.ImageField(upload_to='profile_images/',null=True,blank=True)
    bi0 = models.TextField(null=True,blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
         return f"{self.user.username}'s Profile"
