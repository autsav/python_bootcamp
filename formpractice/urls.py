from django.urls import path

from .views import forms_home,django_form,django_model_form,new_form


urlpatterns = [
    path('home', forms_home),
    path('django-home',django_form),
    path('django-model-home',django_model_form),
    path('my-form',new_form),

]
 