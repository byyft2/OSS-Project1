from django.shortcuts import render,redirect, get_object_or_404, Http404
from .models import Continent, Continent_blog
from django.contrib.auth.decorators import login_required
from .forms import *
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


# Create your views here.
def companygogo(request):
    blogs = Continent_blog.objects.all()
    paginator = Paginator(blogs, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    list = request.GET.get("list")
    if list:
        blogs = blogs.filter(title=list)
    return render(request, "companytest.html", {'blogs':blogs, 'posts':posts})

def company_detail(request, id):
    blog = get_object_or_404(Continent_blog, pk=id)
    posts = Continent_Comment.objects.filter(post=blog.id)
    return render(request, "company_detail.html", {"blog":blog , "posts":posts})

@login_required
def company_delete(request,id):
    blog = get_object_or_404(Continent_blog, pk=id)
    if blog.author != request.user:
        return redirect("main")
    blog.delete()
    return redirect("companytest")

@login_required
def company_update(request,id):
    if request.method == "GET":
        blog = get_object_or_404(Continent_blog, pk=id)
        return render(request, "company_update.html",{"blog":blog})
    elif request.method == "POST":
        blog = get_object_or_404(Continent_blog, pk=id)
        blog.title = request.POST["title"]
        blog.content = request.POST["content"]
        blog.continent = request.POST["continent_name"]
        blog.country = request.POST["country"]
        blog.hashtag = request.POST["concept"]
        blog.start_at = request.POST["startday"]
        blog.comeback_at = request.POST["comebackday"]
        blog.save()
        return redirect("company_detail",id)
    return Http404()

@login_required
def company_comment_create(request, id):
    post=get_object_or_404(Continent_blog,pk=id)
    if request.method=='POST':
        Continent_Comment.objects.create(
            post=post,
            message=request.POST['message'],
            author=request.user
        )
        return redirect("company_detail",id)
    return render(request,'company_comment_create.html')

@login_required
def company_comment_delete(request, id):
    post=get_object_or_404(Continent_Comment, pk=id)
    if post.author!=request.user:
        return redirect("main")
    if request.method=='POST':
        post_pk=post.post.pk
        post.delete()
        return redirect("company_detail", id=post_pk)
    return render(request, "company_comment_delete.html", {"post": post})

@login_required
def company_comment_update(request, id):
    post=get_object_or_404(Continent_Comment, pk=id)   
    if post.author!=request.user:
        return redirect("main")
    if request.method=='POST':
        post.message=request.POST["message"]
        post_pk=post.post.pk
        post.save()
        return redirect("company_detail", id=post_pk)
    elif request.method == 'GET':
        return render(request, "company_comment_update.html", {"post": post})
    

def drawChart(request):
  #  continent_list = Continent.objects.order_by('-count')
 #   context = {'continent_list': continent_list}
    a = 3
    b = 3
    c = 4
    lista = [a, b, c]
    return render(request, 'companychart.html', {'aa': lista})

@login_required
def continentcreate(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        title = request.POST["title"]
        content = request.POST["content"]
        continent_name = request.POST["continent_name"]
        country = request.POST["country"]
        concept = request.POST["concept"]
        startday = request.POST["startday"]
        comebackday = request.POST["comebackday"]
        author = request.user
        #form = CompanyForm(request.POST)
        #sibal = Continent_blog.objects.create(title = title, content = content, continent = continent_name, country = country, hashtag = concept, start_at = startday, comeback_at = comebackday)
        #sibal.save()
        form = CompanyForm(request.POST)
        obj= Continent_blog(title = title, content = content, continent = continent_name, country = country, hashtag = concept, start_at = startday, comeback_at = comebackday, author = author)
        obj.save()
       # form.author=request.user
        #form.save()
        return redirect('companytest')
    elif request.method == 'POST':
        form = CompanyForm()
        return render(request, 'company_create.html', {'form': form})
       # continent = (title=title, content=content, continent_name=continenet_name, country=country, concept=concept, startday=startday, comebackday=comebackday)
       # continent.save()
        #if form.is_valid():
         #   title = 
          #  continent_blog = form.save(commit=False)
           # continent_blog.author = request.user
            #continent_blog.save()
            #return redirect('companygogo')
    #else:
     #   form = CompanyForm()

def continentcreatego(request):
    return render(request, 'company_create.html')

