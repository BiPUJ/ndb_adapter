import requests

from NDB.advanced_search_options import AdvancedSearchOptions
from NDB.dna_search_options import DnaSearchOptions
from NDB.rna_search_options import RnaSearchOptions
from NDB.search_result import SearchResult
from NDB.ndb_base import NDBBase
import NDB.report_parser as parser
from NDB.summary_result import SummaryResult


class NDB(NDBBase):

    @staticmethod
    def advanced_search(options: AdvancedSearchOptions= None) -> SearchResult:

        if not options:
            options = AdvancedSearchOptions()

        with requests.session() as session:
            resp = session.post(NDBBase._advancedUrl, data=options.get())
            text = resp.text
            report = parser.parse_advanced_search_report(text)
            return report

    @staticmethod
    def dna_search(options: DnaSearchOptions= None) -> SearchResult:

        if not options:
            options = DnaSearchOptions()

        with requests.session() as session:
            resp = session.post(NDBBase._dnaUrl, data=options.get())
            text = resp.text
            report = parser.parse_search_report(text)
            return report

    @staticmethod
    def rna_search(options: RnaSearchOptions= None) -> SearchResult:
        if not options:
            options = RnaSearchOptions()

        with requests.session() as session:
            resp = session.post(NDBBase._rnaUrl, data=options.get())
            text = resp.text
            report = parser.parse_search_report(text)
            return report

    @staticmethod
    def summary(structure_id: str) -> SummaryResult:
        params = {
            'searchTarget': structure_id
        }

        with requests.session() as session:
            resp = session.post(NDBBase._summaryUrl, data=params)
            text = resp.text
            report = parser.parse_summary(text)
            return report
