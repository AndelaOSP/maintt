from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model

from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.views import APIView

from api.models import UserProfile
from api.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows users to be viewed or edited
    '''
    queryset = UserProfile.objects.all().order_by('-created_at')
    serializer_class = UserSerializer


class CreateUserView(CreateAPIView):

    model = get_user_model()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = UserSerializer


class LoginView(APIView):

    def post(self, *args, **kwargs):
        username = self.request.POST['username']
        password = self.request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            login(self.request, user)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=403)


class Logout(APIView):

    def get(self, request, format=None):
        logout(request)
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
