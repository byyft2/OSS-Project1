from django.shortcuts import render,redirect
from .models import Continent, Continent_blog
from django.contrib.auth.decorators import login_required
from .forms import *
from django.core.paginator import Paginator

# Create your views here.
def companygogo(request):
    blogs = Continent_blog.objects.all()
    paginator = Paginator(blogs, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    list = request.GET.get("list")
    if list:
        blogs = blogs.filter(title=list)
    return render(request, "companytest.html", {'posts':blogs})

#def companydetail(request,id):
 #   blog = get_object_or_404(Continent_blog, pk=id)
  #  return render(request, "companydetail.html", {"blog":blog})

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
        title = request.POST["title"]
        content = request.POST["content"]
        continent_name = request.POST["continent_name"]
        country = request.POST["country"]
        concept = request.POST["concept"]
        startday = request.POST["startday"]
        comebackday = request.POST["comebackday"]
        form = CompanyForm(request.POST)
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
    return render(request, 'company_create.html', {'form': form})

def continentcreatego(request):
    return render(request, 'company_create.html')