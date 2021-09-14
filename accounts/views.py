from accounts.forms import LoginForm
from django.shortcuts import redirect, render
# from accounts.forms import LoginForm
from .forms import LoginForm, SignUpForm
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from user.models import User
from django.urls import reverse_lazy
from django.http import HttpResponse

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        
        # print('login view')
        print(request.POST)
        form = LoginForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            user =  authenticate(username=form.cleaned_data['username'],
                                 password=form.cleaned_data['password'])
            if user:
                print("a user is found", user)
                login(request,user)
                return redirect('/accounts/profile')
            else:
                print("auth credentials do not match")
    elif request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/accounts/profile/')
        form = LoginForm()
        
    

    return render(request,'accounts/login.html',{'form': form})

@login_required(login_url='/accounts/login/')
#incase of login_url='', it takes login_url from settings
def profile_view(request):
    # if request.user.is_authenticated:
    #     pass
    # else:
    #     pass

    #this context is passed for statusapp
    from statusapp.models import StatusMessage
    # messages = StatusMessage.objects.filter(user= request.user)
    messages = StatusMessage.objects.filter(user_id= request.user.id)
    messages = StatusMessage.objects.all()
    # print(messages)
    return render(request,'accounts/profile.html',{
        'messages':messages
    })

def logout_view(request):
    logout(request)
    return redirect('/accounts/login/')

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            print(form.cleaned_data)
            # from django.contrib.auth.models import User
            

            user = User(
                username = form.cleaned_data['username'],
                first_name = form.cleaned_data['first_name'],
                last_name = form.cleaned_data['last_name'],
                email = form.cleaned_data['email'],
                password = form.cleaned_data['password'],
                confirm_password = form.cleaned_data['confirm_password'],
            )
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('/accounts/login/')
            
    elif request.method == 'GET':
        form = SignUpForm()

    return render(request, 'accounts/signup.html', {'form': form})