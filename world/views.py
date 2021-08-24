from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse

# Create your views here.

# def home(request):
#     response = HttpResponse()
#     response.content = """
#     <html>
#     <body>
#         <h1>Hello WOrld</h1>
#         <p>This is my first Awesome Web Application in Django</p>
#     </body>
#     </html>

#     """
#     return response

def home(request):
    return HttpResponse("hi from home")


def profile(request, username):
    data = {
        'ram':'Ram bahadur',
        'hari':'Hari Bahadur',
        'sita':'Sita Maya',
    }
    full_name = data.get(username)

    if not full_name:
        return HttpResponseNotFound("The username does not exits", status=404)
    
    # string_data = "Your name is : {}".format(username)
    string_data = f"Your name is : {full_name}"

    return HttpResponse(string_data)

def profile_json(r,username):
    data = {
        'ram':'Ram bahadur',
        'hari':'Hari Bahadur',
        'sita':'Sita Maya',
    }
    full_name = data.get(username)

    if not full_name:
        return HttpResponseNotFound("The username does not exits", status=404)
    
    # string_data = "Your name is : {}".format(username)
    dict_data = {
        'full_name': full_name
    }

    return JsonResponse(dict_data)

def int_converter_view(r,int_data):
    # int_data1 = int_data
    print("int data is:", int_data)
    print(type(int_data))
    # converted_data = int(int_data)
    try:
        _ = int(int_data)
    except ValueError:
        return HttpResponse(f"Something is wrong", status=404)

    return HttpResponse(f"OK Ok Ok:{int_data}")

def debug_request(request):
    print("Request Method", request.method)
    print("Request Scheme", request.scheme)
    print("Request Headers", request.headers)
    print("Request GET", request.GET)

    return HttpResponse("Hello from debug")
    