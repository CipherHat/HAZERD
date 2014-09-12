__author__ = 'cipherhat'

from os import path
import unittest
from django.test.client import Client
import visa_sponsor
# from comp61542.database import database

class TestApp(unittest.TestCase):
    c = Client()

    def setUp(self):
        dir, _ = path.split(__file__)
        # data = "dblp_curated_sample.xml"
        # visa_sponsor.app.config['TESTING'] = True
        # visa_sponsor.app.config['DATASET'] = data
        # db = database.Database()
        # db.read(path.join(dir, "..", "data", data))
        # comp61542.app.config['DATABASE'] = db
        # self.app = visa_sponsor.app.test_client()

    def test_home(self):
        r = self.c.get("/")
        self.assertEqual(200, r.status_code, "Status code was not 'OK'.")

if __name__ == '__main__':
    unittest.main()