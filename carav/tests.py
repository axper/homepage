from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from freezegun import freeze_time
from http import HTTPStatus

from carav import models


class WaterFountainModelTests(TestCase):
    @freeze_time('2018-08-13')
    def test(self):
        now = timezone.now()

        water_fountain = models.WaterFountain.objects.create(lat=1.2, lng=3.4)

        self.assertEqual(now, water_fountain.created)
        self.assertEqual(now, water_fountain.updated)
        self.assertEqual('WaterFountain #1 @1.2,3.4', str(water_fountain))
        self.assertFalse(water_fountain.deleted)


class CreateWaterFountainViewTests(TestCase):
    def test_request_not_post(self):
        response = self.client.get(reverse('carav:create_water_fountain'))

        self.assertEqual(HTTPStatus.METHOD_NOT_ALLOWED, response.status_code)

    def test_lat_not_in_request(self):
        response = self.client.post(reverse('carav:create_water_fountain'), data={'lng': 1})

        self.assertEqual(HTTPStatus.BAD_REQUEST, response.status_code)
        self.assertEqual(b'lat is required', response.content)

    def test_lng_not_in_request(self):
        response = self.client.post(reverse('carav:create_water_fountain'), data={'lat': 1})

        self.assertEqual(HTTPStatus.BAD_REQUEST, response.status_code)
        self.assertEqual(b'lng is required', response.content)

    def test_duplicate_lat_lng(self):
        models.WaterFountain.objects.create(lat=1.111, lng=2.222)

        response = self.client.post(reverse('carav:create_water_fountain'), data={'lat': 1.111, 'lng': 2.222})

        self.assertEqual(HTTPStatus.BAD_REQUEST, response.status_code)
        self.assertEqual(b'duplicate latitude and longitude', response.content)

    @freeze_time('2018-08-13')
    def test(self):
        now = timezone.now()

        response = self.client.post(reverse('carav:create_water_fountain'), data={'lat': 2.334, 'lng': 5.6678})

        self.assertEqual(HTTPStatus.OK, response.status_code)
        self.assertEqual(1, models.WaterFountain.objects.count())
        water_fountain = models.WaterFountain.objects.get()
        self.assertEqual(1, water_fountain.id)
        self.assertEqual(2.334, water_fountain.lat)
        self.assertEqual(5.6678, water_fountain.lng)
        self.assertEqual(now, water_fountain.created)
        self.assertEqual(now, water_fountain.updated)


class AllWaterFountainsViewTests(TestCase):
    def test_request_not_get(self):
        response = self.client.post(reverse('carav:all_water_fountains'))

        self.assertEqual(HTTPStatus.METHOD_NOT_ALLOWED, response.status_code)

    def test(self):
        models.WaterFountain.objects.create(lat=1, lng=2)
        models.WaterFountain.objects.create(lat=3, lng=4)
        models.WaterFountain.objects.create(lat=5, lng=6, deleted=True)

        response = self.client.get(reverse('carav:all_water_fountains'))

        self.assertEqual(HTTPStatus.OK, response.status_code)
        self.assertEqual([{'lat': 1.0, 'lng': 2.0, 'id': 1}, {'lat': 3.0, 'lng': 4.0, 'id': 2}],
                         response.json()['data'])


class DeleteWaterFountainViewTests(TestCase):
    def test_request_not_post(self):
        response = self.client.get(reverse('carav:delete_water_fountain'))

        self.assertEqual(HTTPStatus.METHOD_NOT_ALLOWED, response.status_code)

    def test_no_id(self):
        response = self.client.post(reverse('carav:delete_water_fountain'))

        self.assertEqual(HTTPStatus.BAD_REQUEST, response.status_code)
        self.assertEqual(b'id is required', response.content)

    def test_does_not_exist(self):
        response = self.client.post(reverse('carav:delete_water_fountain'), {'id': 0})

        self.assertEqual(HTTPStatus.BAD_REQUEST, response.status_code)
        self.assertEqual(b'water fountain with id 0 does not exist', response.content)

    def test_already_deleted(self):
        water_fountain = models.WaterFountain.objects.create(lat=1, lng=2, deleted=True)

        response = self.client.post(reverse('carav:delete_water_fountain'), {'id': water_fountain.id})

        self.assertEqual(HTTPStatus.BAD_REQUEST, response.status_code)
        self.assertEqual(b'already deleted', response.content)

    def test(self):
        water_fountain = models.WaterFountain.objects.create(lat=1, lng=2)

        response = self.client.post(reverse('carav:delete_water_fountain'), {'id': water_fountain.id})

        self.assertEqual(HTTPStatus.OK, response.status_code)
        water_fountain = models.WaterFountain.objects.get()
        self.assertTrue(water_fountain.deleted)


class UpdateWaterFountainTests(TestCase):
    def test_request_not_post(self):
        response = self.client.get(reverse('carav:update_water_fountain'))

        self.assertEqual(HTTPStatus.METHOD_NOT_ALLOWED, response.status_code)

    def test_no_id(self):
        response = self.client.post(reverse('carav:update_water_fountain'))

        self.assertEqual(HTTPStatus.BAD_REQUEST, response.status_code)
        self.assertEqual(b'id is required', response.content)

    def test_no_lat(self):
        response = self.client.post(reverse('carav:update_water_fountain'), {'id': 1})

        self.assertEqual(HTTPStatus.BAD_REQUEST, response.status_code)
        self.assertEqual(b'lat is required', response.content)

    def test_no_lng(self):
        response = self.client.post(reverse('carav:update_water_fountain'), {'id': 1, 'lat': 1})

        self.assertEqual(HTTPStatus.BAD_REQUEST, response.status_code)
        self.assertEqual(b'lng is required', response.content)

    def test_does_not_exist(self):
        response = self.client.post(reverse('carav:update_water_fountain'), {'id': 1, 'lat': 1, 'lng': 1})

        self.assertEqual(HTTPStatus.BAD_REQUEST, response.status_code)
        self.assertEqual(b'water fountain with id 1 does not exist', response.content)

    def test(self):
        models.WaterFountain.objects.create(lat=1, lng=1)

        response = self.client.post(reverse('carav:update_water_fountain'), {'id': 1, 'lat': 2, 'lng': 3})

        self.assertEqual(HTTPStatus.OK, response.status_code)
        water_fountain = models.WaterFountain.objects.get()
        self.assertEqual(2, water_fountain.lat)
        self.assertEqual(3, water_fountain.lng)
