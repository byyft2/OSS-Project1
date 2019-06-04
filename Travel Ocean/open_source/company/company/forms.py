from django import forms

from .models import Continent_blog

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Continent_blog
        fields = ('title',
                  'content', 'continent',
                  'country', 'hashtag',
                  'start_at', 'comeback_at')
        