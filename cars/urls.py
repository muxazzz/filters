"""cars URL Configuration

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
from cars_libr.views import (CarListView, CarView, RegisterView, CreateUserProfile, index, )
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CarListView.as_view()),
    path('in', index, name='index'),
    path('cars/', CarListView.as_view()),
    path('cars/<str:pk>/', CarView.as_view()),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),  
    path('logout/', LogoutView.as_view(), name='logout'),  
    path('register/', RegisterView.as_view(  
        template_name='register.html',  
		success_url='127.0.0.1/profile-create'  
    ), name='register'),  
    path('profile-create/', CreateUserProfile.as_view(), name='profile-create'),  
]
