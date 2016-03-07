import unittest
from NDB.ndb import NDB
from NDB.enums import ReportType


class SearchTests(unittest.TestCase):

    def test_advanced_search(self):
        report = NDB.advanced_search()
        count = report["count"]
        print("Counted: " + str(count))

        self.assertGreater(count, 7955)

    def test_advanced_search_citation(self):
        report = NDB.advanced_search(rep_type=ReportType.Citation)
        count = report["count"]
        print("Counted: " + str(count))

        self.assertGreater(count, 8020)

    def test_dna_search(self):
        report = NDB.dna_search()
        count = report["count"]
        print("Counted: " + str(count))
        print("Report: " + str(report))

        self.assertGreater(count, 5420)

    def test_rna_search(self):
        report = NDB.rna_search()
        count = report["count"]
        print("Counted: " + str(count))
        print("Report: " + str(report))

        self.assertGreater(count, 2950)

    def test_summary(self):
        report = NDB.summary('NA3352')
        print("Report: " + str(report))

        self.assertTrue(report)


if __name__ == '__main__':
    unittest.main()