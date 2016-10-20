from django.test import TestCase
from faker import Faker

from django.contrib.auth.models import User
from api.models import UserProfile

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

class UserProfileTestCase(TestCase):
    '''
    Test cases for the UserProfile model that has a
    1-to-1 relation with the ~auth.models.User model
    '''

    def setUp(self):
        '''
        Setup pre-conditions for the tests
        '''
        # create one user, this should trigger creation of
        # a UserProfile model instance
        User.objects.create_user(**user1)

    def test_user_created(self):
        '''
        Tests if user is successfully created
        '''
        user = User.objects.get(username=user1['username'])
        self.assertEqual(user.username, user1['username'])
        self.assertEqual(user.first_name, user1['first_name'])
        self.assertEqual(user.last_name, user1['last_name'])
        self.assertEqual(user.email, user1['email'])
        self.assertEqual(user.is_staff, user1['is_staff'])
        self.assertIsNotNone(user.id)
        # check if password has been hashed
        self.assertNotEqual(user.password, user1['password'])

    def test_user_profile_created(self):
        '''
        Tests if the hook is triggered for creating UserProfile
        once a User is created
        '''
        user = User.objects.get(username=user1['username'])
        profile = UserProfile.objects.get(user=user)
        self.assertEqual(profile.user_id, user.id)
        self.assertIsNotNone(profile.created_at)
        self.assertIsNotNone(profile.updated_at)

