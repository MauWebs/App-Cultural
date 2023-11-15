from django.urls import path

from .views import *

urlpatterns = [
    path('post/', postSales),
    path('get/all/', getSales)
]