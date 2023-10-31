from django.urls import path

from . import views

urlpatterns = [
    path('post/login/', views.MyTokenObtainPairView.as_view()),
    path('post/register/', views.register),
    path('post/register/editor/', views.registerEditor),
    path('post/register/admin/', views.registerAdmin),
    path('put/', views.putUser),
    path('get/profile/', views.getUserProfile),
    path('get/<int:pk>/', views.getSoloUser),
    path('get/all/', views.getUsers),
]