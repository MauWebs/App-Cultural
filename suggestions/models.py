from django.db import models


class Suggestions(models.Model):
    description = models.TextField(max_length=300)    
