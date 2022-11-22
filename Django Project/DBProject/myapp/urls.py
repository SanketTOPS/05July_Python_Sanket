from django import views
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
   path('',views.index),
   path('showdata/',views.showdata,name='showdata'),
   path('deletedata/<int:stid>',views.deletedata),
   path('updatedata/<int:stid>',views.updatedata),
]
