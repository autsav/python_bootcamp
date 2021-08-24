from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.


def hello_templates(request):
    template = loader.get_template('hello.html')
    context = {
        'name': 'Utsab Adhikari',
    }
    template_data = template.render(context, request)
    return HttpResponse(template_data)

def hello_render(request):
    context = {
        'name':' Suraj Bista'
    }
    return render(request, "hello_render.html", context)

def hello_new(request):
    context = {
        'name':'Paridhi Subedi'
    }
    return render(request,"hello_new.html", context)