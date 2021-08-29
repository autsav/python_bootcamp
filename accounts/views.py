from accounts.forms import LoginForm
from django.shortcuts import redirect, render
# from accounts.forms import LoginForm
from .forms import LoginForm
from django.contrib.auth import authenticate,login


# Create your views here.
def login_view(request):
    if request.method == 'POST':
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
        form = LoginForm()

    return render(request,'accounts/login.html',{'form': form})


def profile_view(request):
    if request.user.is_authenticated:
        pass
    else:
        pass
    return render(request,'accounts/profile.html')