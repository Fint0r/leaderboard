from django.urls import path
from . import views

urlpatterns = [
    path('leaderboard/', views.default_response),
    path('', views.default_response),
]
