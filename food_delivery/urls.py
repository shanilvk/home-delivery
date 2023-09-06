"""
URL configuration for food_delivery project.

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
from account import views
from django.conf import settings
from django.conf.urls.static import static
from account.views import signupview,signinview
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',signinview.as_view(),name='signin'),
    path('signup',signupview.as_view(),name='signup'),
    path('home',views.index,name='index'),
    path('contact/',views.contact_us,name='contact'),
    path('about/',views.about,name='about'),
    path('menu/',views.menu,name='menu'),
    path('booking/',views.booking,name='booking'),
    path('veg/',views.vegetarian,name='veg'),
    path('nonveg/',views.nonvegetarian,name='nonveg'),
    path('beve/',views.beverage,name='beve'),
    path('customer/',include('customer.urls'))
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
