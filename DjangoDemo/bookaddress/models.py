from django.conf import settings
from django.db import models


class Contact(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    phone_number = models.IntegerField()
    email = models.EmailField()
