from django.db import models


class Contacts(models.Model):
    name = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    email = models.EmailField()
    web = models.URLField(blank=True)
    matter = models.CharField(max_length=50)
    consultation = models.CharField(max_length=100)
    message = models.TextField(max_length=500)