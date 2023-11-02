from django.urls import path

from .views import *

urlpatterns = [
    path('post/', postContact),
    path('get/all/', getAllContact),
    path('get/<int:pk>/', getIdContact),
    path('delete/<int:pk>/', deleteIdContact),
]