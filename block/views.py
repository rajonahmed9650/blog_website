from django.shortcuts import render,redirect
from django.http import HttpResponse
from block.models import Category,Blogs
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .forms import RegisterFrom
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout


# Create your views here.

def home(request):
    # return HttpResponse("Education For Nation")
    categories = Category.objects.all()
    featured_post = Blogs.objects.filter(is_feacherd =True,)
    posts = Blogs.objects.filter(is_feacherd =False,status = 'published')
   
    context = {
        'categories':categories,
        'featured_post':featured_post,
        'posts':posts
    }
    return render(request,'home.html',context)


def posts_by_category(request, category_id):
    posts = Blogs.objects.filter(status='published', category=category_id)
    try:
        category = Category.objects.get(pk = category_id)
    except:
        return redirect('home')   

    # category = get_object_or_404(Category,pk=category_id) 
    context = {
        'posts':posts,
        'category' : category
    }
    return render(request,'posts_by_category.html',context)



def blogs(request,slug):
    single_post = get_object_or_404(Blogs,slug=slug,status ='published')
    context={
        'single_post':single_post
    }
    return render(request,'blogs.html',context)

def Search(request):
    keyword = request.GET.get('keyword')
    # blogs = Blogs.objects.filter(title__icontains = keyword) টাইটেলে যে সব কি-ওর্য়াড থাকবে সে অনুয়াযী সার্চ করবে । 
    blogs = Blogs.objects.filter(Q(title__icontains = keyword) | Q(short_description__icontains = keyword) | Q(blog_body__icontains = keyword),status = 'published')
    context = {
        'blogs':blogs,
        'keyword':keyword
    }
    return render(request,'search.html',context)


def register(request):

    if request.method == "POST":
        form = RegisterFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
        
    else:    
        form = RegisterFrom()
    context = {
        'form': form
    }
    return render(request,'register.html',context)


def Login_view(request):
    
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)  
            return redirect('dashboard')
        
    else:
        form = AuthenticationForm()
    
    return render(request,'login.html',{'form':form})

def Logout_view(request):
    logout(request)
    return redirect('home')
       