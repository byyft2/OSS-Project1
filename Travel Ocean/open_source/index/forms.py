from django import forms

from .models import Blog
from .models import Comment
from .models import User

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'content','image')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message']
        
class updateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'name', 'phone', 'birth', 'email')

