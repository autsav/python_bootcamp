from django.shortcuts import redirect, render , get_object_or_404, redirect
from .models import UserInfo
from .form import UserInfoModelForm
# Create your views here.
def list_all_over(request):
    data = UserInfo.objects.all()
    context = {
        'data':data
    }
    return render(request, 'crud/list.html', context=context)

def detail_view_of_users(request, user_id):
    # user_obj = UserInfo.objects.get(id=user_id)
    user_obj = get_object_or_404(UserInfo, id=user_id)

    # print(user_obj)
    return render(request, 'crud/detail.html',context= {
        'user_obj': user_obj
    })

def create_user_info(request):
    if request.method == 'POST':
        form = UserInfoModelForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)           
            print("form is valid")
            form.save()
            return redirect('/crud/list/')
        else:
            print("form is invalid")
    else:
        form = UserInfoModelForm()
        #form process
    return render(request, 'crud/create.html',{
        'form':form
    })


def update_user_info(request, user_id):
    user_object = get_object_or_404(UserInfo, id=user_id)
    if request.method == 'POST':
        form = UserInfoModelForm(request.POST, instance=user_object)
        if form.is_valid():
            print(form.cleaned_data)           
            print("form is valid")
            form.save()
            return redirect(f'/crud/detail/{user_id}')
        else:
            print("form is invalid")
    else:
        form = UserInfoModelForm(instance=user_object)
        #form process
    return render(request, 'crud/update.html',{
        'form':form
    })

def delete_user_info(request, user_id):
    user_object = get_object_or_404(UserInfo, id=user_id)

    user_object.delete()
    return redirect(f'/crud/list/')