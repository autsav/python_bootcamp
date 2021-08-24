from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

# Create your views here.
def render_static(request):
    return render(request, 'static.html')

def manage_media(request):
    if request.method == 'POST':
        print("post data", request.POST)
        print("file", request.FILES)
        file_obj = request.FILES['myfile']

        print("my file name is: ", file_obj.name)
        fs = FileSystemStorage()
        filename = fs.save(file_obj.name, file_obj)

        file_url = fs.url(filename)
        print(" after save filename is ", filename)
        print("my file url is", file_url)




    return render(request, 'media.html')