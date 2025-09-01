from django import forms
from block.views import Category,Blogs
from django.contrib.auth.forms import UserCreationForm
from  accounts.models import CustomUser

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        

class BlogsForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = ('title','category','blog_image','short_description','blog_body','status','is_feacherd')        


class AddUserForm(UserCreationForm):
    class Meta:
        model =CustomUser
        fields = ('username','email','first_name','last_name','is_active','is_staff','is_superuser','groups','user_permissions')
        

class EditForm(forms.ModelForm):
    class Meta:
        model =CustomUser
        fields = ('username','email','first_name','last_name','is_active','is_staff','is_superuser','groups','user_permissions')        