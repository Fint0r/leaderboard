from django.urls import path
from . import views

urlpatterns = [
    path('leaderboard/', views.default_response),
    path('ip/', views.get_client_ip),
    path('', views.default_response),
]
