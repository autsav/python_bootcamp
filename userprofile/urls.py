from django import urls
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import home
from django.contrib import admin
from django.contrib.admin.sites import site

# from .views import list_all_over,detail_view_of_users,create_user_info,update_user_info,delete_user_info

app_name = 'crud'
urlpatterns = [
    # path('list/', list_all_over,name='list'),
    # path('detail/<int:user_id>/', detail_view_of_users,name='detail'),
    path('admin', admin.site.urls),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='login.html'), name='logout'),
    path('', home,name='login'),



]
