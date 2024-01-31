from django.test import TestCase, Client, RequestFactory

# Create your tests here.
from .models import Publisher
from django.contrib.auth.models import User, AnonymousUser

from .views import greeting_view_user

class TestPublisherModel(TestCase):
    """Test the Publisher Model"""
    def setUp(self):
        self.p = Publisher(name='Packt', website ='www.packt.com', email ='contact@packt.com')
        
    def test_create_publisher(self):
        self.assertIsInstance(self.p, Publisher)
        
    def test_str_representation(self):
        self.assertEquals(str(self.p), "Packt")
        
class TestGreetingView(TestCase):
    """Test the Greeting View"""
    def setUp(self):
        self.client = Client()

    def test_greeting_view(self):
        response = self.client.get('/test/greeting')
        self.assertEquals(response.status_code,200)
        
class TestLoggedInGreetingView(TestCase):
    """Test the greeting view for the authenticated users."""
    def setUp(self):
        self.test_user =User.objects.create_user(username ='alice',password ='examplepass1')
        self.test_user.save()
        self.factory =RequestFactory()

    def test_user_greeting_not_authenticated(self):
        request =self.factory.get('/test/greet_user')
        request.user = AnonymousUser()
        response =greeting_view_user(request)
        self.assertEquals(response.status_code, 302)
        
    def test_user_authenticated(self):
        request = self.factory.get('/test/greet_user')
        request.user = self.test_user
        response = greeting_view_user(request)
        self.assertEquals(response.status_code, 200)
        
        
        