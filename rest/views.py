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

        serializer = AddTwoNumberSerializer(data=data)
        if serializers.is_valid():
            number1 = serializer.validated_data['number1']
            number2 = serializer.validated_data['number2']
            result = number1 + number2
            return JsonResponse({'result': result})
        else:
            print('down')
            print(serializer.errors)
            return JsonResponse({'error':'Something went wrong'}, status=400)


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import renderer_classes,parser_classes

@api_view(['GET', 'POST'])
@parser_classes([JSONParser])
def add_two_numbers_in_rest(request):
    if request.method == 'GET':
        return Response({'message':'Welcome to add two numbers'})

    elif request.method == 'POST':
        # data = JSONParser().parse(request)
        # print("requestPOST->",request.POST)
        # print("data->",data)

        # serializer = AddTwoNumberSerializer(data=request.data)
        # print(serializers)
        # if serializers.is_valid():
        #     number1 = serializer.validated_data['number1']
        #     number2 = serializer.validated_data['number2']
        #     result = number1 + number2
        #     return Response({'result': result})
       
        # print('down')
        # print(serializer.errors)
        # return Response({'error':'Something went wrong'}, status=400)
        serializer = AddTwoNumberSerializer(data=request.data)
        print(serializers)
        
        serializers.is_valid(raise_exception=True)
        number1 = serializer.validated_data['number1']
        number2 = serializer.validated_data['number2']
        result = number1 + number2
        return Response({'result': result})
       
        # print('down')
        # print(serializer.errors)
        # return Response({'error':'Something went wrong'}, status=400)