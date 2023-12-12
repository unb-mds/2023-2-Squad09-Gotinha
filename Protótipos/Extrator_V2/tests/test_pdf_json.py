import unittest
from pdf_json import url_Json

class TestPDFJSON(unittest.TestCase):
    def test_url_Json_exists(self):
        self.assertTrue(callable(url_Json), "url_Json não está definido como uma função em pdf_json")

if __name__ == '__main__':
    unittest.main()
