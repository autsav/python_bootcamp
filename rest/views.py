from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from .serializers import AddTwoNumberSerializer, InfoSerializer
# from django.shortcuts import render
from .models import Info
from .serializers import InfoSerializer
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
        
        serializer.is_valid(raise_exception=True)
        number1 = serializer.validated_data['number1']
        number2 = serializer.validated_data['number2']

        result = number1 + number2
        return Response({'result': result})
       
        # print('down')
        # print(serializer.errors)
        # return Response({'error':'Something went wrong'}, status=400)
@api_view(['GET','POST','PUT','DELETE'])
def info_view(request, pk=None):
    if request.method == 'GET':
  
        qs= Info.objects.all()
        # result = []
        # for i in qs:
        #     serializer = InfoSerializer(instance=i)
        #     result.append(serializer.data)
        serializer = InfoSerializer(instance=qs, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        
            
        serializer = InfoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # name = serializer.validated_data['name']
        # address = serializer.validated_data['address']
        # obj = Info.objects.create(
        #     name=name,
        #     address=address
        # )
        serializer.save()
        return Response({'status':'ok post', 'result':serializer.data})
    #to update
    elif request.method == 'PUT':
        try:
            obj =Info.objects.get(pk=pk)
        except Info.DoesNotExist:
            return Response({'error': 'Doesnt exists'}, status=404)

        serializer = InfoSerializer(data=request.data, instance=obj)
        serializer.is_valid(raise_exception=True)

        # name = serializer.validated_data['name']
        # address = serializer.validated_data['address']
        # obj.name=name
        # obj.address=address
        # obj.save()
        serializer.save()
        return Response({'status':'ok PUT','result':serializer.data})

    elif request.method == "DELETE":
        try:
            obj = Info.objects.get(pk=pk)
        except Info.DoesNotExist:
            return Response({'error': 'Doesnot exists'}, status=404)
        
        obj.delete()
        return Response({'status':'Ok Deleted'})