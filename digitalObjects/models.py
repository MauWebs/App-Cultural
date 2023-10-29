from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone

from users.models import User

# --------------------------------------------------------------------------- #

class DigitalObject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    start_date = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=300)
    place = models.CharField(max_length=150)
    format = models.CharField(max_length=20)
    tag = models.CharField(max_length=200)
    url = models.URLField()

# --------------------------------------------------------------------------- #

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    digital_object = models.ForeignKey(
        DigitalObject, on_delete=models.CASCADE, null=True)
    rating_value = models.PositiveIntegerField(
        default=None, validators=[MinValueValidator(0), MaxValueValidator(6)])

# --------------------------------------------------------------------------- #

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    digital_object =  models.ForeignKey(DigitalObject, on_delete=models.CASCADE, null=False)
    start_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(max_length=300)