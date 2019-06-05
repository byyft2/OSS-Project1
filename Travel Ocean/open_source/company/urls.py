from django.urls import path

from .import views

urlpatterns = [
    path('companytest/', views.companygogo, name="companytest"),
    path('continentcreatego/', views.continentcreatego, name="continentcreatego"),
    path('companyChart/', views.drawChart, name="drawChart"),
    path('continentcreate/', views.continentcreate, name="continentcreate"),
    path('company_detail/<int:id>', views.company_detail, name="company_detail"),
    path('company_delete/<int:id>', views.company_delete, name="company_delete"),
    path('company_update/<int:id>', views.company_update, name="company_update"),
    path('company_comment_create/<int:id>', views.company_comment_create, name="company_comment_create"),
    path('company_comment_delete/<int:id>', views.company_comment_delete, name="company_comment_delete"),
    path('company_comment_update/<int:id>', views.company_comment_update, name="company_comment_update"),
    #path('companydetail', views.companydetail, name="companydetail"),
    #path('companydetail/',views.companydetail,name="companydetail"),
]