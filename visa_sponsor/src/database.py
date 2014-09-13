__author__ = 'Abdu'

import xml.etree.ElementTree as ET

class Database(object):

    def _init_(self, XMLfile):
        self.XMLfile = XMLfile

    def parse(self, XMLfile):
        tree = ET.parse(XMLfile)
        print tree.getroot()
        return tree.getroot()