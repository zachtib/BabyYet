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
