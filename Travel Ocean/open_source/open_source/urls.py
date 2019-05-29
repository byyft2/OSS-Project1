"""open_source URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import index.views
from django.conf import settings
from django.conf.urls.static import static
import continent.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index.views.main, name="main"),
    path('signup/', index.views.signup, name="signup"),
    path('signout/', index.views.signout, name="signout"),
    path('find/', index.views.find, name="find"),
    path('create/', index.views.create, name="create"),
    path('free_borad/', index.views.free_borad, name="free_borad"),
    path('free_borad_delete/<int:id>', index.views.free_borad_delete, name="free_borad_delete"),
    path('free_borad_update/<int:id>', index.views.free_borad_update, name="free_borad_update"),
    path('free_borad_detail/<int:id>', index.views.free_borad_detail, name="free_borad_detail"),
    path('free_comment_create/<int:id>', index.views.free_comment_create, name="free_comment_create"),
    path('free_comment_update/<int:id>', index.views.free_comment_update, name="free_comment_update"),
    path('free_comment_delete/<int:id>', index.views.free_comment_delete, name="free_comment_delete"),
    path('continent/', include("continent.urls")),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)