from django import forms

from .models import Continent_blog
from .models import Continent_Comment

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Continent_blog
        fields = ('title',
                  'content', 'continent',
                  'country', 'hashtag',
                  'start_at', 'comeback_at')
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Continent_Comment
        fields = ['message']