from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from .forms import RegistrationForm, PostcreationForm
# from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def blog(request):
    return render(request, 'blog/post_list.html', {})
