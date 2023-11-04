from django.db import models
from django.urls import reverse

class User(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    email = models.CharField("Email", max_length=200)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('user-detail', args=[str(self.id)])

class Book(models.Model):
    FORMAT = (
    ('Hardcover', 'Hardcover'),
    ('Paperback', 'Paperback'),
    ('PDF', 'PDF file'),
    ('Digital', 'Digital file containing the book'),
    ('Link', 'Link to the book or a free download site'),
    )
    isbn = models.CharField(max_length=13)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200, default='', null=True, blank=True)
    format = models.CharField(max_length=200, choices=FORMAT, blank = False)
    description = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

class OwnedBook(models.Model):
    CONDITION = (
    ('Like New', 'Like New - as if just purchased new'),
    ('Slightly Used', 'Slightly Used - some minor wear and tear'),
    ('Heavily Used', 'Heavily Used - some major wear and tear'),
    ('Poor', 'Poor - The book is in really bad condition'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, default = None)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, default = None)
    is_available = models.BooleanField(default = False)
    condition = models.CharField(max_length=200, choices=CONDITION, blank = False)
    def __str__(self):
        return self.book.title
    def get_absolute_url(self):
        return reverse('ownedbook-detail', args=[str(self.id)])
    
class BorrowedBook(models.Model):
    ownedbook = models.ForeignKey(OwnedBook, on_delete=models.CASCADE, default = None)
    borrower = models.ForeignKey(User, on_delete=models.CASCADE, default = None)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE, default = None)
    def __str__(self):
        return self.book_id.title
    def get_absolute_url(self):
        return reverse('borrowedbook-detail', args=[str(self.id)])

class WantedBook(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default = None)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE, default = None)
    def __str__(self):
        return self.book_id.title
    def get_absolute_url(self):
        return reverse('wantedbook-detail', args=[str(self.id)])
