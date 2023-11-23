from ..models import *
from django.contrib.auth import get_user_model
from django.test import TestCase


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(username='Bob', phone='867-5309', email='testbob@squarepants.edu', password='testpass123456')
        User.objects.create_superuser(username='admin', phone='555-1111', email='superuser@krypton.com', password='admin54321')

    def test_user_field_values(self):
        user = User.objects.get(id=1)
        self.assertEqual(user.username, 'Bob')
        self.assertEqual(user.phone, '867-5309')
        self.assertEqual(user.email, 'testbob@squarepants.edu')
        self.assertEqual(user.password, 'testpass123456')

    def test_superuser_field_values(self):
        superuser = User.objects.get(id=2)
        self.assertEqual(superuser.username, 'admin')
        self.assertEqual(superuser.phone, '555-1111')
        self.assertEqual(superuser.email, 'superuser@krypton.com')
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)

    def test_username_label(self):
        user = User.objects.get(id=1)
        username_label = user._meta.get_field('username').verbose_name
        self.assertEqual(username_label, 'username')

    def test_username_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('username').max_length
        self.assertEqual(max_length, 200)

    def test_phone_label(self):
        user = User.objects.get(id=1)
        phone_label = user._meta.get_field('phone').verbose_name
        self.assertEqual(phone_label, 'phone')

    def test_phone_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('phone').max_length
        self.assertEqual(max_length, 10)

    def test_email_label(self):
        user = User.objects.get(id=1)
        email_label = user._meta.get_field('email').verbose_name
        self.assertEqual(email_label, 'Email')

    def test_email_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('email').max_length
        self.assertEqual(max_length, 254)

    def test_user_withinvalid_email(self):
        with self.assertRaises(ValueError):
            User.objects.create_user(username='Bad Email', email='', password='noemail')
            
    def test_password_label(self):
        user = User.objects.get(id=1)
        password_label = user._meta.get_field('password').verbose_name
        self.assertEqual(password_label, 'password')

    def test_password_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('password').max_length
        self.assertEqual(max_length, 128)

    def test_object_name_is_username(self):
        user = User.objects.get(id=1)
        expected_object_name = f'{user.username}'
        self.assertEqual(str(user), expected_object_name)

    def test_get_absolute_url(self):
        user = User.objects.get(id=1)
        self.assertEqual(user.get_absolute_url(), '/user/1/')

    def test_superuser_with_invalid_flags(self):
        User = get_user_model()
        email = 'admin2@example.com'
        with self.assertRaises(ValueError):
            User.objects.create_superuser(email=email, username='admin', password='adminpassword', is_staff=False)
        with self.assertRaises(ValueError):
            User.objects.create_superuser(email=email, username='admin', password='adminpassword', is_superuser=False)

class BookModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Book.objects.create(isbn = '1234567890123', title = 'A Test Book', author='Arthur Testy', format='Hardcover', description='This book defies description')

    def test_isbn_label(self):
        book = Book.objects.get(id=1)
        isbn_label = book._meta.get_field('isbn').verbose_name
        self.assertEqual(isbn_label, 'isbn')

    def test_isbn_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field('isbn').max_length
        self.assertEqual(max_length, 13)

    def test_title_label(self):
        book = Book.objects.get(id=1)
        title_label = book._meta.get_field('title').verbose_name
        self.assertEqual(title_label, 'title')

    def test_title_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field('title').max_length
        self.assertEqual(max_length, 200)

    def test_author_label(self):
        book = Book.objects.get(id=1)
        author_label = book._meta.get_field('author').verbose_name
        self.assertEqual(author_label, 'author')

    def test_author_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field('author').max_length
        self.assertEqual(max_length, 200)

    def test_format_label(self):
        book = Book.objects.get(id=1)
        format_label = book._meta.get_field('format').verbose_name
        self.assertEqual(format_label, 'format')

    def test_format_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field('format').max_length
        self.assertEqual(max_length, 200)

    def test_description_label(self):
        book = Book.objects.get(id=1)
        description_label = book._meta.get_field('description').verbose_name
        self.assertEqual(description_label, 'description')

    def test_object_name_is_title(self):
        book = Book.objects.get(id=1)
        expected_object_name = f'{book.title}'
        self.assertEqual(str(book), expected_object_name)

    def test_get_absolute_url(self):
        book = Book.objects.get(id=1)
        self.assertEqual(book.get_absolute_url(), '/book/1/')

class OwnedBookModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create(username='Bob', phone='867-5309', email='testbob@squarepants.edu', password='testpass123456')
        test_book = Book.objects.create(isbn = '1234567890123', title = 'A Test Book', author='Arthur Testy', format='Hardcover', description='This book defies description')
        OwnedBook.objects.create(user = test_user, book = test_book, is_available = True, condition = 'Like New')

    def test_user_label(self):
        owned_book = OwnedBook.objects.get(id=1)
        user_label = owned_book._meta.get_field('user').verbose_name
        self.assertEqual(user_label, 'user')

    def test_book_label(self):
        owned_book = OwnedBook.objects.get(id=1)
        book_label = owned_book._meta.get_field('book').verbose_name
        self.assertEqual(book_label, 'book')

    def test_is_avaiable_label(self):
        owned_book = OwnedBook.objects.get(id=1)
        is_avaiable_label = owned_book._meta.get_field('is_available').verbose_name
        self.assertEqual(is_avaiable_label, 'is available')

    def test_condition_label(self):
        owned_book = OwnedBook.objects.get(id=1)
        condition_label = owned_book._meta.get_field('condition').verbose_name
        self.assertEqual(condition_label, 'condition')

    def test_condition_length(self):
        owned_book = OwnedBook.objects.get(id=1)
        max_length = owned_book._meta.get_field('condition').max_length
        self.assertEqual(max_length, 200)

    def test_object_name_is_book_title(self):
        owned_book = OwnedBook.objects.get(id=1)
        expected_object_name = f'{owned_book.book.title}'
        self.assertEqual(str(owned_book), expected_object_name)

    # def test_get_absolute_url(self):
    #     owned_book = OwnedBook.objects.get(id=1)
    #     self.assertEqual(owned_book.get_absolute_url(), '/book/1/')