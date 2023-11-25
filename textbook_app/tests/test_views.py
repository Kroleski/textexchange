import time
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.test import LiveServerTestCase, TestCase
from django.urls import reverse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from ..models import *
from ..views import *
from ..forms import *

class ViewsTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create_superuser(username='admin', phone='555-1111', email='superuser@krypton.com', password='admin54321')

    def setUp(self):
        test_user = User.objects.create(username='Bob', phone='867-5309', email='testbob@squarepants.edu', password='testpass123456')
        test_book = Book.objects.create(isbn = '1234567890123', title = 'A Test Book', author='Arthur Testing', format='Hardcover', description='This book defies description')
        test_user.save()
        test_book.save()
        owned_book = OwnedBook.objects.create(user = test_user, book = test_book, is_available = True, condition = 'Like New')
        owned_book.save()

    def test_view_exists_index(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_index(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_view_url_exists_accounts_login(self):
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_exists_book_list(self):
        response = self.client.get('/book/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_book_list(self):
        response = self.client.get(reverse('book'))
        self.assertEqual(response.status_code, 200)

    def test_view_url_exists_book_detail(self):
        response = self.client.get('/book/1/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_exists_book_add(self):
        response = self.client.get('/book/add/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/?next=/book/add/')

    def test_view_url_accessible_book_add(self):
        response = self.client.get(reverse('book_add'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/?next=/book/add/')

    def test_view_url_exists_book_edit(self):
        response = self.client.get('/book/edit/1/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/?next=/book/edit/1/')

    def test_view_url_exists_book_delete(self):
        response = self.client.get('/book/delete/1/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/?next=/book/delete/1/')

    def test_view_url_exists_books(self):
        response = self.client.get('/books/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_books(self):
        response = self.client.get(reverse('books'))
        self.assertEqual(response.status_code, 200)

    def test_view_url_exists_owned_book_add(self):
        response = self.client.get('/owned-book-add/1/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/?next=/owned-book-add/1/')

    def test_view_url_exists_toggle_availability(self):
        response = self.client.get('/toggle-availability/1/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/?next=/toggle-availability/1/')

    def test_view_url_exists_user_add(self):
        response = self.client.get('/user/add/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_user_add(self):
        response = self.client.get(reverse('user-add'))
        self.assertEqual(response.status_code, 200)

    def test_view_url_exists_user_detail(self):
        response = self.client.get('/user/1/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/?next=/user/1/')

    def test_view_url_exists_users(self):
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/?next=/users/')

    def test_view_url_accessible_users(self):
        response = self.client.get(reverse('users'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/?next=/users/')


class SeleniumViewsTests(LiveServerTestCase):
    def test_1_home_page(self):
        print('')
        print('Selenium TEST 1: Testing that the host is active and that the site title can be read...')
        driver = webdriver.Safari()
        driver.get('http://127.0.0.1:8000/')
        time.sleep(1)
        assert 'Textbook Exchange' in driver.title

    def test_2_navbar(self):
        print('')
        print('Selenium TEST 2: Testing the links in the NavBar...')
        driver = webdriver.Safari()
        driver.get('http://127.0.0.1:8000/')
        time.sleep(1)
        print('Selenium TEST 2a: Testing "Available Books"...')
        available_books = driver.find_element(By.LINK_TEXT, 'Available Books')
        available_books.click()
        time.sleep(1)
        assert 'Books Currently Available' in driver.page_source
        print('Selenium TEST 2b: Testing "All Books"...')
        all_books = driver.find_element(By.LINK_TEXT, 'All Books')
        all_books.click()
        time.sleep(1)
        assert 'All the Books in the Database' in driver.page_source
        print('Selenium TEST 2c: Testing "All Users" access denied to invalid user...')
        all_users = driver.find_element(By.LINK_TEXT, 'All Users')
        all_users.click()
        time.sleep(1)
        assert 'Please login to see this page.' in driver.page_source

    def test_3_login_form(self):
        print('')
        print('Selenium TEST 3a: Testing the user authentication login form can login a valid user...')
        driver = webdriver.Safari()
        driver.get('http://127.0.0.1:8000/accounts/login/')
        time.sleep(1)
        user_email = driver.find_element(By.ID, 'id_username')
        user_password = driver.find_element(By.ID, 'id_password')
        submit = driver.find_element(By.ID, 'submit')
        user_email.send_keys('rkroleski@comcast.net')
        time.sleep(1)
        user_password.send_keys('Password123')
        time.sleep(1)
        submit.send_keys(Keys.RETURN)
        time.sleep(1)
        assert 'rkroleski@comcast.net' in driver.page_source
        print('Selenium TEST 3b: Testing "All Users" access granted to valid user...')
        all_users = driver.find_element(By.LINK_TEXT, 'All Users')
        all_users.click()
        time.sleep(1)
        assert 'User List' in driver.page_source
        print('Selenium TEST 3c: Testing User Detail View access granted to valid user...')
        driver.get('http://127.0.0.1:8000/user/1')
        time.sleep(1)
        assert "User's Name: admin" in driver.page_source



class AddBookViewTest(TestCase):
    def setUp(self):
        test_user = User.objects.create(username='testuser', phone='867-5309', email='testuser@example.com', password='testpassword')
        test_book = Book.objects.create(isbn = '1234567890123', title = 'A Test Book', author='Arthur Testing', format='Hardcover', description='This book defies description')
        test_user.save()
        test_book.save()
        self.ownedbook = OwnedBook.objects.create(user = test_user, book = test_book, is_available = True, condition = 'Like New')
        self.ownedbook.save()
        self.url = reverse('owned-book-add', args=[str(self.ownedbook.id)])

    def test_add_book_view_with_valid_data(self):
        self.client.login(username='testuser', password='testpassword')
        form_data = {
            'title': 'A Test Book',
            'author': 'Arthur Testing',
        }

        response = self.client.post(self.url, form_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Book.objects.filter(title='A Test Book', ownedbook=self.ownedbook).exists())
        # self.assertRedirects(response, reverse('ownedbook-detail', args=[str(self.ownedbook.id)]))

    def test_add_book_view_with_invalid_data(self):
        self.client.login(username='testuser', password='testpassword')
        form_data = {}
        response = self.client.post(self.url, form_data)
        self.assertEqual(response.status_code, 302)

    def test_add_book_view_when_not_logged_in(self):
        response = self.client.get(self.url)
        self.assertRedirects(response, reverse('login') + f'?next={self.url}')