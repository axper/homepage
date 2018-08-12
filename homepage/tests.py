from django.test import TestCase


class HomepageTests(TestCase):
    def test_root_url(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Welcome')
