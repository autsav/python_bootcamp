from .views import login_view, profile_view
from django.urls import path
# from django.views import View


app_name = 'accounts'
urlpatterns = [
    path('login/', login_view, name="login"),
    path('profile/', profile_view, name="profile"),
]
