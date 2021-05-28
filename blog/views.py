from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import PostcreationForm
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
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
