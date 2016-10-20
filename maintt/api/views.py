from api.models import UserProfile
from rest_framework import viewsets
from api.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows users to be viewed or edited
    '''
    queryset = UserProfile.objects.all().order_by('-created_at')
    serializer_class = UserSerializer
