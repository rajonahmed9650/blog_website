
from django.urls import path
from .views import dashboard,categories,add_categories,edit_categories,delete_categories,posts,add_new_posts,delete_posts,update_posts

app_name = 'dashboard'

urlpatterns = [
    path('',dashboard,name='dashboard'),
    path('categories/',categories,name='categories'),
    path('categories/add',add_categories,name='add_categories'),
    path('categories/edit/<int:pk>',edit_categories,name='edit_categories'),
    path('categories/delete/<int:pk>',delete_categories,name='delete_categories'),
    path('posts/',posts, name='posts'),
    path('posts/add/', add_new_posts , name = 'add_new_posts'),
    path('posts/delete/<int:pk>', delete_posts , name = 'delete_posts'),
    path('posts/update/<int:pk>', update_posts , name = 'update_posts')     
]