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
        settings.configure(DJANGO_SETTINGS_MODULE='HAZERD.settings', ROOT_URLCONF='HAZERD.urls')
        # data = "dblp_curated_sample.xml"
        # visa_sponsor.app.config['TESTING'] = True
        # visa_sponsor.app.config['DATASET'] = data
        # db = database.Database()
        # db.read(path.join(dir, "..", "data", data))
        # comp61542.app.config['DATABASE'] = db
        # self.app = visa_sponsor.app.test_client()

    def test_home(self):
        c = Client()
        r = c.get('visa/')
        print(r.status_code)
        self.assertEqual(200, r.status_code, "Status code was not 'OK'.")

if __name__ == '__main__':
    unittest.main()