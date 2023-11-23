from django.contrib.auth.models import AbstractUser, BaseUserManager, User
from django.db import models
from django.urls import reverse

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, username, password, **extra_fields)
    
class User(AbstractUser):
    username = models.CharField(max_length=200, default="")
    phone = models.CharField(max_length=10)
    email = models.EmailField("Email", unique=True)
    objects = CustomUserManager()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS = ['username', 'phone']
    def __str__(self):
        return self.username
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
    # def get_absolute_url(self):
    #     return reverse('ownedbook-detail', args=[str(self.id)])
    
# class BorrowedBook(models.Model):
#     borrowed_book = models.ForeignKey(OwnedBook, on_delete=models.CASCADE, default = None)
#     borrower = models.ForeignKey(User, on_delete=models.CASCADE, default = None)
#     book = models.ForeignKey(Book, on_delete=models.CASCADE, default = None)
#     due_back = models.DateField(default = None)
#     def __str__(self):
#         return self.book.title
#     def get_absolute_url(self):
#         return reverse('borrowedbook-detail', args=[str(self.id)])
#     @property
#     def is_overdue(self):
#         return bool(self.due_back and date.today() > self.due_back)

# class WantedBook(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, default = None)
#     book = models.ForeignKey(Book, on_delete=models.CASCADE, default = None)
#     def __str__(self):
#         return self.book.title
#     def get_absolute_url(self):
#         return reverse('wantedbook-detail', args=[str(self.id)])
