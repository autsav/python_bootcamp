from django.shortcuts import render
from django.views import View
from django.http.response import HttpResponse
from django.views.generic import TemplateView
from django.views.generic import RedirectView


# Create your views here.
class FirstView(View):
    #get -->get()
    #post -->post()

    def get(self, request, *args, **kwargs):
        return HttpResponse("This is GET ")

    def post(self, request,*args, **kwargs):
        return HttpResponse("this is POST")


class FirstTemplate(TemplateView):
    template_name = 'classbased/template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['msg'] = "Hello from the views"
        print("context", context)
        return context

class FirstTemplateRedirect(RedirectView):
    url = '/c/template/'