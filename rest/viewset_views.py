from rest_framework.viewsets import ModelViewSet
#ReadOnlyViewSet enable only get method and retrieve through id 
from rest.models import Info
from rest.serializers import InfoModelSerializer

class InfoModelViewSet(ModelViewSet):
    serializer_class = InfoModelSerializer
    queryset = Info.objects.all()
    # we can overide create, update , delete all of those methods from here