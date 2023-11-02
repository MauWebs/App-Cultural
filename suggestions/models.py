from django.db import models
from users.models import User

class Suggestions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    description = models.TextField(max_length=300)    
