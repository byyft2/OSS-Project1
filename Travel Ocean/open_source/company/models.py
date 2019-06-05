from django.db import models
from index.models import *
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Continent(models.Model):
    name = models.CharField(max_length=30)
    count = models.IntegerField(default=0)
    
class Continent_blog(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    continent = models.CharField(max_length=30, null=False)
    country = models.CharField(max_length=30, null=False)
    hashtag = models.CharField(max_length=10, null=False)
    start_at = models.CharField(max_length=40, null=False)
    comeback_at = models.CharField(max_length=40, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Continent_Comment(models.Model):
    post = models.ForeignKey(Continent_blog, on_delete=models.CASCADE,related_name='comments')
    message = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering=['-id']
        
    def __str__(self):
        return self.post.title