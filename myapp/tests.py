from django.test import SimpleTestCase
class SimpleTests(SimpleTestCase):
    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    def test_about(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code,200)
    