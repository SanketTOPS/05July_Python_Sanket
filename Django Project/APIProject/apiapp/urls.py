from django.contrib import admin
from django.urls import path,include
from apiapp import views

urlpatterns = [
    path('getalldata/',views.getalldata),
    path('getstid/<int:id>/',views.getstid),
    path('deleteid/<int:id>/',views.deleteid),
    path('savestdata/',views.savestdata),
    path('updatedata/<int:id>/',views.updatedata),
]
