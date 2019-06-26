from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class LoginTests(TestCase):

    def test_login_enforced(self):
        c = Client()
        response = c.get('/crud/')
        self.assertRedirects(response, '/accounts/login/?next=/crud/')

        response = c.get('/crud/create/')
        self.assertRedirects(response, '/accounts/login/?next=/crud/create/')
        
        response = c.get('/crud/search/')
        self.assertRedirects(response, '/accounts/login/?next=/crud/search/')

    def test_login(self):
        user = User.objects.create_superuser('user', 'fake.email@gmail.com', '12345')
        c = Client()
        response = c.post('/accounts/login/', {'username' : 'user', 'password' : '12345'})
        self.assertEqual(response.url, "/accounts/profile/")

    def test_pages_reachable(self):
        user = User.objects.create_superuser('user', 'fake.email@gmail.com', '12345')
        c = Client()
        login = c.login(username='user', password='12345')
        self.assertTrue(login)