from accounts.models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Comment

class RegisterFrom(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email','username','password1','password2')
        

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
        widgets = {
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 2,
                'style': 'resize:none;'
            }),
        }

