"""myrecommendations URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path

from . import views
from django.conf.urls import url

urlpatterns = [
    path('news/country/<slug:country>/topic/<slug:topic>/language/<slug:language>/', views.details, name='details'),
    path('privacy', views.privacy, name='privacy'),
    path('', views.index, name='index'),
    path('news/api/<slug:country>/topic/<slug:topic>/language/<slug:language>/', views.api, name='api'),
    path('news/apiv2/<slug:country>/topic/<slug:topic>/language/<slug:language>/', views.apiv2, name='apiv2'),
]