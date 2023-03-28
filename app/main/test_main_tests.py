from django.contrib.auth.models import User
from django.test import TestCase
from main.models import Memory
from django.test import Client


# launch all tests with `python manage.py test`
class TestMemoryModel(TestCase):
    """Test case for memory model"""

    def setUp(self):
        """Set up the test"""
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()

    def testLoginRedirection(self):
        """Test that login redirects to the home page"""
        c = Client()
        response = c.post('/accounts/login/', {'login': 'testuser', 'password': '12345'})
        self.assertEqual(response.status_code, 302)

    def testIndexPageOpen(self):
        """Logged-in user opens index page"""
        c = Client()
        user = User.objects.get(username="testuser")
        c.force_login(user)
        response = c.get('')
        self.assertEqual(response.status_code, 200)

    def testUserPageOpen(self):
        """Logged-in user opens user page"""
        c = Client()
        user = User.objects.get(username="testuser")
        c.force_login(user)
        response = c.get('/places/')
        self.assertEqual(response.status_code, 200)

    def testAddMemoryPageOpen(self):
        """Logged-in user opens Add memory page"""
        c = Client()
        user = User.objects.get(username="testuser")
        c.force_login(user)
        response = c.get('/add_memory/')
        self.assertEqual(response.status_code, 200)

    def testUpdatePageOpen(self):
        """Logged-in user opens update memory page"""
        c = Client()
        user = User.objects.get(username="testuser")
        c.force_login(user)
        Memory.objects.create(place='django',
                              owner=User.objects.get(username='testuser'),
                              slug='django',
                              latitude=1,
                              longitude=2,
                              text='some test text',
                              photo='photos/default.png', )

        response = c.get('/update_memory/django/1/')
        self.assertEqual(response.status_code, 200)

    def testDeletePageOpen(self):
        """Logged in user opens Delete memory page"""
        c = Client()
        user = User.objects.get(username="testuser")
        c.force_login(user)
        Memory.objects.create(place='django',
                              owner=User.objects.get(username='testuser'),
                              slug='django',
                              latitude=1,
                              longitude=2,
                              text='some test text',
                              photo='photos/default.png', )

        response = c.get('/delete_memory/django/1/')
        self.assertEqual(response.status_code, 200)

    def testIndexPageOpenLoggedOut(self):
        """LoggedOut user opens index page"""
        c = Client()
        response = c.post('')
        self.assertEqual(response.status_code, 200)

    def testUserPageOpenLoggedOut(self):
        """LoggedOut user opens user page"""
        c = Client()
        user = User.objects.get(username="testuser")
        c.force_login(user)
        response = c.get('/places/')
        self.assertEqual(response.status_code, 200)

    def testAddMemoryPageOpenLoggedOut(self):
        """LoggedOut user opens Add memory page"""
        c = Client()
        response = c.get('/add_memory/')
        self.assertEqual(response.status_code, 302)

    def testUpdatePageOpenLoggedOut(self):
        """LoggedOut user opens update memory page"""
        c = Client()
        response = c.get('/update_memory/django/1/')
        self.assertEqual(response.status_code, 302)

    def testDeletePageOpenLoggedOut(self):
        """LoggedOut user opens Delete memory page"""
        c = Client()
        response = c.get('/delete_memory/django/1/')
        self.assertEqual(response.status_code, 302)

    def testMemoryCreation(self):
        """Logged-in user creates a memory"""
        c = Client()
        user = User.objects.get(username="testuser")
        c.force_login(user)
        Memory.objects.create(place='django',
                              owner=User.objects.get(username='testuser'),
                              slug='django',
                              latitude=1,
                              longitude=2,
                              text='some test text',
                              photo='photos/default.png', )
        self.assertTrue(Memory.objects.get(place='django'))
