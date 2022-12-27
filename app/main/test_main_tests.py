from django.contrib.auth.models import User
from django.test import TestCase
from main.models import Memory
from django.test import Client


class TestMemoryModel(TestCase):

    def test_setup(self):
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()

    def test_LoginRedirection(self):
        c = Client()
        response = c.post('/accounts/login/', {'login': 'testuser', 'password': '12345'})
        self.assertEqual(response.status_code, 302)

    def test_IndexPageOpen(self):
        """Logged in user opens index page"""
        c = Client()
        user = User.objects.get(username="testuser")
        c.force_login(user)
        response = c.get('')
        self.assertEqual(response.status_code, 200)

    def test_UserPageOpen(self):
        """Logged in user opens user page"""
        c = Client()
        user = User.objects.get(username="testuser")
        c.force_login(user)
        response = c.get('/places/')
        self.assertEqual(response.status_code, 200)

    def test_AddMemoryPageOpen(self):
        """Logged in user opens Add memory page"""
        c = Client()
        user = User.objects.get(username="testuser")
        c.force_login(user)
        response = c.get('/add_memory/')
        self.assertEqual(response.status_code, 200)

    def test_UpdatePageOpen(self):
        """Logged in user opens update memory page"""
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

    def test_DeletePageOpen(self):
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

    def test_IndexPageOpenLoggedOut(self):
        """LoggedOut user opens index page"""
        c = Client()
        response = c.post('')
        self.assertEqual(response.status_code, 200)

    def test_UserPageOpenLoggedOut(self):
        """LoggedOut user opens user page"""
        c = Client()
        user = User.objects.get(username="testuser")
        c.force_login(user)
        response = c.get('/places/')
        self.assertEqual(response.status_code, 200)

    def test_AddMemoryPageOpenLoggedOut(self):
        """LoggedOut user opens Add memory page"""
        c = Client()
        response = c.get('/add_memory/')
        self.assertEqual(response.status_code, 302)

    def test_UpdatePageOpenLoggedOut(self):
        """LoggedOut user opens update memory page"""
        c = Client()
        response = c.get('/update_memory/django/1/')
        self.assertEqual(response.status_code, 302)

    def test_DeletePageOpenLoggedOut(self):
        """LoggedOut user opens Delete memory page"""
        c = Client()
        response = c.get('/delete_memory/django/1/')
        self.assertEqual(response.status_code, 302)

    def test_MemoryCreation(self):
        """Logged in user creates a memory"""
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

