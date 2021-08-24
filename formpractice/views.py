from django.http.response import HttpResponse
from django.shortcuts import render
from .forms import MyForm, FormsModelForm
from django.http import HttpResponse

# Create your views here.

def forms_home(request):
    if request.method == 'GET':
        return render(request, "formpractice/forms.html", {})
    else:
        print(request.POST)
        return HttpResponse("OKOK")


def new_form(request):
    if request.method == 'GET':
        return render(request, "formpractice/my_form.html", {})
    else:
        print(request.POST)
        return HttpResponse("very Ok")



def django_form(request):
    if request.method == 'GET':
        form = MyForm()
        return render(request, 'formpractice/django_form.html', {'form': form})
    else:
        form = MyForm(request.POST)
        if form.is_valid():
            print("after validation on views",form.cleaned_data)
            return HttpResponse("OK")
        else:
            return render(request, 'formpractice/django_form.html', {'form': form})

def django_model_form(request):
    if request.method == 'GET':
        form = FormsModelForm()
        return render(request, 'formpractice/django_model_form.html', {'form': form})
    else:
        form = FormsModelForm(request.POST)
        if form.is_valid():
            form.save()
            print("after validation on views",form.cleaned_data)
            return HttpResponse("OK")
        else:
            return render(request, 'formpractice/django_model_form.html', {'form': form})

# def new_form(request):
#     if request.method == 'GET':
#         form = MyForm()
#         return render(request, 'formpractice/django_form.html', {'form': form})
#     else:
#         form = MyForm(request.POST)
#         if form.is_valid():
#             print("after validation on views",form.cleaned_data)
#             return HttpResponse("OK")
#         else:
#             return render(request, 'formpractice/django_form.html', {'form': form})