from django.test import TestCase
from django.urls import reverse
from .models import Room, Topic, Message, User

# Create your tests here.

class YourAppViewsTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword'
        )

        # Create a test topic
        self.topic = Topic.objects.create(name='Test Topic')

        # Create a test room
        self.room = Room.objects.create(
            host=self.user,
            topic=self.topic,
            name='Test Room',
            description='Test Room Description'
        )

        # Create a test message
        self.message = Message.objects.create(
            user=self.user,
            room=self.room,
            body='Test Message'
        )

    def test_user_registration(self):
        response = self.client.post(reverse('register'), {
            'name': 'Test User',
            'username': 'testuser2',
            'email': 'testuser2@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword'
        })
        self.assertEqual(response.status_code, 302)  

    def test_login_view(self):
        response = self.client.post(reverse('login'), {
            'email': 'testuser@example.com',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 302)  

    def test_logout_view(self):
        self.client.login(email='testuser@example.com', password='testpassword')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)  
    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)  