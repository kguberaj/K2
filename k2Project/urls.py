"""k2Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf.urls.static import static

from django.conf import settings
from k2app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('index/', views.index, name='index'),
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('message/', views.message, name='message'),
    path('rent/', views.rent, name='rent'),
    path('rent_form/', views.rent_form, name='rent_form'),
    path('login_user/', views.login_user, name='login_user'),
    path('register/', views.register, name='register'),

]
urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
