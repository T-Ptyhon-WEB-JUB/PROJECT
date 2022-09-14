from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.get_books, name='get_books'),
    path('books/<int:book_id>/', views.get_book, name='get_book'),
    path('books/<int:book_id>/edit/', views.edit_book, name='edit_book'),
    path('books/<int:book_id>/delete/', views.delete_book, name='delete_book'),
    path('books/add/', views.add_book, name='add_book'),
]
