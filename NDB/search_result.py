from NDB.search_report import *
from typing import List


class SearchResult(object):
    def __init__(self):
        self._count = 0
        self._report = []

    def count(self) -> int:
        return self._count

    def report(self) -> list:
        return self._report

    def set_count(self, count: int) -> None:
        self._count = count

    def set_report(self, report: list) -> None:
        self._report = report


class SimpleResult(SearchResult):
    def __init__(self):
        super().__init__()

    def report(self) -> List[SimpleReport]:
        return self._report


class AdvancedResult(SearchResult):
    def __init__(self):
        super().__init__()

    def report(self) -> List[AdvancedReport]:
        return self._report

    def report_ndb_status(self) -> List[NDBStatusReport]:
        return [NDBStatusReport(x) for x in self._report]

    def report_cell_dimensions(self) -> List[CellDimensionsReport]:
        return [CellDimensionsReport(x) for x in self._report]

    def report_citation(self) -> List[CitationReport]:
        return [CitationReport(x) for x in self._report]

    def report_refinement(self) -> List[RefinementDataReport]:
        return [RefinementDataReport(x) for x in self._report]
