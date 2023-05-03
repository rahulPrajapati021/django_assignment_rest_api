from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('works/', views.works),
    path('register/', views.register),
    path('creatework/', views.creatework),
]