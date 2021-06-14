from django.contrib.auth.models import User
from django.test import TestCase

from baby.models import Baby


class BabyTestCase(TestCase):

    def test_home_returns_ok(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_loading_home_creates_an_entry_if_none_exist(self):
        self.assertEqual(Baby.objects.count(), 0)
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Baby.objects.count(), 1)

    def test_baby_nope(self):
        Baby.objects.create(name='Gizmo', born=False)
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual('Nope.', response.context['answer'])

    def test_baby_yep(self):
        Baby.objects.create(name='Gremlin', born=True)
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual('Yep.', response.context['answer'])

    def test_api_nope(self):
        Baby.objects.create(name='Gizmo', born=False)
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, 200)
        json = response.json()
        self.assertEqual(json['born'], False)

    def test_api_yep(self):
        Baby.objects.create(name='Gremlin', born=True)
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, 200)
        json = response.json()
        self.assertEqual(json['born'], True)

    def test_signed_in_as_admin(self):
        user = User.objects.create(username='teddymog', is_staff=True)
        user.set_password('12345')
        user.save()

        Baby.objects.create(name='Gizmo', born=False)

        self.client.login(username='teddymog', password='12345')

        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual('Nope.', response.context['answer'])
        self.assertTrue(response.context['show_admin_link'])

    def test_signed_in_as_regular_user(self):
        user = User.objects.create(username='bashful')
        user.set_password('w00f')
        user.save()

        gizmo = Baby.objects.create(name='Gizmo', born=False)

        self.client.login(username='bashful', password='w00f')

        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual('Nope.', response.context['answer'])
        self.assertFalse(response.context['show_admin_link'])
        self.assertTrue('admin_link' not in response.context.keys())
