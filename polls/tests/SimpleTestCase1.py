from django.test import SimpleTestCase
from django.urls import reverse

class HomePageTest(SimpleTestCase):

    def test_home_page_status_code(self):
        response = reverse('polls:index')
        self.assertEqual(response, '/polls/')

