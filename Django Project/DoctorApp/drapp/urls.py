from django.contrib import admin
from django.urls import path,include
from drapp import views

urlpatterns = [
   path('',views.index),
   path('about/',views.about),
   path('appointment/',views.appointment),
   path('blog/',views.blog),
   path('contact/',views.contact),
   path('detail/',views.detail),
   path('price/',views.price),
   path('search/',views.search),
   path('team/',views.team),
   path('service/',views.service),
   path('testimonial/',views.testimonial),


]

