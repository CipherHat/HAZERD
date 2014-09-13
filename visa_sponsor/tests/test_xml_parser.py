__author__ = 'Abdu'
from os import  path
from django.test import TestCase
from visa_sponsor.src import database

class XMLParserTestCase(TestCase):
    def setUp(self):
        dir, _ = path.split(__file__)
        self.data_dir = path.join(dir, "..", "data")

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        db = database.Database()
        root = db.parse(path.join(self.data_dir, "tier2_sponsor_list.xml"))
        self.assertEqual(root, 'tier2_list')