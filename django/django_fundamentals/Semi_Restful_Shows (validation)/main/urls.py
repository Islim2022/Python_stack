from django.urls import path
from . import views
from .models import Show

urlpatterns = [
    path('shows', views.shows),
    path('shows/new', views.add_show),
    path('shows/create', views.create), #When we click create, new show is added.
    path('shows/<int:show_id>', views.show_summary),
    path('shows/<int:show_id>/edit', views.edit_show),
    path('shows/<int:show_id>/update', views.update_show), #When we click update, updates is made to the show.
    path('shows/<int:show_id>/destroy', views.delete)
]