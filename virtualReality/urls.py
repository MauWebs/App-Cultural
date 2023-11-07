from django.urls import path

from .views import *

urlpatterns = [
    path('post/', postVirtualReality),
    path('get/all/', getAllVirtualReality),
    path('delete/<int:pk>/', deleteVirtualReality)
]