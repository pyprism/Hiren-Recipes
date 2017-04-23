from django.urls import resolve
from django.test import TestCase, TransactionTestCase
from django.contrib.auth.models import User
from django.test import Client
from .models import Recipe, CookedAt
from . import views
from freezegun import freeze_time
from django.core.files.uploadedfile import SimpleUploadedFile


class ModelTest(TransactionTestCase):
    reset_sequences = True

    def setUp(self):
        f = SimpleUploadedFile('image.jpg', b'xyz')
        recipe = Recipe(name='test', image=f)
        recipe.save()
        CookedAt.objects.create(date='2016-12-17', recipe=recipe, rating=5)

    def test_models_stored_correct_object(self):
        self.assertEqual(Recipe.objects.count(), 1)
        self.assertEqual(CookedAt.objects.count(), 1)

        recipes = Recipe.objects.all()
        self.assertEqual(recipes[0].name, 'test')


class LoginViewTest(TransactionTestCase):
    """
    Test for index/login view
    """
    reset_sequences = True

    def setUp(self):
        self.c = Client()
        self.user = User.objects.create_user('hiren', 'a@b.com', 'bunny')

    def test_view_returns_correct_template(self):
        response = self.c.get('/')
        self.assertTemplateUsed(response, 'login.html')

    def test_authenticated_user_redirect_to_the_app(self):
        self.c.login(username='hiren', password='bunny')
        response = self.c.get('/', follow=True)
        self.assertRedirects(response, '/recipes/')

    def test_redirect_for_unauthenticated_user_works(self):
        response = self.c.get('/recipes/')
        self.assertRedirects(response, '/?next=/recipes/')

    def test_redirect_works_for_bad_auth(self):
        response = self.c.post('/', {'username': 'hiren', 'password': 'bad pass'}, follow=True)
        self.assertRedirects(response, '/')

    def test_message_works_for_bad_auth(self):
        response = self.c.post('/', {'username': 'hiren', 'password': 'bad pass'}, follow=True)
        message = list(response.context.get('messages'))[0]
        self.assertEqual(message.message, 'Username/Password is not valid!')
        self.assertEqual(message.tags, 'error')

    def test_login_url_resolves_to_login_view(self):
        found = resolve('/')
        self.assertEqual(found.func, views.login)
