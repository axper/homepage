from django.test import TestCase


class HomepageTests(TestCase):
    def test_root_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Babken')

    def test_django_admin_url(self):
        response = self.client.get('/django-admin/')
        self.assertRedirects(response, '/django-admin/login/?next=/django-admin/')

    def test_wagtail_admin_url(self):
        response = self.client.get('/wagtail-admin/')
        self.assertRedirects(response, '/wagtail-admin/login/?next=/wagtail-admin/')
