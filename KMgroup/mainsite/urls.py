from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main_site),
    path('gallery', views.gallery_site),
    path('price', views.price_site),
    path('reviews', views.reviews_site),
    path('rules', views.rules_site),
    path('contacts', views.contacts_site),
    path('calendar', views.calendar_site),
]