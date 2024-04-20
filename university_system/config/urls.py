"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from user.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="home"),
    path('login-enrollee/', login_enrollee, name='login_enrollee'),
    path('login-commission/', login_commission, name='login_commission'),
    path('signup/', signupuser, name='signup'),
    path('sign-out', sign_out, name='signout'),
    path('room/', room, name='room')
]
