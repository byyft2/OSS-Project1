from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    birth = models.CharField(max_length=10)

class Blog(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    image = models.ImageField(upload_to="images/blog/", blank=True) 
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-id']
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE,related_name='comments')
    message = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering=['-id']
        
    def __str__(self):
        return self.post.title


    

    