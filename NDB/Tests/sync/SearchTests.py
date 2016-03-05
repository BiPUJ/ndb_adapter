import unittest
from NDB.ndb import NDB


class SearchTests(unittest.TestCase):

    def test_advanced_search(self):
        ndb = NDB()
        report = ndb.advanced_search()
        count = report["count"]
        print("Counted: " + str(count))

        self.assertGreater(count, 7955)


if __name__ == '__main__':
    unittest.main()