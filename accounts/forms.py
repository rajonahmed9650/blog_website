# accounts/forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label='Email')  # এখানে username এর জায়গায় email
    class Meta:
        model = CustomUser
        fields = ['email', 'password']


# accounts/forms.py
from django import forms
from .models import CustomUser

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'user_type']
