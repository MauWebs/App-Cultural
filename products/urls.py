from django.urls import path

from .views import *

urlpatterns = [
    path('post/', postProduct),
    path('get/all/', getAllProduct),
    path('delete/<int:pk>/', deleteProduct),
]