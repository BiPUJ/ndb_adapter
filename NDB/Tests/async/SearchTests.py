import unittest
import asyncio
from NDB.asyncndb import NDB
from NDB.enums import ReportType


class SearchTests(unittest.TestCase):
    def setUp(self):
        self.main_loop = asyncio.get_event_loop()

    def test_advanced_search(self):
        report = self.main_loop.run_until_complete(NDB.advanced_search())
        count = report["count"]
        print("Counted: " + str(count))

        self.assertGreater(count, 7955)

    def test_advanced_search_citation(self):
        report = self.main_loop.run_until_complete(NDB.advanced_search(rep_type=ReportType.Citation))
        count = report["count"]
        print("Counted: " + str(count))

        self.assertGreater(count, 8020)

    def test_dna_search(self):
        report = self.main_loop.run_until_complete(NDB.dna_search())
        count = report["count"]
        print("Counted: " + str(count))

        self.assertGreater(count, 5420)

if __name__ == '__main__':
    unittest.main()