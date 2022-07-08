from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Post
from django.db.models.query import QuerySet
from datetime import datetime
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


from django.http import HttpResponse
from django.shortcuts import render
from .models import Post, Contact, SiteInfo
from .forms import *

# Create your views here.
# def index(request):
#     all_post = Post.objects.all()
#     print(all_post)
#     return HttpResponse(f"{all_post[0].description}, {all_post[0].title}, <br><h3>{all_post[0].img}</h3>")


# def summury(request):
#     a = 5
#     b = 4
#     return HttpResponse(f"a + b")



# Create your views here.
def index(request):
    all_post = Post.objects.filter(is_draft=False, is_delete=False)
    contacts = Contact.objects.filter(is_active=True)
    site_info = SiteInfo.objects.filter(is_active=True).first()
    context = {
        "all_posts": all_post,
        "contacts": contacts,
        "site_info": site_info,
    }
    return render(
        request=request,
        template_name='vlog_app/index.html',
        context=context
        )
    
    
# Model View Controller
# Model Template View
    
    
    
def post_detail(request, post_id):
    
    contacts = Contact.objects.filter(is_active=True)
    
    site_info = SiteInfo.objects.filter(is_active=True).first()
        
    post = get_object_or_404(Post, id=post_id, is_draft=False, is_delete=False)
    # post = Post.objects.get(id=post_id)
    
    context = {
        "post": post,
        "contacts": contacts,
        "site_info": site_info,
    }
    
    return render(
        request=request,
        template_name="vlog_app/post-detail.html",
        context=context
    )
    
    
def create_post(request):
    
    form = CreatePostForm()
    
    context = {
        "form": form
    }
    
    if request.method == "POST":
        form = CreatePostForm(request.POST, request.Files)
        if form.is_valid():
            form.save(user_id=request.user.id)
            return redirect('/')
        
        
    return render(
        request=request,
        template_name='vlog_app/post-create.html',
        context=context
    )
    
    
def registration(request):
    
    form = UserCreationForm() 
    contacts = Contact.objects.filter(is_active=True)
    site_info = SiteInfo.objects.filter(is_active=True).first()
    
    context = {
        "form": form,
        "contacts": contacts,
        "site_info": site_info,
    }
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(
                request=request,
                user=user
            )
            return redirect('/')
    
    return render(
        request=request,
        template_name='registration/sing_up.html',
        context=context
    )
    

def edit_post(request, post_id):
    post = get_object_or_404(
        Post, 
        pk=post_id, 
        user__id=request.user.id, 
        is_delete=False
        )
    form = EditPostForm(
        instance=post
    )
    
    contacts = Contact.objects.filter(is_active=True)
    site_info = SiteInfo.objects.filter(is_active=True).first()
        

    context = {
        "form": form,
        "contacts": contacts,
        "site_info": site_info,
    }
    
    if request.method == "POST":
        # form = EditPostForm(request.POST or None, request.FILES or None)
        # if form.is_valid():
        #     cd = form.cleaned_data
        #     post.title = cd['title']
        #     post.img = cd['img'] if cd['img'] else post.img
        #     post.description = cd['description']
        #     post.is_draft = cd['is_draft']
        #     post.is_delete = cd['is_delete']
        #     post.save
        #     return redirect('/')
        form = EditPostForm(
            request.POST,
            request.FILES,
            instance=post
        )
        
        if form.is_valid():
            form.save()
            return redirect('/')
        
    return render(
        request=request,
        template_name='vlog_app/post-edit.html',
        context=context
    )