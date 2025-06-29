from django.urls import path
from .import views
urlpatterns = [
    path('',views.home, name='home'),
    path('reg/register/',views.register,name='register'),
    path('log/login/',views.Login_view,name='login'),
    path('log/logout',views.Logout_view,name='logout'),
    path('category/<int:category_id>/',views.posts_by_category, name='posts_by_category'),
    path('blogs/search/',views.Search , name='search'),
    path('<slug:slug>/',views.blogs, name='blogs'),
]