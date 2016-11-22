from django.contrib.auth.models import User
from api.models import UserProfile, Issue
from rest_framework.response import Response
from django.http import Http404
from rest_framework import serializers, status


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
        fields = (
            'url', 'username', 'first_name', 'last_name', 'email', 'is_staff',
            'created_at', 'updated_at', 'password'
        )

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


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ('state', 'user', 'title', 'description', 'created_at')

    @staticmethod
    def create(validated_data):
        issue = Issue.objects.create(**validated_data)
        return issue

    @staticmethod
    def update(instance, validated_data):
        try:
            instance.state = validated_data.get('state', instance.state)
            instance.user = validated_data.get('user', instance.user)
            instance.title = validated_data.get('title', instance.title)
            instance.description = validated_data.get('description', instance.description)
            instance.created_at = validated_data.get('created_at', instance.created_at)
            return instance
        except instance.DoesNotExist:
            raise Http404

    def check_issue_exist(self, id):
        try:
            return Issue.objects.get(id=id)
        except Issue.DoesNotExist:
            raise Http404

    def delete(self, instance, format=None):
        issue = self.check_issue_exist(item_id=instance.id)
        issue.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
