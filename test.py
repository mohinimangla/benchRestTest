import requests
import unittest

BASE = "http://127.0.0.1:5000/"
 
class TestGetTransactions(unittest.TestCase):
    # test function
    def test_getall(self):
        response = requests.get(BASE + "/transactions")
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(response.json().get("count"), 1)
        self.assertGreaterEqual(len(response.json().get("transactions")), 1)
        self.assertLessEqual(len(response.json().get("transactions")), 10)

    def test_getvalid_page(self):
        response = requests.get(BASE + "/transactions?limit=2&offset=11")
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(response.json().get("count"), 1)
        self.assertEqual(len(response.json().get("transactions")), 2)

    def test_getinvalid_offset(self):
        response = requests.get(BASE + "/transactions?offset=90")
        self.assertEqual(response.status_code, 404)
    
    def test_getinvalid_limit(self):
        response = requests.get(BASE + "/transactions?limit=0")
        self.assertEqual(response.status_code, 404)
        

class TestGetReport(unittest.TestCase):
    def test_getallreport(self):
        response = requests.get(BASE + "/report")
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(response.json()), 0)

unittest.main()