from django.test import LiveServerTestCase
import requests


class LiveServerTest(LiveServerTestCase):

    def test_server_running(self):
        response = requests.get(self.live_server_url + "/polls/")
        self.assertEqual(response.status_code, 200)
        