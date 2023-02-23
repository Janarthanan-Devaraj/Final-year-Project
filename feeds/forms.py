from django import forms
from .models import Post
from django.core.files.storage import FileSystemStorage


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'slug','image', 'content')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title of the Blog'}),
            'slug': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Copy the title with no space and a hyphen in between'}),
            'content': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Content of the Blog'}),
        }