import unittest
from flask import Flask
from app.common import status
import app.server as server


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.app = Flask('Fruit World', static_folder="./app/static")
        self.app.add_url_rule('/', view_func=server.home)
        self.app.add_url_rule('/fruits', view_func=server.fruits)
        self.app.add_url_rule('/re_sort', view_func=server.re_sort)
        self.app.add_url_rule('/reset', view_func=server.reset_list)

    def tearDown(self):
        pass


class TestServer(BaseTest):

    def test_home(self):
      """This should return a 200 status code when the home page is requested"""
      with self.app.test_client() as client:
        response = client.get('/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_fruits(self):
      """This should add the fruit from the GET request to the fruit_list and return a 200 status code when the fruits page is requested"""
      with self.app.test_client() as client:
        response = client.get('/fruits?fruit=Apple')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        

    def test_re_sort(self):
      """This should return a 200 status code when the re_sort page is requested"""
      with self.app.test_client() as client:
        client.get('/fruits?fruit=Apple')
        client.get('/fruits?fruit=Banana')
        response = client.get('/re_sort?fruit=&sorting_type=Protein')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = client.get('/re_sort?fruit=&sorting_type=Carbohydrates')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        response = client.get('/re_sort?fruit=&sorting_type=Calories')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = client.get('/re_sort?fruit=&sorting_type=Fat')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = client.get('/re_sort?fruit=&sorting_type=Sugar')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_reset(self):
      """This should return to the home page when the reset button is clicked"""

      with self.app.test_client() as client:
        response = client.get('/reset')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestErrors(BaseTest):

    def test_fruits_error_handler(self):
      """This should return an error handler when the fruits page is requested without a fruit"""
      with self.app.test_client() as client:
        response = client.get('/fruits')
        self.assertIn(b"Please Select More Fruits To Sort and Compare!", response.data)


    def test_re_sort_error_handler(self):
      """this should return an error handler when the re_sort page is requested without a fruit"""
      with self.app.test_client() as client:
        response = client.get('/re_sort?fruit=&sorting_type=Sugar')
        self.assertIn(b"Please Select More Fruits To Sort and Compare!", response.data)
        response = client.get('/re_sort?fruit=&sorting_type=Carbohydrates')
        self.assertIn(b"Please Select More Fruits To Sort and Compare!", response.data)
        response = client.get('/re_sort?fruit=&sorting_type=Protein')
        self.assertIn(b"Please Select More Fruits To Sort and Compare!", response.data)
        response = client.get('/re_sort?fruit=&sorting_type=Calories')
        self.assertIn(b"Please Select More Fruits To Sort and Compare!", response.data)
        response = client.get('/re_sort?fruit=&sorting_type=Fat')
        self.assertIn(b"Please Select More Fruits To Sort and Compare!", response.data)
