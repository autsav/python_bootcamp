"""helloworld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django import urls
from django.contrib import admin
from django.contrib.admin.sites import site
from django.urls import path, register_converter, include
from world.views import home, profile, profile_json,int_converter_view,debug_request
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from userprofile import views as user_views
from django.views.generic import FormView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('profile/<str:username>/',profile),
    path('profile-json/<str:username>/',profile_json),
    path('path/<str:int_data>/',int_converter_view),
    path('debug/',debug_request),
    path('templates/',include('templating.urls')),
    path('forms/',include('formpractice.urls')),
    path('static-demo/',include('staticmedia.urls')),
    path('crud/',include('crud.urls', namespace='crud')),
    path('c/',include('classbased.urls', namespace='classbased')),
    path('userprofile/',include('userprofile.urls', namespace='userprofile')),
    path('rest/',include('rest.urls')),


    path('admin/',admin.site.urls),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('', user_views.home, name='home'),
    path('contact/',user_views.contact, name='contact'),
    path('accounts/',include('accounts.urls', namespace='accounts')),
    path('statusapp/',include('statusapp.urls', namespace='statusapp')),



    




]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    import debug_toolbar
    urlpatterns =[
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns