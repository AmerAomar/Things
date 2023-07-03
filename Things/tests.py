from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Thing


# Create your tests here.

class ThingTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser1', password='pass')
        testuser1.save()

        test_thing = Thing.objects.create(Thing_name='chair', user_name=testuser1, description="test desc ...")
        test_thing.save()

    def test_thing_model(self):
        thing = Thing.objects.get(id=1)
        user = get_user_model().objects.get(id=1)
        self.assertEqual(thing.Thing_name, 'chair')
        self.assertEqual(thing.user_name, user)
        self.assertEqual(thing.description, 'test desc ...')
