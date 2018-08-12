from django.db import models
from django.utils import timezone


class WaterFountain(models.Model):
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)
    lat = models.FloatField('Latitude')
    lng = models.FloatField('Longitude')
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return 'WaterFountain #{} @{},{}'.format(self.id, self.lat, self.lng)
