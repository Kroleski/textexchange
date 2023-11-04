from django.urls import path
from . import views
from .views import list_books

urlpatterns = [
path('', views.index, name='index'),
path('book/', views.BookListView.as_view(), name= 'book'),
path('book/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
path('book/add/', views.book_add, name='book_add'),
path('book/edit/<int:pk>/', views.book_edit, name='book-edit'),
path('book/delete/<int:pk>/', views.book_confirm_delete, name='book-confirm-delete'),
path('books/', list_books, name='books'),
path('owned-book-add/<int:user_id>/', views.owned_book_add, name='owned-book-add'),
path('toggle-availability/<int:owned_book_id>/', views.toggle_availability, name='toggle-availability'),
path('user/add/', views.user_add, name='user-add'),
path('user/<int:pk>', views.UserDetailView.as_view(), name='user-detail'),
path('users/', views.UserListView.as_view(), name= 'users'),
]