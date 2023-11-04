from django.forms import ModelForm
from .models import Book, OwnedBook, User

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields=['isbn', 'title', 'author', 'format', 'description']

class OwnedBookForm(ModelForm):
    class Meta:
        model = OwnedBook
        fields = ['book', 'condition']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'phone', 'email']