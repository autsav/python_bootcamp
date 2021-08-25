from django.forms import models
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView

from .form import UserInfoModelForm
from .models import UserInfo
from django.urls import reverse_lazy

class Create(CreateView):
    form_class = UserInfoModelForm
    template_name = 'classbased/create.html'
    # success_url='/c/list/'
    success_url = reverse_lazy('classbased:list')

class List(ListView):
    template_name = 'classbased/list.html'
    model = UserInfo
    context_object_name = 'data'

class Detail(DetailView):
    template_name = 'classbased/detail.html'
    model = UserInfo
    pk_url_kwarg = 'id'
    context_object_name = 'user_obj'



class Delete(DeleteView):
    model = UserInfo
    success_url = reverse_lazy("classbased:list")   

class Update(UpdateView):
    form_class = UserInfoModelForm
    template_name = 'classbased/update.html'
    model = UserInfo
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('classbased:list')

    def form_valid(self, form):
        print("form is valid")
        return super().form_valid(form)

