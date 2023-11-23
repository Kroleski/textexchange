# import time
# from django.contrib.auth import get_user_model
# from django.test import LiveServerTestCase, TestCase
# from django.urls import reverse
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from ..models import *
# from ..views import *
# from ..forms import *

# class Anonymous_host_test(LiveServerTestCase):
#     def test_home_page(self):
#         print('')
#         print('TEST 1: Testing that the host is active and that the site title can be read...')
#         driver = webdriver.Safari()
#         driver.get('http://127.0.0.1:8000/')
#         time.sleep(1)
#         assert 'Textbook Exchange' in driver.title

# class Anonymous_navbar_test(LiveServerTestCase):
#     def test_navbar(self):
#         print('')
#         print('TEST 2: Testing the links in the NavBar...')
#         driver = webdriver.Safari()
#         driver.get('http://127.0.0.1:8000/')
#         time.sleep(1)
#         print('TEST 2a: Testing "Available Books"...')
#         available_books = driver.find_element(By.LINK_TEXT, 'Available Books')
#         available_books.click()
#         time.sleep(1)
#         assert 'Books Currently Available' in driver.page_source
#         print('TEST 2b: Testing "All Books"...')
#         all_books = driver.find_element(By.LINK_TEXT, 'All Books')
#         all_books.click()
#         time.sleep(1)
#         assert 'All the Books in the Database' in driver.page_source
#         print('TEST 2c: Testing "All Users" access denied to invalid user...')
#         all_users = driver.find_element(By.LINK_TEXT, 'All Users')
#         all_users.click()
#         time.sleep(1)
#         assert 'Please login to see this page.' in driver.page_source

# class Valid_user_login_and_test_user_links(LiveServerTestCase):
#     def test_login_form(self):
#         print('')
#         print('TEST 3a: Testing the user authentication login form can login a valid user...')
#         driver = webdriver.Safari()
#         driver.get('http://127.0.0.1:8000/accounts/login/')
#         time.sleep(1)
#         user_email = driver.find_element(By.ID, 'id_username')
#         user_password = driver.find_element(By.ID, 'id_password')
#         submit = driver.find_element(By.ID, 'submit')
#         user_email.send_keys('rkroleski@comcast.net')
#         time.sleep(1)
#         user_password.send_keys('Password123')
#         time.sleep(1)
#         submit.send_keys(Keys.RETURN)
#         time.sleep(1)
#         assert 'rkroleski@comcast.net' in driver.page_source
#         print('TEST 3b: Testing "All Users" access granted to valid user...')
#         all_users = driver.find_element(By.LINK_TEXT, 'All Users')
#         all_users.click()
#         time.sleep(1)
#         assert 'User List' in driver.page_source
#         print('TEST 3c: Testing User Detail View access granted to valid user...')
#         driver.get('http://127.0.0.1:8000/user/1')
#         time.sleep(1)
#         assert "User's Name: admin" in driver.page_source
