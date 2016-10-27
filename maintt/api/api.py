from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from django.conf import settings

from .serializers import UserSerializer
from .models import UserProfile


class SignUpAPI(ViewSet):

    serializer_class = UserSerializer
    def signup(self, *args, **kwargs)
  
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            user = UserProfile.objects.get(username=serializer.data['username'])
            user.backend = settings.AUTHENTICATION_BACKENDS[0]
            login(self.request, user)
            
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)