from django.contrib import admin
from django.urls import path
from . import views
from .views import menu

urlpatterns = [
    
    path('', views.menu, name='menu'),  # Assuming the view for the menu page is named 'menu'
]
