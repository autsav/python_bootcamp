from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from .serializers import AddTwoNumberSerializer
# from django.shortcuts import render

# Create your views here.
@csrf_exempt
def add_two_numbers(request):
    if request.method == 'GET':
        return JsonResponse({'message':'Welcome to add two numbers'})

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        print("requestPOST->",request.POST)
        print("data->",data)

        serializers = AddTwoNumberSerializer(data=data)
        if serializers.is_valid():
            number1 = serializers.validated_data['number1']
            number2 = serializers.validated_data['number2']
            result = number1 + number2
            return JsonResponse({'result': result})
        else:
            print('down')
            print(serializers.errors)
            return JsonResponse({'error':'Something went wrong'}, status=400)