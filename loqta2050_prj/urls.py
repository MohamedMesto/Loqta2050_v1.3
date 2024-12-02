"""
URL configuration for loqta2050_prj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from blog2050.views import blog2050_func
from home.views import home_func
from aboutus.views import aboutus_func

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_func, name='home_func'),
    path('blog2050/', blog2050_func, name='blog2050_func'),
    path('aboutus/',aboutus_func,name='aboutus_func')

]
