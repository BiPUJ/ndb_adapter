from NDB.search_report import *
from typing import List

from NDB.statistics import Statistics


class SearchResult(object):
    """Base class for search result"""
    def __init__(self):
        """Default constructor"""
        self._count = 0
        self._report = []

    def get_count(self) -> int:
        """Gets search results count

        :return: search results count
        :rtype: int
        """
        return self._count

    def get_report(self) -> list:
        """Gets search results report

        :return: list of search results reports
        :rtype: list
        """
        return self._report

    def set_count(self, count: int) -> None:
        """Sets result count

        :param count: value to set as count
        :type count: int
        :return: None
        """
        self._count = count

    def set_report(self, report: list) -> None:
        """Sets result report list

        :param report: list to be set as report
        :type report: list
        :return: None
        """
        self._report = report

    report = property(get_report, set_report, doc="Gets result report")
    """Search report property gets report list"""
    count = property(get_count, set_count, doc="Gets result count")
    """Search count property gets report count"""

    def __str__(self):
        return "Count: " + str(self._count) + ", Report:" + str([str(x) for x in self._report])


class SimpleResult(SearchResult):
    """Class for simple search result"""
    def __init__(self):
        """Default constructor"""
        super().__init__()

    def get_report(self) -> List[SimpleReport]:
        """Gets search results report list

        :return: list of simple search reports
        :rtype: List[SimpleReport]
        """
        return self._report


class AdvancedResult(SearchResult):
    """Class for advanced search result"""
    def __init__(self):
        """Default constructor"""
        super().__init__()
        self._statistics = Statistics()

    def get_report(self) -> List[AdvancedReport]:
        """Gets advanced search results report list. You should annotate return type depending on ReportType.

        :return: list of advanced search reports
        :rtype: List[AdvancedReport]
        """
        return self._report

    def get_statistics(self) -> Statistics:
        """Get statistics of advanced search

        :return: statistics of advanced search
        :rtype Statistics
        """
        return self._statistics

    def set_statistics(self, report: list) -> None:
        """Sets statistic

        :param report: report list to be parse as statistic
        :type report: list
        :return: None
        """
        self._statistics.set_report(report)

    statistics = property(get_statistics, set_statistics, doc="Statistics of advanced search")
    """Statistic report property gets report statistic"""

    def __str__(self):
        return "Count: " + str(self._count) + ", Report:" + str([str(x) for x in self._report]) + \
            "Statistics: " + str(self._statistics)
