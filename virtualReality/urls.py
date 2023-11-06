from django.urls import path

from .views import *

urlpatterns = [
    path('post/', postVirtualReality),
    path('delete/<int:pk>/', deleteVirtualReality)
]