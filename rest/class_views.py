from datetime import time
from decimal import Context
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Info
# from .serializers import InfoSerializer
from .serializers import InfoModelSerializer

from rest_framework import status
from django.utils import timezone


class InfoClassBasedViews(APIView):

    def get(self, request, *args, **kwargs):
        qs = Info.objects.all()
        # print(qs)
        serializer = InfoModelSerializer(instance=qs, many=True)
        return Response(serializer.data)
        
    def post(self, request, *args, **kwargs):
        current_time = timezone.now()
        print("Current Time", current_time)
        context = {
            'current_time':current_time
        }

        serializer = InfoModelSerializer(data=request.data, context=context)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # return Response({'status': 'ok post', 'result':serializers.data}, status=201)
        return Response({'status': 'ok post', 'result':serializer.data}, status=status.HTTP_201_CREATED)

