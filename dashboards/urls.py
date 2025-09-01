
from django.urls import path
from dashboards import views 
app_name = 'dashboard'

urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('categories/',views.categories,name='categories'),
    path('categories/add',views.add_categories,name='add_categories'),
    path('categories/edit/<int:pk>',views.edit_categories,name='edit_categories'),
    path('categories/delete/<int:pk>',views.delete_categories,name='delete_categories'),



    path('posts/',views.posts, name='posts'),
    path('posts/add/', views.add_new_posts , name = 'add_new_posts'),
    path('posts/delete/<int:pk>', views.delete_posts , name = 'delete_posts'),
    path('posts/update/<int:pk>', views.update_posts , name = 'update_posts'),

    path('users/',views.users, name = 'users'), 
    path('users/add/', views.add_users, name ='add_users'),
    path('users/update/<int:pk>',views.update_users, name = 'update_users'),
    path('users/delete/<int:pk>',views.delete_users, name = 'delete_users'),


  

]