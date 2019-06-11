from django.shortcuts import render,redirect, get_object_or_404, Http404 ,HttpResponse
from .models import Continent, Continent_blog
from django.contrib.auth.decorators import login_required
from .forms import *
from django.core.paginator import Paginator


# Create your views here.
def companygogo(request):
    blogs = Continent_blog.objects.all()
    list = request.GET.get("list")
    CL = request.GET.get("countrylist")
    if list:
        blogs = blogs.filter(title__contains=list)
    if CL:
        blogs = blogs.filter(country__contains=CL)
    paginator = Paginator(blogs, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
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
        if blog.start_at > blog.comeback_at:
            return redirect("company_update",id)
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
        form = CompanyForm(request.POST)
        if startday > comebackday:
            return render(request, "company_create.html",{"msg":"도착일이 출발일보다 빠를수는 없습니다."})
        if len(title) < 1 or len(content) < 1:
            return render(request, "company_create.html",{"msg":"공백이 있으면 안됩니다.", "post": obj})
        if len(continent_name) < 1:
            return render(request, "company_create.html",{"msg":"대륙을 선택해주세요."})
        if len(country) < 1:
            return render(request, "company_create.html",{"msg":"나라를 선택해주세요."})
        if len(startday) < 1 or len(comebackday) < 1:
            return render(request, "company_create.html",{"msg":"날짜를 선택해주세요."})
        obj= Continent_blog(title = title, content = content, continent = continent_name, country = country, hashtag = concept, start_at = startday, comeback_at = comebackday, author = author)
        obj.save()
    elif request.method == 'POST':
        form = CompanyForm()
        return render(request, 'company_create.html', {'form': form})
    return redirect(companygogo)
       
@login_required
def continentcreatego(request):
    return render(request, 'company_create.html')

