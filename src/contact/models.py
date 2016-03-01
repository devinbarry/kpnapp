from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    zip = models.CharField(max_length=20)
    city = models.CharField(max_length=255)
    image = models.URLField()
