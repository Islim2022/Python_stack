from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('registration', views.registration),
    path('login', views.login),
    path('success', views.success),
    path('logout', views.logout),
    path('add_book', views.add_book),
    path('books/<int:book_id>', views.view_book),
    path('update_book/<int:book_id>', views.update_book),
    path('delete/<int:book_id>', views.delete_book),
    path('add_to_favorites/<int:book_id>', views.favorite),
    path('remove_from_favorites/<int:book_id>', views.unfavorite),
]