# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
# from .forms import CustomAuthenticationForm, CustomUserCreationForm
# from .models import CustomUser
# from django.contrib import messages

# # Custom Registration Form
# from django import forms

# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = CustomUser
#         fields = ("username", "email", "password1", "password2", "user_type")

# # Register View
# def register_view(request):
#     if request.method == "POST":
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)  # Auto login after registration
#             # রোল অনুযায়ী রিডাইরেক্ট
#             if user.user_type == "admin":
#                 return redirect("/admin-dashboard/")
#             elif user.user_type == "author":
#                 return redirect("/author-dashboard/")
#             else:
#                 return redirect("/reader-dashboard/")
#     else:
#         form = CustomUserCreationForm()
#     return render(request, "accounts/register.html", {"form": form})


# def LoginView(request):
#     if request.method == "POST":
#         form = CustomAuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             email = form.cleaned_data.get("username")  # username ফিল্ড আসলে Email
#             password = form.cleaned_data.get("password")
#             user = authenticate(request, email=email, password=password)
#             if user is not None:
#                 login(request, user)
#                 # ইউজারের role অনুযায়ী redirect
#                 if user.user_type == "admin":
#                     return redirect("/home/")
#                 elif user.user_type == "author":
#                     return redirect("/home/")
#                 else:
#                     return redirect("/home/")
#     else:
#         form = CustomAuthenticationForm()
    
#     return render(request, "accounts/login.html", {"form": form})


# def Logout_view(request):
#     logout(request)
#     return redirect("login")  # লগআউট হলে লগইন পেজে পাঠানো হবে
