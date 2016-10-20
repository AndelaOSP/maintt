from django.contrib.auth.models import User
from api.models import UserProfile
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    '''
    UseSerializer, combines both User and UserProfile models
    '''
    username = serializers.CharField(source='user.username')
    email = serializers.CharField(source='user.email')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    password = serializers.CharField(source='user.password', write_only=True)
    is_staff = serializers.IntegerField(source='user.is_staff')

    class Meta:
        model = UserProfile
        fields = ('url', 'username', 'first_name', 'last_name', 'email', 'is_staff',
            'created_at', 'updated_at', 'password')

    @staticmethod
    def create(self, validated_data):
        '''
        Given a dictionary of deserialized field values, either update
        an existing model instance, or create a new model instance.
        '''
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        # the hook at the models then creates the UserProfile
        return UserProfile.objects.get(user=user)

    @staticmethod
    def update(self, instance, validated_data):
        '''
        Update a serialized User object
        '''
        # First, update the User
        user_data = validated_data.pop('user', None)
        for attr, value in user_data.items():
            setattr(instance.user, attr, value)
        # Then, update UserProfile
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance