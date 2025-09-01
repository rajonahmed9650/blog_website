from django.shortcuts import render,redirect
from django.http import HttpResponse
from block.models import Category,Blogs
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm,BlogsForm,AddUserForm,EditForm
from django.shortcuts import get_object_or_404
from django.template.defaultfilters import slugify
from accounts.models import CustomUser


# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    category_counts = Category.objects.all().count()
    blogs_counts = Blogs.objects.all().count()
    # print(category_counts)
    # print(blogs_counts)

    context = {
        'category_counts':category_counts,
        'blogs_counts':blogs_counts
    }
    return render(request,'dashboard/dashboard.html',context)



def categories(request):

    return render(request,'dashboard/categories.html')


def add_categories(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard:categories')
    form = CategoryForm()    
    context = {
        'form':form
    }
    return render(request,'dashboard/add_categories.html',context)



def edit_categories(request,pk):
    category = get_object_or_404(Category,pk = pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('dashboard:categories')
    form = CategoryForm(instance=category)
    context = {
        'form':form,
        'category' : category
    }

    return render(request, 'dashboard/edit_categories.html',context)

def delete_categories(request,pk):
    category = get_object_or_404(Category,pk=pk)
    category.delete()
    return redirect('dashboard:categories')


def posts(request):
    posts = Blogs.objects.all()
    context = {
        'posts':posts
    }
    return render(request,'dashboard/posts.html',context)


def add_new_posts(request):
    if request.method == "POST":
        form = BlogsForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            title = form.cleaned_data['title']
            post.slug = slugify(title)
            post.save()
            print('Success')
            return redirect('dashboard:posts')
        else :
            print(form.errors)    
    form = BlogsForm()
    context = {
        'form':form
    }
    return render(request,'dashboard/add_new_posts.html',context)


def delete_posts(request,pk):
    post = get_object_or_404(Blogs,pk=pk)
    post.delete()
    return redirect('dashboard:posts')


def update_posts(request,pk):
    post = get_object_or_404(Blogs,pk=pk)
    if request.method == 'POST':
        form = BlogsForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect('dashboard:posts')
    form = BlogsForm(instance=post)

    context = {
        'form' : form,
         'post': post
    } 
    return render(request,'dashboard/update_post.html',context)   



def users(request):
    users = CustomUser.objects.all()
    context = {
        'users':users
    }
    return render(request,'dashboard/users.html',context)



def add_users(request):
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashobard:users')
    form = AddUserForm()
    context = {
        'form':form
    }
    return render(request,'dashboard/add_users.html',context)



def update_users(request,pk):
    user = get_object_or_404(CustomUser,pk=pk)
    if request.method == 'POST':
        form = EditForm(request.POST, instance= user)
        if form.is_valid():
            form.save()
            return redirect('dashboard:users')
        else:
            print(form.errors)
    form = EditForm(instance = user )
    context = {
        'form':form,
        'user':user
    }    
    return render(request,'dashboard/update_users.html',context)


def delete_users(request,pk):
    user = get_object_or_404(CustomUser,pk = pk)
    user.delete()
    return redirect('dashboard:users')