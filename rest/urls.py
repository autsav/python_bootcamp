from django.urls import path
from .views import add_two_numbers

urlpatterns = [
    path('add/', add_two_numbers)
]
