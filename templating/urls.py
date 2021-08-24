from django.urls import path
from .views import hello_templates,hello_render,hello_new

urlpatterns = [
    path('hello/', hello_templates),
    path('hello_render/', hello_render),
    path('hello_new/', hello_new),


]
