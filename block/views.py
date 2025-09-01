from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from block.models import Category,Blogs,Comment
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .forms import RegisterFrom,CommentForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout


from django.contrib.auth.decorators import login_required
from account_profile.models import Profile
from account_profile.forms import ProfileForm


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



from .forms import CommentForm

from django.shortcuts import get_object_or_404, redirect
from .forms import CommentForm
from .models import Blogs, Comment

def blogs(request, slug):
    single_post = get_object_or_404(Blogs, slug=slug, status='published')
    comments = Comment.objects.filter(blog=single_post)
    comment_count = comments.count()
    
    # POST handle
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = request.user  
            new_comment.blog = single_post
            new_comment.save()
            return redirect('blogs', slug=single_post.slug) 
    else:
        form = CommentForm()
    
    context = {
        'single_post': single_post,
        'comments': comments,
        'comment_count': comment_count,
        'form': form,
    }
    return render(request, 'blogs.html', context)



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
            return redirect('login')
        
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
            return redirect('dashboard:dashboard')
        
    else:
        form = AuthenticationForm()
    
    return render(request,'login.html',{'form':form})

def Logout_view(request):
    logout(request)
    return redirect('home')
       

# accounts/views.py
@login_required
def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
        
            return redirect('profile_view')  
    else:
        form = ProfileForm()

    context = {'form': form, 'profile': profile}
    return render(request, 'profile/profile.html', context)


@login_required
def update_profile(request):
   
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_view')  
    else:
        form = ProfileForm(instance=profile)  

    context = {'form': form, 'profile': profile}
    return render(request, 'profile/update_profile.html', context)


