from rest_framework import serializers
from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter

from django_filters.rest_framework import DjangoFilterBackend

from .serializers import InfoModelSerializer
from .models import Info
from .pagination import MyLimitOffsetPagination


class InfoModelCreateAPIView(CreateAPIView):
    

    def perform_create(self, serializer):
        serializer.save()
        print("ok the serilizer is saved")

        
class InfoModelListAPIView(ListAPIView):
    serializer_class = InfoModelSerializer
    pagination_class = MyLimitOffsetPagination
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]

    search_fields = ['name']
    order_fields = ['name', 'id']
    filterset_fields = ['name','address']
    # authentication_classes = [TokenAuthentication, ]
    # permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        # return super().get_queryset()(self):
        return Info.objects.all()

class InfoModelDestroyAPIView(DestroyAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoModelSerializer
    
class InfoModelUpdateAPIView(UpdateAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoModelSerializer

class InfoModelRetrieveAPIView(RetrieveAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoModelSerializer