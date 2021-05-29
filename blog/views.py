from django.core.files.base import ContentFile
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import CommentForm, PostcreationForm, PassForm
from .models import Comment, Post
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from . utils import randompassword
# Create your views here.

def blog(request):
    posts = Post.objects.all().order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})



def new_post(request):

    if request.method == 'POST':
        form = PostcreationForm(request.POST, request.FILES)
        # password = 000000
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            password = randompassword()
            while(True):
                try:
                    x = Post.objects.get(password=password)
                except Post.DoesNotExist:
                    x = None
                if x:
                    password = randompassword()
                else:
                    instance.password = password
                    print(password)
                    break
            instance.publish()
            return redirect('blog')
        else:
            return render(request, 'blog/new_post.html', {'form':form})
    else:
        form = PostcreationForm()
    return render(request, 'blog/new_post.html', {'form': form})



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

def passpage(request):
    form =PassForm()
    if request.method == "POST":
        form = PassForm(request.POST)
        if form.is_valid():
            passw = form.cleaned_data.get('password')
            try:
                x = Post.objects.get(password=passw)
            except Post.DoesNotExist:
                x = None
            if x:
                id = x.pk
                return redirect('action', pk=id)
            else:
                messages.error(request,"Credential is wrong")
        else:
            return render(request,'blog/postpass.html',{'form':form})
    context = {
        'form':form,
    }
    return render(request,'blog/postpass.html',context)

def action(request, pk):
    obj = Post.objects.get(pk=pk)
    context = {
        'ob':obj,
    }
    return render(request, 'blog/action.html',context)

def delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('blog')

def edit(request, pk):
    post = Post.objects.get(pk=pk)
    form = PostcreationForm(instance=post)
    if request.method == 'POST':
        form = PostcreationForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.password = post.password
            instance.pk = post.pk
            instance.save()
            return redirect('detail', pk=pk)
    else:
        return render(request, 'blog/post_edit.html', {'form': form})
