from django.urls import path

from .views import *

urlpatterns = [
       path('post/', postNew),
       path('put/<int:pk>/', putNew),
       path('delete/<int:pk>/', deleteNew),
       path('get/all/', getAllNews),
       path('get/<int:pk>/', getIdNew)
]