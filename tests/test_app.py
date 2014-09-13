import HAZERD

__author__ = 'cipherhat'

from os import path
import unittest
from django.test.client import Client
from HAZERD import settings
from django.conf import settings
import visa_sponsor
# from comp61542.database import database

class TestApp(unittest.TestCase):

    def setUp(self):
        dir, _ = path.split(__file__)
        self.c = Client()

    def test_home(self):
        r = self.c.get('/visa/')
        self.assertEqual(200, r.status_code, "Status code was not 'OK'.")

if __name__ == '__main__':
    unittest.main()