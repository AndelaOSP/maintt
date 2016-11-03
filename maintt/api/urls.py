from django.conf.urls import include, url
from rest_framework import routers
from api import views

from .api import SignUpAPI

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^signup/$', SignUpAPI.as_view({
        'get': 'post',
    }), name="signup"),
]
