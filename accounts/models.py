# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    USER_TYPE_CHOICES = (
        ('admin', 'Admin'),
        ('author', 'Author'),
        ('reader', 'Reader'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='reader')

    USERNAME_FIELD = 'email'   
    REQUIRED_FIELDS = ['username'] 

    def __str__(self):
        return self.email

