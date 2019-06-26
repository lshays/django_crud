from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Person
from datetime import date

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
        
        response = c.get('/crud/')
        self.assertEqual(response.status_code, 200)
        
        response = c.get('/crud/create/')
        self.assertEqual(response.status_code, 200)
        
        response = c.get('/crud/search/')
        self.assertEqual(response.status_code, 200)

class ModelTests(TestCase):

    def test_create_record(self):
        Person.objects.create(name="testname", date="2019-06-26", number=1)
        self.assertEqual(len(Person.objects.all()), 1)
        self.assertEqual(Person.objects.get(id=1).name, "testname")
        self.assertEqual(Person.objects.get(id=1).date, date(2019,6,26))
        self.assertEqual(Person.objects.get(id=1).number, 1)
