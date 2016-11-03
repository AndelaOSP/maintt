from api.models import UserProfile
from rest_framework import viewsets, status
from rest_framework.response import Response

from api.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows users to be viewed or edited
    '''
    queryset = UserProfile.objects.all().order_by('-created_at')
    serializer_class = UserSerializer


#############
# ADMIN API #
#############
class AdminUserAPI(viewsets.ViewSet):
    """ API endpoint that allows admin user
        to manage administrators
    """
    def list(self, *args, **kwargs):
        return Response({'yo': 'asdjasjdas'}, status=200)

    def create_staff(self, *args, **kwargs):
        serializer = UserSerializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save(is_staff=True)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def login_staff(self, *args, **kwargs):
        test