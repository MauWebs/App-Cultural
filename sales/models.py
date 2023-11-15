from django.db import models

from users.models import User


class Sales(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    products = models.JSONField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_sold = models.DateTimeField(auto_now_add=True)