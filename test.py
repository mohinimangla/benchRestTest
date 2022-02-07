import requests
import unittest

BASE = "http://127.0.0.1:5000/"
 
class TestGetTransactions(unittest.TestCase):
    # test function
    def test_getall(self):
        response = requests.get(BASE + "/transactions")
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.json()), 1)

    def test_getvalid_page(self):
        response = requests.get(BASE + "/transactions?page=2")
        self.assertEqual(response.status_code, 200)
        self.assertLessEqual(len(response.json()), 10)

    def test_getinvalid_page(self):
        response = requests.get(BASE + "/transactions?page=5")
        self.assertEqual(response.status_code, 404)
        

class TestGetReport(unittest.TestCase):
    def test_getallreport(self):
        response = requests.get(BASE + "/report")
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(response.json()), 0)

unittest.main()