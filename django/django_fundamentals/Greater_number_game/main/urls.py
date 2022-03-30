from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index),
    path('submit', views.get_number),
    path('high', views.higher),
    path('low', views.lower),
    path('correct', views.correct),
]