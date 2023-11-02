from django.urls import path

from .views import *

urlpatterns = [
       path('post/', postDigitalObject),
       path('get/all/', getAllDigitalObjects),
       path('put/<int:pk>/', putDigitalObject),
       path('get/<int:pk>/', getIdDigitalObjects),
       path('post/rating/<int:pk>/', postRating),
       path('post/<int:pk>/comment/', postComment),
]