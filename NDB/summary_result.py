

class SummaryResult(object):
    def __init__(self):
        self._report = {
            'PDB ID': '',
            'NDB ID': '',
            'Title': '',
            'Space Group': '',
            'Refinement': '',
            'Experimental Information': '',
            'Molecular Description': '',
            'Protein Sequence': {},
            'Primary Citation': {
                'Journal': '',
                'Authors': '',
                'pp': '',
                'Year': '',
                'Pubmed Id': '',
                'Title': ''
            },
            'Cell Constants': {
                'a': '',
                'b': '',
                'c': '',
                'alpha': '',
                'beta': '',
                'gamma': ''
            },
            'Nucleic Acid Sequence': {}
        }

    def pdb_id(self) -> str:
        return self._report['PDB ID']

    def ndb_id(self) -> str:
        return self._report['NDB ID']

    def title(self) -> str:
        return self._report['Title']

    def space_group(self) -> str:
        return self._report['Space Group']

    def refinement(self) -> str:
        return self._report['Refinement']

    def experimental_method(self) -> str:
        return self._report['Experimental Information']

    def description(self) -> str:
        return self._report['Molecular Description']

    def citation_journal(self) -> str:
        return self._report['Primary Citation']['Journal']

    def citation_authors(self) -> str:
        return self._report['Primary Citation']['Authors']

    def citation_pages(self) -> str:
        return self._report['Primary Citation']['pp']

    def citation_year(self) -> str:
        return self._report['Primary Citation']['Year']

    def citation_pubmed_id(self) -> str:
        return self._report['Primary Citation']['Pubmed Id']

    def citation_title(self) -> str:
        return self._report['Primary Citation']['Title']

    def cell_constants(self) -> dict:
        return self._report['Cell Constants']

    def cell_a(self) -> float:
        return self._report['Cell Constants']['a']

    def cell_b(self) -> float:
        return self._report['Cell Constants']['b']

    def cell_c(self) -> float:
        return self._report['Cell Constants']['c']

    def cell_alpha(self) -> float:
        return self._report['Cell Constants']['alpha']

    def cell_beta(self) -> float:
        return self._report['Cell Constants']['beta']

    def cell_gamma(self) -> float:
        return self._report['Cell Constants']['gamma']

    def protein_seq(self) -> list:
        return list(self._report['Protein Sequence'].values())

    def protein_seq_with_names(self) -> list:
        return list(self._report['Protein Sequence'].items())

    def nucleic_acid_seq(self) -> list:
        return list(self._report['Nucleic Acid Sequence'].values())

    def nucleic_acid_seq_with_names(self) -> list:
        return list(self._report['Nucleic Acid Sequence'].items())

    def update(self, report: dict) -> None:
        self._report.update(report)

    def get_dict(self) -> dict:
        return self._report

    def __str__(self) -> str:
        return str(self._report)
