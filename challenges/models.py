from django.contrib.auth.models import User
from django.db import models


class Challenge(models.Model):
    title = models.TextField()
    description = models.TextField()
    created_by_user = models.ForeignKey(User, null=True, blank=True)

    def __str__(self):
        return self.title
