from django.urls import path

from .views import *

urlpatterns = [
       path('post/', postDigitalObject),
       path('getAll/', getAllDigitalObjects),
       path('getId/<int:pk>/', getIdDigitalObjects),
       path('getId/<int:pk>/comment/', postComment),
       path('postRating/<int:pk>/', postRating),
]