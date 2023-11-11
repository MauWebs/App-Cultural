from django.db import models

from users.models import User

# --------------------------------------------------------------------------- #

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=35)
    description = models.TextField(max_length=300)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    url = models.URLField()

# --------------------------------------------------------------------------- #
