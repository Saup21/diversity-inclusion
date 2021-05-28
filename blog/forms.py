from django import forms
from .models import Post

# Necessary forms:

class PostcreationForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'text', 'image']
