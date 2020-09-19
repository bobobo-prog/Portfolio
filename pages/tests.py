from django.http import request
from django.test import SimpleTestCase

class SimpleTests(SimpleTestCase):

    def homepage_up(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code,200)



