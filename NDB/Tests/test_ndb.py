import unittest
from datetime import date
from NDB.advanced_search_options import AdvancedSearchOptions
from NDB.dna_search_options import DnaSearchOptions
from NDB.ndb import NDB
from NDB.enums import *


class NDBTest(unittest.TestCase):

    def test_advanced_search(self) -> None:
        result = NDB.advanced_search()
        count = result.count()
        print("Counted: " + str(count))
        print("ReleaseDate: " + str(result.report()[0].release_date()))

        self.assertGreater(count, 7955)

    def test_advanced_search_statistic(self) -> None:
        opt = AdvancedSearchOptions(ReportType.RNABasePairRelFreq)
        opt.set_hybrid(yes_no_ignore=YesNoIgnore.Yes)
        result = NDB.advanced_search(opt)

        count = result.count()
        print("Counted: " + str(count))
        print("Stats: " + str(result.statistics()))

        self.assertGreaterEqual(count, 37)
        self.assertIsNot(result.statistics().min, {})

    def test_advanced_search_citation(self) -> None:
        opt = AdvancedSearchOptions(report_type=ReportType.Citation)

        result = NDB.advanced_search(opt)
        count = result.count()
        first = result.report()[0]  # type: ReportType.Citation
        print("Counted: " + str(count))

        self.assertGreater(count, 8020)
        self.assertTrue(isinstance(first.year(), int))

    def test_advanced_search_cell_dime(self) -> None:
        opt = AdvancedSearchOptions(report_type=ReportType.CellDimensions)

        result = NDB.advanced_search(opt)
        count = result.count()
        first = result.report()[0]  # type: ReportType.CellDimensions
        print("Counted: " + str(count))

        self.assertGreaterEqual(count, 7349)
        self.assertTrue(isinstance(first.cell_a(), float))

    def test_advanced_search_drug_binding(self) -> None:
        opt = AdvancedSearchOptions()
        opt.set_drug(yes_no_ignore=YesNoIgnore.Yes)
        opt.set_drug_binding(AndOr.Or, DrugBinding.Intercalation, DrugBinding.OutsideBinder)

        result = NDB.advanced_search(opt)
        count = result.count()
        print("Counted: " + str(count))

        self.assertGreaterEqual(count, 250)

    def test_advanced_search_released_since(self) -> None:
        opt = AdvancedSearchOptions()
        opt.set_released(since_date=date(2015, 5, 1))

        result = NDB.advanced_search(opt)
        count = result.count()
        print("Counted: " + str(count))

        self.assertGreaterEqual(count, 626)

    def test_advanced_search_alpha(self) -> None:
        opt = AdvancedSearchOptions()
        opt.set_cell_alpha(gt_lt_eq=GreaterLowerEqual.GreaterEqual, value=40.0)

        result = NDB.advanced_search(opt)
        count = result.count()
        print("Counted: " + str(count))

        self.assertGreaterEqual(count, 6734)

    def test_dna_search(self) -> None:
        result = NDB.dna_search()
        count = result.count()
        print("Counted: " + str(count))
        print("Report: " + str(result.report()))

        self.assertGreater(count, 5420)

    def test_dna_search_polymer(self) -> None:
        opt = DnaSearchOptions()
        opt.set_polymer(Polymer.DrugDNA)

        result = NDB.dna_search(opt)
        count = result.count()
        print("Counted: " + str(count))
        print("Report: " + str(result.report()))

        self.assertGreaterEqual(count, 377)

    def test_dna_search_structural_features(self) -> None:
        opt = DnaSearchOptions()
        opt.set_structural_features(StructuralFeatures.aDNA)

        result = NDB.dna_search(opt)
        count = result.count()
        print("Counted: " + str(count))
        print("Report: " + str(result.report()))

        self.assertGreaterEqual(count, 392)

    def test_rna_search(self) -> None:
        result = NDB.rna_search()
        count = result.count()
        print("Counted: " + str(count))
        print("Report: " + str(result.report()))

        self.assertGreater(count, 2950)

    def test_report_search(self) -> None:
        result = NDB.dna_search()
        first = result.report()[0]
        print("First: " + first.pdb_id())

        self.assertIsNotNone(first)

    def test_summary(self) -> None:
        report = NDB.summary('5F8K')
        print(report.ndb_id())
        print("Report: " + str(report))

        self.assertTrue(report)


if __name__ == '__main__':
    unittest.main()
