from django.contrib import admin
from .models import Continent, Continent_blog, Continent_Comment
# Register your models here.
admin.site.register(Continent)
admin.site.register(Continent_blog)
admin.site.register(Continent_Comment)