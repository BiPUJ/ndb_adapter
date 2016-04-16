

class SimpleReport(object):
    def __init__(self, report: dict = None):
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


class AdvancedReport(object):
    def __init__(self, report: dict = None):
        self._report = {
            'NDB ID': '',
            # NDB status Report
            'PDB ID': '',
            'Title': '',
            'NDB Release Date': '',
            'Authors': '',
            'Initial Deposition Date': '',
            # Cell dimensions Report
            'Length A': '',
            'Length B': '',
            'Length C': '',
            'Angle Alpha': '',
            'Angle Beta': '',
            'Angle Gamma': '',
            'Space Group': '',
            # Citation Report
            'Citation Title': '',
            'Citation Authors': '',
            'Journal': '',
            'Pubmed ID': '',
            'Year': '',
            # Refinement Information Report
            'R-value_work': '',
            'R-value_obs': '',
            'R-value_free': '',
            'Higher Resolution Limit': '',
            'Lower Resolution Limit': '',
            'Reflections Observed': '',
            'Structure Refinement': '',
            # NA Backbone Torsion Report
            'Model ID': '',
            'Chain ID': '',
            'Residue Num': '',
            'Residue Name': '',
            "O3'-P-O5'-C5": '',
            "P-O5'-C5'-C4'": '',
            "O5'-C5'-C4'-C3'": '',
            "C5'-C4'-C3'-O3'": '',
            "C4'-C3'-O3'-P": '',
            "C3'-O3'-P-O5'": '',
            "O4'-C1'-N1-9-C2-4": ''
        }
        if report:
            self._report.update(report)

    def ndb_id(self) -> str:
        return self._report['NDB ID']

    def get_dict(self) -> dict:
        return self._report

    def __str__(self) -> str:
        return str(self._report)


class NDBStatusReport(AdvancedReport):
    def __init__(self, parent_class: AdvancedReport = None):
        if parent_class:
            self._report = parent_class._report
        else:
            super().__init__()

    def pdb_id(self) -> str:
        return self._report['PDB ID']

    def title(self) -> str:
        return self._report['Title']

    def release_date(self) -> str:
        return self._report['NDB Release Date']

    def deposition_date(self) -> str:
        return self._report['Initial Deposition Date']

    def authors(self) -> str:
        return self._report['Authors']


class CellDimensionsReport(AdvancedReport):
    def __init__(self, parent_class: AdvancedReport = None):
        if parent_class:
            self._report = parent_class._report
        else:
            super().__init__()

    def cell_a(self) -> str:
        return self._report['Length A']

    def cell_b(self) -> str:
        return self._report['Length B']

    def cell_c(self) -> str:
        return self._report['Length C']

    def cell_alpha(self) -> str:
        return self._report['Angle Alpha']

    def cell_beta(self) -> str:
        return self._report['Angle Beta']

    def cell_gamma(self) -> str:
        return self._report['Angle Gamma']

    def space_group(self) -> str:
        return self._report['Space Group']


class CitationReport(AdvancedReport):
    def __init__(self, parent_class: AdvancedReport = None):
        if parent_class:
            self._report = parent_class._report
        else:
            super().__init__()

    def pdb_id(self) -> str:
        return self._report['PDB ID']

    def citation_title(self) -> str:
        return self._report['Citation Title']

    def citation_authors(self) -> str:
        return self._report['Citation Authors']

    def journal(self) -> str:
        return self._report['Journal']

    def pubmed_id(self) -> str:
        return self._report['Pubmed ID']

    def year(self) -> str:
        return self._report['Year']


class RefinementDataReport(AdvancedReport):
    def __init__(self, parent_class: AdvancedReport = None):
        if parent_class:
            self._report = parent_class._report
        else:
            super().__init__()

    def r_work(self) -> str:
        return self._report['R-value_work']

    def r_obs(self) -> str:
        return self._report['R-value_obs']

    def r_free(self) -> str:
        return self._report['R-value_free']

    def higher_resolution(self) -> str:
        return self._report['Higher Resolution Limit']

    def lower_resolution(self) -> str:
        return self._report['Lower Resolution Limit']

    def reflections(self) -> str:
        return self._report['Reflections Observed']

    def structure_ref(self) -> str:
        return self._report['Structure Refinement']
