from django.urls import path

from .views import *

urlpatterns = [
    path('post/backup/', create_backup),
]