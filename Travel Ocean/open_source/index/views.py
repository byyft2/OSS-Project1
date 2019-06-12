from django.shortcuts import render, redirect, get_object_or_404, Http404, HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from .models import User
from .models import Blog
from .models import Comment
from company.models import Continent_blog, Continent
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
            return render(request, "main.html",{"msg":"일치하는 회원정보가 없습니다."})
        auth.login(request, user)
    return redirect("main")

def package(request):
    return render(request, "package.html")

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
        pwlen = len(password)
        if len(birth[0:4]) == 0:
            return render(request, "signup.html",{"msg":"공백 입니다."})
        if User.objects.filter(username=username).exists():
            return render(request, "signup.html",{"msg":"이미 존재하는 ID입니다."})
        if is_blank(username, password, password_check, name, phone, birth, email):
            return render(request, "signup.html",{"msg":"공백 입니다."})
        if password != password_check:
            return render(request, "signup.html",{"pw_msg":"비빌번호가 일치하지않습니다."})
        if password == password_check and pwlen <8:
            return render(request, "signup.html",{"pw_msg":"비빌번호는 8자 이상으로 해야합니다."})
        if birthcheck > 2019 or birthcheck < 1920:
            return render(request, "signup.html",{"pw_msg":"음 연도가 잘못된것 같은데요?"})
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

def id_find(request):
    if request.method == "POST":
        name = request.POST["user"]
        email = request.POST["email"]
        if is_id_blank(name, email):
            return render(request, "id_find.html",{"msg":"공백 입니다."})
        realname = User.objects.filter(name=name , email = email)
        #realemail = User.objects.filter(email=email)
        namelength = len(realname)
        if namelength == 0:
            return render(request, "id_find.html",{"msg":"해당하는 정보가 없습니다."})
        users = User.objects.filter(name=name) and User.objects.filter(email=email)
        return render(request, "id_find.html",{"users":users})
    return render(request, "id_find.html")


def testgogo(request):
    if request.method == "POST":
        username = request.POST["userid"] 
        name = request.POST["user"]
        email = request.POST["email"]
        if is_pw_blank(username,name, email):
            return render(request, "password_find.html",{"msg":"공백 입니다."})
        #if sipal.username == username and sipal.name == name and sipal.email == email
        getID = User.objects.filter(username = username, name = name, email = email)
        #sibal1 = User.objects.filter()
        getIDlen = len(getID)
        if getIDlen>0:
            blog = User.objects.get(username=username , name=name , email=email)
            form = updateForm(instance=blog)
            return render(request, "change_user_test.html", {'form': form , "blog": blog})
        elif getIDlen == 0:
            return render(request, "password_find.html",{"msg":"일치하는 회원정보가 없습니다."})
        #try:
            #blog = User.objects.get(username=username , name=name , email=email)
        #except User.DoesNotExist:
            #msg = "{} 가 없습니다. ".format(username)
            #raise Http404(msg)
        form = updateForm(instance=blog)
        return render(request, "change_user_test.html", {'form': form , "blog": blog})
    return render(request, "password_find.html")

def testgogogo(request):
    if request.method == "POST":
        username = request.POST["username"]
        name = request.POST["name"]
        phone = request.POST["phone"]
        birth = request.POST["birth"]
        email = request.POST["email"]
        password = request.POST["pw1"]
        password_check = request.POST["pw2"]
        if is_blank(username, password, password_check, name, phone, birth, email):
            return render(request, "change_user_test.html",{"msg":"공백 입니다."})
        if password != password_check:
            return render(request, "change_user_test.html",{"pw_msg":"비빌번호가 일치하지않습니다."})
        queryset = User.objects.filter(username__exact=username)
        queryset.delete()
        sibal = User.objects.create_user(username = username, name = name, phone = phone, birth = birth, email = email, password = password )
        auth.login(request, sibal)
    return render(request, "main.html")

def testgogogogo(request):
    if request.method == "POST":
        sibal = request.user
        return HttpResponse(sibal)



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
    list = request.GET.get('list')
    if list:
        blogs = blogs.filter(title__contains = list)
    paginator = Paginator(blogs, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, "free_borad.html", {"blogs":blogs, "posts":posts})

def free_borad_detail(request, id):
    blog = get_object_or_404(Blog, pk=id)
    posts = Comment.objects.filter(post=blog.id)
    return render(request, "free_borad_detail.html", {"blog":blog, "posts":posts})

@login_required
def free_borad_delete(request,id):
    blog = get_object_or_404(Blog, pk=id)
    if blog.author != request.user:
        return redirect("main")
    if request.method == 'POST':
        blog.delete()
        return redirect("free_borad")
    return render(request, "free_borad_delete.html", {"blog": blog})

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
    if request.method=='POST':
        comment = Comment()
        comment.message = request.POST["message"]
        comment.post = get_object_or_404(Blog, pk=id)
        comment.author = request.user
        #if len(comment.message) == 0:
            #return redirect("free_borad_detail", comment.post.id, {"msg":"공백입니다."})
        # if is_msg_blank(comment.message):
        #     return render(request, "free_borad_detail.html",{"msg":"공백 입니다."})
        comment.save()        
        return redirect("free_borad_detail", comment.post.id)
        #return HttpResponse(len(comment.message))
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


def is_blank(id, pw, pw_check,user, phone, birth, email):
    if len(id) == 0 or len(pw) == 0 or len(pw_check) == 0 or len(user) == 0 or len(phone) == 0 or len(birth) == 0 or len(email) == 0:
        return True
    return False

def is_id_blank(user, email):
    if len(user) == 0  or len(email) == 0:
        return True
    return False

def is_pw_blank(username, user, email):
    if len(username) == 0 or len(user) == 0 or len(email) == 0:
        return True
    return False

def is_msg_blank(message):
    if len(message) == 0:
        return True
    return False

def update_user(request, id):
    user = get_object_or_404(User, pk=id)
    return render(request,"update_user.html",{"user":user})