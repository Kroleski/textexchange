from django import forms
from django.forms import ModelForm
from .models import Book, User, OwnedBook

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields=['isbn', 'title', 'author', 'description']

    # def clean_isbn(self):
    #     isbn = self.cleaned_data['isbn']
    #     return isbn

    # def clean_title(self):
    #     title = self.cleaned_data['title']
    #     return title

    # def clean_author(self):
    #     author = self.cleaned_data['author']
    #     return author

    # def clean_description(self):
    #     description = self.cleaned_data['description']
    #     return description

class BookSearchForm(forms.Form):
    isbn = forms.CharField(label='10-digit or 13-digit ISBN', max_length=13)

class OwnedBookForm(ModelForm):
    class Meta:
        model = OwnedBook
        fields = ['book', 'condition']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'phone', 'email']