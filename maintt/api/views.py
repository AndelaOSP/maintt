from api.models import UserProfile
from rest_framework import viewsets
from rest_framework import permissions, viewsets,status,views
from rest_framework.response import Response
from api.serializers import UserSerializer
from django.contrib.auth import authenticate,login,logout
from api.permissions import IsProfileOwner


class UserViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows users to be viewed or edited
    '''
    queryset = UserProfile.objects.all().order_by('-created_at')
    serializer_class = UserSerializer
    lookup_field = 'username'

    def get_permissions(self):

    	 #if the request is in safe methods to call dangerous methods i.e delete, update etc. then allow any, 
    	 #it means this user must be an authenticated one.

    	if self.request.method in permissions.SAFE_METHODS:
    		return(permissions.AllowAny(),)

    	#if the request is a post then just allow any user, any user can make or create a new profile

    	if self.request.method== 'POST':
    		return(permissions.AllowAny(),)

    	# see if user is authenticated and is the profile owner/

    	return(permissions.isAuthenticated(),IsAccountOwner(),)	

    def create(self,request):

    	serializer = self.serializer_class(data=request.data)

    	if serializer.is_valid():

    		#create a new user.
    		Account.objects.create_user(**serializer.validated_data)

    		#if its succesful return the data and throw a 201 response

    		return Response(serializer.validated_data,status.HTTP_201_CREATED)
        
        #else if its not successful return an error message and a 400 response.
    	return Response({
    		'response':'Account could not be created.'
    	},status=status.HTTP_400_BAD_REQUEST)	
    	
class LoginView(views.APIView):
	def post(self,request,format=None):

		#get the data that was posted

		data = request.data

		#retrive the individual attributes from the retrieved data object

		email = data.get('email',None)
		password =data.get('password',None)

		#authenticate the account

		profile =  authenticate(email=email,password=password)

		#if there is an existing account, first check to see if its active

		if profile is not None:
			if profile.is_active:

				#login the user if he/she posseses an active account
				login(request,profile)				

				serialized = UserSerializer(profile)

				#return the response data

				return Response(serialized.data)

			else:

				#user or password was not right, return a 401 and login error

				return Response({
					'response':'username or password invalid'
					},status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(views.APIView):

	#only authenticated users can log out ofcourse!
	permission_classes= (permissions.isAuthenticated,)

    #wire a logout() function to logout the user
	def post(self,request,format=None):
		logout(request)

		return Response({})

			


    	    	

