from django.db import models
from django.utils import timezone

from users.models import User


class News(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=60)
    url = models.URLField(blank=True, null=True)
    start_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(max_length=300)