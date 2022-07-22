import unittest
from Functions.Functions import *
from Functions.Functions_work import directories, documents


class TestFunc(unittest.TestCase):
    def setUp(self):
        self.people = []
        for person in documents:
            self.people.append(person['name'])
            self.people.append('Неверный номер!')
        self.doc_number = []
        for number in documents:
            self.doc_number.append(number['number'])
            self.doc_number.append('Неверный номер!')
        self.doc_type = []
        for doctype in documents:
            self.doc_type.append(doctype['type'])
            self.doc_type.append('Неверный номер!')
        self.shelf = []
        for shelf in directories.keys():
            self.shelf.append(shelf)
            self.shelf.append('Неверный номер!')

    def test_doc_people(self):
        result = doc_people('11-2')
        standard = self.people
        self.assertIn(result, standard)
