from django.urls import path

from .views import *

urlpatterns = [
    
       # -------------- History -------------- #

       # POST
       path('post/', postHistory),
       # DELETE
       path('delete/<int:pk>/', deleteHistory),
       # GET
       path('get/all/', getAllHistory),

]