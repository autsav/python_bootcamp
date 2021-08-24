from django import forms
from django.forms import fields
from .models import FormsModel

class MyForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField(max_value=100)
    email = forms.EmailField()
    age = forms.RadioSelect()

    def clean_name(self):
        print("I am from form", self.cleaned_data)
        name = self.cleaned_data['name']

        return name.lower()

    def clean_email(self):
        print("I am from form", self.cleaned_data)
        email = self.cleaned_data['email']

        
        return email

class FormsModelForm(forms.ModelForm):
    class Meta:
        model = FormsModel
        fields = ['name','email','username']
