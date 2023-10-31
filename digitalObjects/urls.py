from django.urls import path

from .views import *

urlpatterns = [
       path('post/', postDigitalObject),
       path('get/all/', getAllDigitalObjects),
       path('put/<int:pk>/', putDigitalObject),
       path('get/<int:pk>/', getIdDigitalObjects),
       path('get/<int:pk>/comment/', postComment),
       path('post/rating/<int:pk>/', postRating),
]