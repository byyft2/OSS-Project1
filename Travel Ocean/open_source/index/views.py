from django.shortcuts import render, redirect, get_object_or_404, Http404
from django.contrib import auth
from django.contrib.auth.models import User
from .models import User
from .models import Blog
from .models import Comment
from .forms import *
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator



# Create your views here.
def main(request):
    if request.method == "GET":
        return render(request, "main.html")
    elif request.method == "POST":
        username = request.POST["userid"]
        password = request.POST["pw"]
        user = auth.authenticate(request, username=username, password=password)
        if user is None:
            return render(request, "main.html")
        auth.login(request, user)
    return redirect("main")

def signup(request):
    if request.method == "GET":
        return render(request, "signup.html")
    elif request.method == "POST":
        username = request.POST["userid"]
        password = request.POST["pw"]
        password_check = request.POST["pw_check"]
        name = request.POST["user"]
        phone = request.POST["phone"]
        birth = request.POST["birth"]
        email = request.POST["email"]
        if password != password_check:
            return render(request, "signup.html")
        user = User.objects.create_user(
            username=username, password=password, name=name,
            phone=phone, birth=birth, email=email)
        auth.login(request, user)
    return redirect("main")


def signout(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            auth.logout(request)
    return redirect("main")

def find(request):
    return render(request, "find.html")

@login_required
def create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog=form.save(commit=False)
            blog.author=request.user
            blog.save()
            return redirect('free_borad')
    else:
        form = BlogForm()
    return render(request, 'create.html', {'form': form})


def free_borad(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    list = request.GET.get("list")
    if list:
        blogs = blogs.filter(title=list)
    return render(request, "free_borad.html", {'posts':posts})

def free_borad_detail(request, id):
    blog = get_object_or_404(Blog, pk=id)
    posts = Comment.objects.filter(post=blog.id)
    return render(request, "free_borad_detail.html", {"blog":blog, "posts":posts})


@login_required
def free_borad_delete(request,id):
    blog = get_object_or_404(Blog, pk=id)
    if blog.author != request.user:
        return redirect("main")
    blog.delete()
    return redirect("free_borad")

@login_required
def free_borad_update(request,id):
    if request.method == "GET":
        blog = get_object_or_404(Blog, pk=id)
        form = BlogForm(instance=blog)
        return render(request, "free_borad_update.html",{"form":form, "blog":blog})
    elif request.method == "POST":
        blog = get_object_or_404(Blog, pk=id)
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            blog=form.save(commit=False)
            blog.author=request.user
            blog.save()
        return redirect("free_borad_detail",id)
    return Http404()

@login_required
def free_comment_create(request, id):
    post=get_object_or_404(Blog,pk=id)
    if post.author!=request.user:
        return redirect("main")
    if request.method=='POST':
        Comment.objects.create(
            post=post,
            message=request.POST['message'],
            author=request.user
        )
        return redirect("free_borad_detail",id)
    return render(request,'free_comment_create.html')
    

@login_required
def free_comment_update(request, id):
    post=get_object_or_404(Comment, pk=id)   
    if post.author!=request.user:
        return redirect("main")
    if request.method=='POST':
        post.message=request.POST["message"]
        post_pk=post.post.pk
        post.save()
        return redirect("free_borad_detail", id=post_pk)
    elif request.method == 'GET':
        return render(request, "free_comment_update.html", {"post": post})
    

@login_required
def free_comment_delete(request, id):
    post=get_object_or_404(Comment, pk=id)
    if post.author!=request.user:
        return redirect("main")
    if request.method=='POST':
        post_pk=post.post.pk
        post.delete()
        return redirect("free_borad_detail", id=post_pk)
    return render(request, "free_comment_delete.html", {"post": post})


