from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_player, name='register_player'),
    path('search/', views.search_player, name='search_player'),
]
