from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('new_dojo', views.new_dojo),
    path('new_ninja', views.new_ninja),
    path('delete/<int:id>', views.delete)
]
