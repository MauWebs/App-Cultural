from django.db import models
from django.utils import timezone

from users.models import User

# --------------------------------------------------------------------------- #

class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=300)
    start_date = models.DateTimeField(default=timezone.now)
    format = models.CharField(max_length=20)
    tag = models.CharField(max_length=200)
    url = models.URLField()

# --------------------------------------------------------------------------- #