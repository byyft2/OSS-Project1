from django.shortcuts import render, redirect

# Create your views here.
def europe(request):
    return render(request, 'europe.html')

def german(request):
    return render(request, 'german.html')