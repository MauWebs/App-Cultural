from django.db import models
from django.utils import timezone

from users.models import User

# --------------------------------------------------------------------------- #

class VirtualReality(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    start_date = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=300)
    place = models.CharField(max_length=150)
    format = models.CharField(max_length=20)
    tag = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media/', default='', blank='')
    url = url = models.URLField()

# --------------------------------------------------------------------------- #