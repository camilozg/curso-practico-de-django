from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User

# Create your tests here.


class ProfileTestCase(TestCase):
    def setUp(self):
        User.objects.create_user('test_user', 'test_user@test.com', 'djangopass')

    # El nombre de la prueba debe empezar con "test_"
    # Los test se ejecutan con el comando "python manage.py test registration"
    def test_profile_exists(self):
        exists = Profile.objects.filter(user__username='test_user').exists()
        self.assertEqual(exists, True)
