from django.urls import path

from .import views

urlpatterns = [
    path('europe/', views.europe, name="europe"),
    path('europe/german', views.german, name="german"),
]