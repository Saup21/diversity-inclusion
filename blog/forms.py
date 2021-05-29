from django import forms
from .models import Post, Comment

# Necessary forms:

class PostcreationForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Post
        fields = ['title', 'email', 'text', 'image']

    def __init__(self, *args, **kwargs):
        super(PostcreationForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget = forms.TextInput(attrs={'type':'text','class':'form-control','id':'title','placeholder':'Title.....'})
        self.fields['text'].widget = forms.Textarea(attrs={'type':'text','class':'form-control','id':'detail','placeholder':'Detail....'})
        self.fields['email'].widget = forms.EmailInput(attrs={'type':'text','class':'form-control','id':'email', 'name': 'email', 'placeholder':'Your Email.....'})
        # self.fields['image'].widget = forms.


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['comment']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['comment'].widget = forms.TextInput(attrs={'type':'text','name':'comment','class':'form-control','id':'comment','placeholder':'Comment....'})

class PassForm(forms.Form):
    password = forms.IntegerField()

    def __init__(self, *args, **kwargs):
        super(PassForm, self).__init__(*args, **kwargs)
        self.fields['password'].widget = forms.NumberInput(attrs={'type':'number','class':'form-control','placeholder':'Password....','id':'password','name':'password'})
