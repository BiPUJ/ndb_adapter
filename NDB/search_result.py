from NDB.search_report import *
from typing import List

from NDB.statistics import Statistics


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

    def __str__(self):
        return "Count: " + str(self._count) + ", Report:" + str([str(x) for x in self._report])


class SimpleResult(SearchResult):
    def __init__(self):
        super().__init__()

    def report(self) -> List[SimpleReport]:
        return self._report


class AdvancedResult(SearchResult):
    def __init__(self):
        super().__init__()
        self._statistics = Statistics()

    def report(self) -> List[AdvancedReport]:
        return self._report

    def set_statistics(self, report: list) -> None:
        self._statistics.set_report(report)

    def statistics(self) -> Statistics:
        return self._statistics

    def __str__(self):
        return "Count: " + str(self._count) + ", Report:" + str([str(x) for x in self._report]) + \
            "Statistics: " + str(self._statistics)
