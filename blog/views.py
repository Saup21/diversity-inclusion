from django.core.files.base import ContentFile
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import CommentForm, PostcreationForm
from .models import Comment, Post
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
# Create your views here.

def blog(request):
    posts = Post.objects.all().order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

@login_required(login_url='admin')
def new_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostcreationForm(request.POST, request.FILES)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.author = request.user
                instance.publish()
                return redirect('blog')
            else:
                return render(request, 'blog/new_post.html', {'form':form})
        else:
            form = PostcreationForm()
        return render(request, 'blog/new_post.html', {'form': form})
    else:
        return redirect('admin')

@login_required(login_url='admin')
def detailpost(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    comment = Comment.objects.filter(postconnect = post)
    context = {
        'post':post,
        'form':form,
        'comment':comment,

    }
    return render(request, 'blog/blog_detail.html',context)

@login_required(login_url='admin')
def comm(request, pk):
    form = CommentForm()
    context = {
        'form':form,
    }
    post = Post.objects.get(pk=pk)
    comment = Comment.objects.filter(postconnect=post).values()
    comm = list(comment)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            obj = Post.objects.get(pk=pk)
            instance  = form.save(commit=False)
            instance.postconnect = obj
            instance.publish()
            comment = Comment.objects.filter(postconnect=post).values()
            comm = list(comment)
            return JsonResponse({'status':1,'comment':comm})
        else:
            return JsonResponse({'status':0,'comment':comm})

    return render(request, 'blog/blog_detail.html',context)