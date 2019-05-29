from django import forms

from .models import Blog
from .models import Comment

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'content','image')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message']