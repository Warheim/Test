from Yandex.yandex import Yandex
import unittest


class TestFolder(unittest.TestCase):
    def setUp(self):
        self.status = Yandex()
        self.status.get_headers()
        self.status.get_folder_params()
        self.errors = {400: 'Wrong data',
                       401: 'Unauthorised',
                       404: 'File does not exist',
                       409: 'File already exists',
                       None: 'File already exists',
                       }

    def test_good_creation(self):
        self.create_result = self.status.ya_folder()
        try:
            self.assertEqual(self.create_result, 201)
        except AssertionError:
            print(f'Error code: {self.create_result}, {self.errors[self.create_result]}')

    def test_good_search(self):
        self.search_result = self.status.search_folder()
        try:
            self.assertEqual(self.search_result, 200)
        except AssertionError:
            if self.search_result == 404:
                print(f'Error code: {self.create_result}, {self.errors[self.create_result]}')

    def test_bad_creation(self):
        self.create_result = self.status.ya_folder()
        try:
            self.assertEqual(self.create_result, None)
        except AssertionError:
            if self.create_result == 201:
                print('File created')
            else:
                print(f'Error code: {self.create_result}, {self.errors[self.create_result]}')

    def test_bad_search(self):
        self.search_result = self.status.search_folder()
        try:
            self.assertEqual(self.search_result, 404)
        except AssertionError:
            if self.search_result == 200:
                print('File found')
            else:
                print(f'Error code: {self.create_result}, {self.errors[self.create_result]}')
