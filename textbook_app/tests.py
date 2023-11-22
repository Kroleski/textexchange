import time
from django.contrib.auth.models import User
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .models import *
from .views import *
from .forms import *

# import pytest
# import os
# import sys
# from django.core.exceptions import ValidationError
# from django.test import Client
# from django.test import TestCase
# from django.urls import reverse 
# from selenium.webdriver.chrome.service import Service


class Hosttest(LiveServerTestCase):
    def testhomepage(self):
        print('')
        print('TEST 1: Testing that the host is active and that the site title can be read...')
        driver = webdriver.Safari()
        driver.get('http://127.0.0.1:8000/')
        time.sleep(1)
        assert 'Textbook Exchange' in driver.title


class LoginFormTest(LiveServerTestCase):
    def testform(self):
        print('')
        print('TEST 2: Testing the user authentication login form can login a valid user...')
        driver = webdriver.Safari()
        driver.get('http://127.0.0.1:8000/accounts/login/')
        time.sleep(1)
        user_name = driver.find_element(By.ID, 'id_username')
        user_password = driver.find_element(By.ID, 'id_password')
        submit = driver.find_element(By.ID, 'submit')
        user_name.send_keys('admin')
        time.sleep(1)
        user_password.send_keys('Password123')
        submit.send_keys(Keys.RETURN)
        time.sleep(1)
        assert 'admin' in driver.page_source



# TRAVIS:
# class TestModels(TestCase):
#     def setUp(self):
#         # Set up a Product
#         self.product = Product.objects.create(
#             name='test product',
#             price=999,
#             description='test description',
#             image='test_image.jpg',
#             category='hats',
#         )

#         # Set up a Homescreen
#         self.homescreen = Homescreen.objects.create(
#             title='test title',
#             paragraph='test paragraph',
#         )

#     def test_product(self):
#         product_url = reverse("product_details", kwargs={"pk": self.product.id})
#         product_string = 'test product'

#         self.assertEqual(self.product.name, 'test product')
#         self.assertEqual(self.product.price, 999)
#         self.assertEqual(self.product.description, 'test description')
#         self.assertEqual(self.product.image, 'test_image.jpg')
#         self.assertEqual(self.product.category, 'hats')
#         self.assertEqual(self.product.get_absolute_url(), product_url)
#         self.assertEqual(str(self.product), product_string)

#     def test_home_str(self):
#         homescreen_str = 'test title'
#         self.assertEqual(self.homescreen.title, 'test title')
#         self.assertEqual(str(self.homescreen), homescreen_str)
#         self.assertEqual(self.homescreen.paragraph, 'test paragraph')


# class CreateUserTest(TestCase):
#     def setUp(self):
#         self.client = Client()

#     def test_create_user(self):
#         user_data = {
#             'username': 'testuser',
#             'password1': 'arstarst',
#             'password2': 'arstarst',
#         }
#         response = self.client.post(reverse('register'), user_data)
#         self.assertEqual(response.status_code, 302)
#         self.assertTrue(User.objects.filter(username='testuser').exists())


#  def test_navbar(self):
#         # Test that a user can create a new post using a form

#         # The user goes to the home page of the blog
#         self.browser.get("http://127.0.0.1:8000/")
#         time.sleep(1)
#         dashboard_link = By.LINK_TEXT, "Dashboard"
#         customer_link = By.LINK_TEXT, "Customer view"
#         login_link = By.LINK_TEXT, "Login"
#         logout_link = By.LINK_TEXT, "Log out"
#         register_link = By.LINK_TEXT, "Register"
#         home_link = By.LINK_TEXT, "Home"

#         try:
#             self.browser.find_element(*logout_link).click()
#         except:
#             print("Already logged out")
#         time.sleep(1)
#         self.browser.find_element(*login_link).click() 
#         time.sleep(1)
#         self.browser.find_element(By.ID,'id_username').send_keys('user')
#         self.browser.find_element(By.ID,'id_password').send_keys('arstarst')
#         self.browser.find_element(By.ID,'submit').click()
#         time.sleep(1)
#         self.browser.find_element(*home_link).click()
#         time.sleep(1)
#         self.browser.find_element(*customer_link).click()
#         time.sleep(1)
#         self.browser.find_element(*dashboard_link).click()






# KORY:
# class TestNavbarAndAuthentication(TestCase):

#     def tearDown(self):
#         self.driver.quit()

#     def test_navbar_links(self):
#         # Test Navbar Links
#         # You can find elements by their CSS classes, IDs, or text
#         home_link = self.driver.find_element(By.LINK_TEXT, "Home")
#         grocery_items_link = self.driver.find_element(By.LINK_TEXT, "Grocery Items")
#         recipes_link = self.driver.find_element(By.LINK_TEXT, "Recipes")
#         login_link = self.driver.find_element(By.LINK_TEXT, "Login")

#         # Perform click actions and assertions
#         home_link.click()
#         # Add assertions to check if you are on the correct page after clicking the link
#         self.assertIn("Home", self.driver.title)
        
#         # Similarly, perform similar actions and assertions for other links

#     def test_login_functionality(self):
#         # Test Login Functionality
#         # Find the login link and click it
#         login_link = self.driver.find_element(By.LINK_TEXT, "Login")
#         login_link.click()

#         # Find the username and password fields and submit a login
#         username_field = self.driver.find_element(By.ID, 'id_username')
#         password_field = self.driver.find_element(By.ID, 'id_password')
#         submit_button = self.driver.find_element(By.ID, 'submit')

#         # Enter test credentials and submit the form
#         username_field.send_keys('testuser')
#         password_field.send_keys('testpassword')
#         submit_button.click()

#         # Add assertions to verify successful login
#         # For example:
#         self.assertIn("Welcome", self.driver.page_source)