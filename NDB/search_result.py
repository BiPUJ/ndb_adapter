

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
