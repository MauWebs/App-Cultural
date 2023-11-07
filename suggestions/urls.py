from django.urls import path

from .views import *

urlpatterns = [
    path('post/', postSuggestion),
    path('get/all/', getAllSuggestions),
    path('get/<int:pk>/', getSuggestion),
]