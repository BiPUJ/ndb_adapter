

class SearchReport(object):
    def __init__(self, report: dict= None):
        self._report = {
            'NDB ID': '',
            'PDB ID': '',
            'Classification': '',
            'Title': '',
            'PDB Release Date': '',
            'Authors': '',
            'Citation Title': '',
            'Citation Detail': '',
            'Experiment': '',
            'Resolution': '',
            'R work': '',
            'R free': ''
        }
        if report:
            self._report.update(report)

    def pdb_id(self) -> str:
        return self._report['PDB ID']

    def ndb_id(self) -> str:
        return self._report['NDB ID']

    def title(self) -> str:
        return self._report['Title']

    def classification(self) -> str:
        return self._report['Classification']

    def release_date(self) -> str:
        return self._report['PDB Release Date']

    def authors(self) -> str:
        return self._report['Authors']

    def citation_title(self) -> str:
        return self._report['Citation Title']

    def citation_detail(self) -> str:
        return self._report['Citation Detail']

    def experimental_method(self) -> str:
        return self._report['Experiment']

    def resolution(self) -> str:
        return self._report['Resolution']

    def r_work(self) -> str:
        return self._report['R work']

    def r_free(self) -> str:
        return self._report['R free']

    def get_dict(self) -> dict:
        return self._report

    def __str__(self) -> str:
        return str(self._report)
