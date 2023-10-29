from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.MyTokenObtainPairView.as_view()),
    path('register/', views.register),
    path('put/', views.putUser),
    path('userProfile/', views.getUserProfile),
    path('<int:pk>/', views.getSoloUser),
    path('getUsers/', views.getUsers),
]