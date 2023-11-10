from django.urls import path

from .views import *

urlpatterns = [
    path('post/', postVirtualReality),
    path('get/all/', getAllVirtualReality),
    path('delete/<int:pk>/', deleteVirtualReality),
    path('get/<int:pk>/noImg/', getIdVirtualRealityNoImg),
    path('get/<int:pk>/noUrl/',getIdVirtualRealityNoUrl)
]