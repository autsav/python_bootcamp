from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
#ReadOnlyViewSet enable only get method and retrieve through id 
from rest.models import Info
from rest.serializers import InfoModelSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest.permissions import IsStaffUser

class InfoModelViewSet(ModelViewSet):
    serializer_class = InfoModelSerializer
    queryset = Info.objects.all()
    authentication_classes = [TokenAuthentication, ]
    # permission_classes = [IsStaffUser, ] 
    # we can overide create, update , delete all of those methods from here
    def get_permissions(self):
        if self.action == 'create' or self.action == 'update' or self.action == 'destroy':
            permissions = [IsStaffUser]
        else:
            permissions = [IsAuthenticated]
        return [permission() for permission in permissions]