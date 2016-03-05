import unittest
import asyncio
from NDB.asyncndb import NDB


class SearchTests(unittest.TestCase):
    def setUp(self):
        self.main_loop = asyncio.get_event_loop()

    def test_advanced_search(self):
        ndb = NDB()
        report = self.main_loop.run_until_complete(ndb.advanced_search())
        count = report["count"]
        print("Counted: " + str(count))

        self.assertGreater(count, 7955)


if __name__ == '__main__':
    unittest.main()