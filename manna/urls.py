"""mrdc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from .views import ProjectListView,ProjectDetailView
from . import views

urlpatterns = [
    path('',views.home , name='manna-home'),
    path('what_we_do/', ProjectListView.as_view(), name='manna-what_we_do'),
    path('project/<pk>', ProjectDetailView.as_view(), name='project-detail'),
    path('get_in_touch/', views.get_in_touch, name='manna-get_in_touch'),
    path('how_you_can_help/', views.how_you_can_help,name='manna-how_you_can_help'),
]
