from django.contrib.auth.models import User

from django.test import TestCase
from django.test.client import RequestFactory
from faker import Faker

from api.models import UserProfile
from api.serializers import UserSerializer

fake = Faker()

# fixtures
user1 = {
    'username': fake.user_name(),
    'first_name': fake.first_name(),
    'last_name': fake.last_name(),
    'email': fake.email(),
    'password': fake.password(),
    'is_staff': 1
}

class SampleTestCase(TestCase):

    def setUp(self):
        '''Prep. steps come here
        '''
        User.objects.create_user(**user1)

    def test_get_request(self):
        '''
        Tests response for a simple get request
        '''
        user = User.objects.get(username=user1['username'])
        profile = UserProfile.objects.get(user_id=user.id)
        context = dict(request=RequestFactory().get('/'))
        serializer = UserSerializer(profile, context=context)
        user_data = serializer.data

        self.assertEqual(user_data['username'], user1['username'])
        self.assertEqual(user_data['first_name'], user1['first_name'])
        self.assertEqual(user_data['last_name'], user1['last_name'])
        self.assertEqual(user_data['email'], user1['email'])
        self.assertEqual(user_data['is_staff'], user1['is_staff'])
        # get ID on the URL and compare
        self.assertEqual(int(user_data['url'].split('/')[-2]), int(user.id))
        