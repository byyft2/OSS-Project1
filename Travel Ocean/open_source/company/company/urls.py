from django.urls import path

from .import views

urlpatterns = [
    path('companytest/', views.companygogo, name="companytest"),
    path('continentcreatego/', views.continentcreatego, name="continentcreatego"),
    path('companyChart/', views.drawChart, name="drawChart"),
    path('continentcreate/', views.continentcreate, name="continentcreate"),
    #path('companydetail', views.companydetail, name="companydetail"),
    #path('companydetail/',views.companydetail,name="companydetail"),
]