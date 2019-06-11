from django.shortcuts import render, redirect

# Create your views here.
def europe(request):
    return render(request, 'europe.html')

def europe_germany(request):
    return render(request, 'europe_germany.html')

def europe_france(request):
    return render(request, 'europe_france.html')

def asia(request):
    return render(request, 'asia.html')

def asia_japan(request):
    return render(request, 'asia_japan.html')

def asia_singapore(request):
    return render(request, 'asia_singapore.html')

def N_america(request):
    return render(request, 'N_america.html')

def N_america_usa(request):
    return render(request, 'N_america_usa.html')

def N_america_canada(request):
    return render(request, 'N_america_canada.html')