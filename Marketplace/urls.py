"""Marketplace URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import include, re_path
from marketplace.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index_view),
    path('bussiness_home/',index_view),
    path('bussiness_signup/',bussiness_signup),
    path('bussiness_signin/',bussiness_signin),
    
    path('bussiness_signup/bussiness_signin/',bussiness_signin),
    path('bussiness_signin/bussiness_signup/bussiness_base/',bussiness_base), 
    path("bussiness_signin/bussiness_base/",bussiness_base),
    path("bussiness_signin/bussiness_signup/bussiness_signin",bussiness_signin),
    path("bussiness_signup/bussiness_signin/bussiness_base/",bussiness_base),       
    re_path(r'^bussiness_signin/bussiness_signup/bussiness_signin/$', bussiness_signin),    
    re_path(r'^bussiness_signin/bussiness_signup/$', bussiness_signup),    #working
    
      path('customer_home/',customer_home),
    # path('bussiness_signin/',bussiness_signin),
    # path('customer_landing/',customer_landing),
    path('customer_signin/customer_home/',customer_home),
    path('customer_signup/',customer_signup,name="sign up"),
    path('customer_signin/',customer_signin,name="log in"),
    path('customer_signup/customer_signin/',customer_signin),
    path('customer_signin/customer_signup/customer_signin',customer_signin),
    path('customer_signup/customer_signin/customer_home/',customer_home),
    path('customer_signin/customer_signup/customer_home/',customer_home),
    path('customer_signin/customer_home',customer_home),
    path('customer_signin/customer_signup/',customer_signup),
    re_path('customer_signin/customer_signup/customer_signin/',customer_home),
    re_path(r'^customer_signin$', customer_signin),
    re_path(r'^customer_signup/$', customer_signup),
    path("customer_signin/", include("django.contrib.auth.urls")),
    path('customer_signin/', LoginView.as_view(template_name='customer/registration/login/login.html')),
     path('accounts/', include('django.contrib.auth.urls')),
    
    re_path('^expertise_signin/expertise_base/expertise_portforlio/',expertise_portforlio),
    path('expertise_signup/',expertise_signup),
     path('expertise_signin/expertise_signup/',expertise_signup),
    path('expertise_signin/',expertise_signin),
    path('expertise_signup/expertise_signin/',expertise_signin),
    path('expertise_signin/expertise_base/',expertise_base),
    path('expertise_signin/expertise_signup/expertise_signin/expertise_base/',expertise_base),
    path('expertise_signin/expertise_signup/expertise_signin/',expertise_signin),
    path('expertise_signup/expertise_signin/expertise_portforlio/',expertise_portforlio),

    path('events_home/',index_view),
    path('event_detail/',index_view),


    path('customer_signin/news_home/',news_home),
    path('customer_signin/customer_signup/customer_home/news_home/',news_home),
    path('customer_signin/customer_home/news_home/',news_home),
    path('customer_signin/customer_home/news_home/news_detail/',news_detail),
    
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
