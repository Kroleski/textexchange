from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name='index'),
path('book/', views.BookListView.as_view(), name= 'book'),
path('book/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
#path('book/<int:pk>/delete/', views.deleteBook, name='book-delete'),
#path('book/<int:pk>/update/', views.updateBook, name='book-update'),
path('users/', views.UserListView.as_view(), name= 'users'),
path('user/<int:pk>', views.UserDetailView.as_view(), name='user-detail'),
#path('user/<int:pk>/create_book/', views.createBook, name='book-create'),
]