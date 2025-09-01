from django.urls import path
from .views import home,posts_by_category,Search,blogs,register,Login_view,Logout_view,profile_view,update_profile
# from accounts import views
urlpatterns = [
    path('',home, name='home'),
    path('reg/register/',register,name='register'),
    path('log/login/',Login_view,name='login'),
    path('log/logout',Logout_view,name='logout'),
    path('category/<int:category_id>/',posts_by_category, name='posts_by_category'),
    path('blogs/search/',Search , name='search'),
    path('<slug:slug>/',blogs, name='blogs'),
    path('pro/profile/',profile_view, name='profile_view'),
    path('pro/update/',update_profile, name='update_profile'),
]