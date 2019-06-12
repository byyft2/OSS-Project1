from django.urls import path

from .import views

urlpatterns = [
    path('europe/', views.europe, name="europe"),
    path('europe/europe_germany', views.europe_germany, name="europe_germany"),
    path('europe/europe_france', views.europe_france, name="europe_france"),
    path('asia/', views.asia, name="asia"),
    path('asia/asia_japan', views.asia_japan, name="asia_japan"),
    path('asia/asia_singapore', views.asia_singapore, name="asia_singapore"),
    path('N_america/', views.N_america, name="N_america"),
    path('N_america/N_america_usa', views.N_america_usa, name="N_america_usa"),
    path('N_america/N_america_canada', views.N_america_canada, name="N_america_canada"),
]