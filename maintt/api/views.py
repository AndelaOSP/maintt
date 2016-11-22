from api.models import UserProfile, Issue
from rest_framework import viewsets
from rest_framework.decorators import list_route
from api.serializers import UserSerializer, IssueSerializer
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows users to be viewed or edited
    '''
    queryset = UserProfile.objects.all().order_by('-created_at')
    serializer_class = UserSerializer


class IssuesViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows issues to be viewed or edited
    '''
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

    @list_route()
    def all_issues(self, request):
        all_issues = Issue.objects.all().order('-created_at')

        page = self.paginate_queryset(all_issues)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(all_issues, many=True)
        return Response(serializer.data)
