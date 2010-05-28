# -*- coding: utf-8 -*-
"""
@author: ilgar
"""
import unittest
from pyzimbra import zutil


class Test(unittest.TestCase):

    # -------------------------------------------------------------------- tests
    def testEmptyHostname(self):
        self.assertRaises(zutil.ZClientException, zutil.soap_url, "")


    def testNotEmptyHostname(self):
        result = zutil.soap_url("localhost")
        self.assertEqual("http://localhost/service/soap", result)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()