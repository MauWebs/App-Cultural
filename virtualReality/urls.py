from django.urls import path

from .views import *

urlpatterns = [
    path('post/', postVirtualReality),
    path('get/all/', getAllVirtualReality),
    path('get/<int:pk>/',getIdVirtualReality),
    path('delete/<int:pk>/', deleteVirtualReality),
    path('upload-image/<int:pk>/', uploadImage),
]