from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.MyTokenObtainPairView.as_view()),
    path('register/', views.register),
    path('register/admin/', views.registerAdmin),
    path('register/editor/', views.registerEditor),
    path('put/', views.putUser),
    path('profile/', views.getUserProfile),
    path('<int:pk>/', views.getSoloUser),
    path('get/all/', views.getUsers),
]