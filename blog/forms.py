from django import forms
from .models import Post, Comment

# Necessary forms:

class PostcreationForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'text', 'image']


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['comment']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['comment'].widget = forms.TextInput(attrs={'type':'text','name':'comment','class':'form-control','id':'comment','placeholder':'Comment....'})
