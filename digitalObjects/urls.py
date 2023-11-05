from django.urls import path

from .views import *

urlpatterns = [
    
       # -------------- DigitalObject -------------- #

       # POST
       path('post/', postDigitalObject),
       # DELETE
       path('delete/<int:pk>/', deleteDigitalObject),
       # GET
       path('get/all/', getAllDigitalObjects),
       path('get/<int:pk>/', getIdDigitalObjects),
       # PUT
       path('put/<int:pk>/', putDigitalObject),

       # ------------------ Rating ------------------ #

       # POST
       path('post/rating/<int:pk>/', postRating),

       # ------------------ Comment ------------------ #

       # POST
       path('post/<int:pk>/comment/', postComment),
       # DELETE
       path('delete/comment/<int:pk>/', deleteComment),

]