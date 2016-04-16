from typing import TypeVar


def assign_numbers(dic: dict):
    for k, v in dic.items():
        try:
            if '.' in v:
                dic[k] = float(v)
            else:
                dic[k] = int(v)
        except ValueError:
            pass
    return dic


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


class _AdvancedBaseReport(object):
    def __init__(self):
        self._report = {
            'NDB ID': ''
        }

    def _update(self, report: dict) -> None:
        self._report.update(report)

    @staticmethod
    def report_type() -> str:
        raise NotImplementedError

    def ndb_id(self) -> str:
        return self._report['NDB ID']

    def get_dict(self) -> dict:
        return self._report

    def __str__(self) -> str:
        return str(self._report)


class NDBStatusReport(_AdvancedBaseReport):
    def __init__(self, report: dict= None):
        super().__init__()
        self._update({
            'PDB ID': '',
            'Title': '',
            'NDB Release Date': '',
            'Authors': '',
            'Initial Deposition Date': ''
        })
        if report:
            self._update(report)

    @staticmethod
    def report_type() -> str:
        return 'ndbStatus'

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


class CellDimensionsReport(_AdvancedBaseReport):
    def __init__(self, report: dict = None):
        super().__init__()
        self._update({
            'Length A': 0,
            'Length B': 0,
            'Length C': 0,
            'Angle Alpha': 0,
            'Angle Beta': 0,
            'Angle Gamma': 0,
            'Space Group': ''
        })
        if report:
            self._update(assign_numbers(report))

    @staticmethod
    def report_type() -> str:
        return 'cellDim'

    def cell_a(self) -> float:
        return self._report['Length A']

    def cell_b(self) -> float:
        return self._report['Length B']

    def cell_c(self) -> float:
        return self._report['Length C']

    def cell_alpha(self) -> float:
        return self._report['Angle Alpha']

    def cell_beta(self) -> float:
        return self._report['Angle Beta']

    def cell_gamma(self) -> float:
        return self._report['Angle Gamma']

    def space_group(self) -> str:
        return self._report['Space Group']


class CitationReport(_AdvancedBaseReport):
    def __init__(self, report: dict = None):
        super().__init__()
        self._update({
            'PDB ID': '',
            'Citation Title': '',
            'Citation Authors': '',
            'Journal': '',
            'Pubmed ID': '',
            'Year': 0
        })
        if report:
            self._update(assign_numbers(report))

    @staticmethod
    def report_type() -> str:
        return 'citation'

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

    def year(self) -> int:
        return self._report['Year']


class RefinementDataReport(_AdvancedBaseReport):
    def __init__(self, report: dict = None):
        super().__init__()
        self._update({
            'R-value_work': 0,
            'R-value_obs': 0,
            'R-value_free': 0,
            'Higher Resolution Limit': 0,
            'Lower Resolution Limit': 0,
            'Reflections Observed': 0,
            'Structure Refinement': ''
        })
        if report:
            self._update(assign_numbers(report))

    @staticmethod
    def report_type() -> str:
        return 'ref'

    def r_work(self) -> float:
        return self._report['R-value_work']

    def r_obs(self) -> float:
        return self._report['R-value_obs']

    def r_free(self) -> float:
        return self._report['R-value_free']

    def higher_resolution(self) -> float:
        return self._report['Higher Resolution Limit']

    def lower_resolution(self) -> float:
        return self._report['Lower Resolution Limit']

    def reflections(self) -> int:
        return self._report['Reflections Observed']

    def structure_ref(self) -> str:
        return self._report['Structure Refinement']


class NABackboneTorsionReport(_AdvancedBaseReport):
    def __init__(self, report: dict = None):
        super().__init__()
        self._update({
            'Model ID': '',
            'Chain ID': '',
            'Residue Num': 0,
            'Residue Name': '',
            "O3'-P-O5'-C5": 0,
            "P-O5'-C5'-C4'": 0,
            "O5'-C5'-C4'-C3'": 0,
            "C5'-C4'-C3'-O3'": 0,
            "C4'-C3'-O3'-P": 0,
            "C3'-O3'-P-O5'": 0,
            "O4'-C1'-N1-9-C2-4": 0
        })
        if report:
            self._update(assign_numbers(report))

    @staticmethod
    def report_type() -> str:
        return 'nabt'

    def model_id(self) -> str:
        return self._report['Model ID']

    def chain_id(self) -> str:
        return self._report['Chain ID']

    def residue_number(self) -> int:
        return self._report['Residue Num']

    def residue_name(self) -> str:
        return self._report['Residue Name']

    def O3_P_O5_C5(self) -> float:
        return self._report["O3'-P-O5'-C5'"]

    def P_O5_C5_C4(self) -> float:
        return self._report["P-O5'-C5'-C4'"]

    def O5_C5_C4_C3(self) -> float:
        return self._report["O5'-C5'-C4'-C3'"]

    def C5_C4_C3_O3(self) -> float:
        return self._report["C5'-C4'-C3'-O3'"]

    def C4_C3_O3_P(self) -> float:
        return self._report["C4'-C3'-O3'-P"]

    def C3_O3_P_O5(self) -> float:
        return self._report["C3'-O3'-P-O5'"]

    def O4_C1_N1_9_C2_4(self) -> float:
        return self._report["O4'-C1'-N1-9-C2-4"]


class BasePairParameterReport(_AdvancedBaseReport):
    def __init__(self, report: dict = None):
        super().__init__()
        self._update({
            'Model Number': 0,
            'Pair Number': 0,
            'Pair Name': '',
            'Shear': 0,
            'Stretch': 0,
            'Stagger': 0,
            'Buckle': 0,
            'Propellor': 0,
            'Opening': 0
        })
        if report:
            self._update(assign_numbers(report))

    @staticmethod
    def report_type() -> str:
        return 'bpp'

    def model_num(self) -> int:
        return self._report['Model Number']

    def pair_num(self) -> int:
        return self._report['Pair Number']

    def pair_name(self) -> str:
        return self._report['Pair Name']

    def shear(self) -> float:
        return self._report['Shear']

    def stretch(self) -> float:
        return self._report['Stretch']

    def stagger(self) -> float:
        return self._report['Stagger']

    def buckle(self) -> float:
        return self._report['Buckle']

    def propellor(self) -> float:
        return self._report['Propellor']

    def opening(self) -> float:
        return self._report['Opening']


class BasePairStepParameterReport(_AdvancedBaseReport):
    def __init__(self, report: dict = None):
        super().__init__()
        self._update({
            'Model Number': 0,
            'Step Number': 0,
            'Step Name': '',
            'Shift': 0,
            'Slide': 0,
            'Rise': 0,
            'Tilt': 0,
            'Roll': 0,
            'Twist': 0,
            'X-Displacement': 0,
            'Y-Displacement': 0,
            'Helical Rise': 0,
            'Inclination': 0,
            'Tip': 0,
            'Helical Twist': 0
        })
        if report:
            self._update(assign_numbers(report))

    @staticmethod
    def report_type() -> str:
        return 'bpsp'

    def model_num(self) -> int:
        return self._report['Model Number']

    def step_num(self) -> int:
        return self._report['Step Number']

    def step_name(self) -> str:
        return self._report['Step Name']

    def shift(self) -> float:
        return self._report['Shift']

    def slide(self) -> float:
        return self._report['Slide']

    def rise(self) -> float:
        return self._report['Rise']

    def tilt(self) -> float:
        return self._report['Tilt']

    def roll(self) -> float:
        return self._report['Roll']

    def x_disp(self) -> float:
        return self._report['X-Displacement']

    def y_disp(self) -> float:
        return self._report['Y-Displacement']

    def helical_rise(self) -> float:
        return self._report['Helical Rise']

    def inclination(self) -> float:
        return self._report['Inclination']

    def tip(self) -> float:
        return self._report['Tip']

    def helical_twist(self) -> float:
        return self._report['Helical Twist']


class DescriptorReport(_AdvancedBaseReport):
    def __init__(self, report: dict = None):
        super().__init__()
        self._update({
            'Structure Description': '',
        })
        if report:
            self._update(report)

    @staticmethod
    def report_type() -> str:
        return 'desc'

    def description(self) -> str:
        return self._report['Structure Description']


class SequencesReport(_AdvancedBaseReport):
    def __init__(self, report: dict = None):
        super().__init__()
        self._update({
            'NA Sequence': '',
            'Structure Description': '',
        })
        if report:
            self._update(report)

    @staticmethod
    def report_type() -> str:
        return 'naSeq'

    def sequence(self) -> str:
        return self._report['NA Sequence']

    def description(self) -> str:
        return self._report['Structure Description']


class StatisticReport(object):
    def __init__(self, report: dict= None):
        self._stats = report

    def get_stats(self):
        return self._stats


class RNA3DBasePairRelFreqReport(_AdvancedBaseReport):
    def __init__(self, report: dict = None):
        super().__init__()
        self._update({
            'PDB ID': '',
            'Relative cWW': 0,
            'Relative tWW': 0,
            'Relative cWH': 0,
            'Relative tWH': 0,
            'Relative cWS': 0,
            'Relative tWS': 0,
            'Relative cHH': 0,
            'Relative tHH': 0,
            'Relative cHS': 0,
            'Relative tHS': 0,
            'Relative cSS': 0,
            'Relative tSS': 0
        })
        if report:
            self._update(assign_numbers(report))

    @staticmethod
    def report_type() -> str:
        return 'bpFreq'

    def pdb_id(self) -> str:
        return self._report['PDB ID']

    def cWW(self) -> float:
        return self._report['Relative cWW']

    def tWW(self) -> float:
        return self._report['Relative tWW']

    def cWH(self) -> float:
        return self._report['Relative cWH']

    def tWH(self) -> float:
        return self._report['Relative tWH']

    def cWS(self) -> float:
        return self._report['Relative cWS']

    def tWS(self) -> float:
        return self._report['Relative tWS']

    def cHH(self) -> float:
        return self._report['Relative cHH']

    def tHH(self) -> float:
        return self._report['Relative tHH']

    def cHS(self) -> float:
        return self._report['Relative cHS']

    def tHS(self) -> float:
        return self._report['Relative tHS']

    def cSS(self) -> float:
        return self._report['Relative cSS']

    def tSS(self) -> float:
        return self._report['Relative tSS']


class RNA3DBasePhosphateRelFreqReport(_AdvancedBaseReport):
    def __init__(self, report: dict = None):
        super().__init__()
        self._update({
            'PDB ID': '',
            'Relative 1BPh': 0,
            'Relative 2BPh': 0,
            'Relative 3BPh': 0,
            'Relative 4BPh': 0,
            'Relative 5BPh': 0,
            'Relative 6BPh': 0,
            'Relative 7BPh': 0,
            'Relative 8BPh': 0,
            'Relative 9BPh': 0,
            'Relative 0BPh': 0
        })
        if report:
            self._update(assign_numbers(report))

    @staticmethod
    def report_type() -> str:
        return 'bphsFreq'

    def pdb_id(self) -> str:
        return self._report['PDB ID']

    def cWW(self) -> float:
        return self._report['Relative cWW']

    def BPh_1(self) -> float:
        return self._report['Relative 1BPh']

    def BPh_2(self) -> float:
        return self._report['Relative 2BPh']

    def BPh_3(self) -> float:
        return self._report['Relative 3BPh']

    def BPh_4(self) -> float:
        return self._report['Relative 4BPh']

    def BPh_5(self) -> float:
        return self._report['Relative 5BPh']

    def BPh_6(self) -> float:
        return self._report['Relative 6BPh']

    def BPh_7(self) -> float:
        return self._report['Relative 7BPh']

    def BPh_8(self) -> float:
        return self._report['Relative 8BPh']

    def BPh_9(self) -> float:
        return self._report['Relative 9BPh']

    def BPh_0(self) -> float:
        return self._report['Relative 0BPh']


class RNA3DBaseStackingRelFreqReport(_AdvancedBaseReport):
    def __init__(self, report: dict = None):
        super().__init__()
        self._update({
            'PDB ID': '',
            'Relative s33': 0,
            'Relative s53': 0,
            'Relative s55': 0
        })
        if report:
            self._update(report)

    @staticmethod
    def report_type() -> str:
        return 'stackFreq'

    def pdb_id(self) -> str:
        return self._report['PDB ID']

    def s33(self) -> float:
        return self._report['Relative s33']

    def s53(self) -> float:
        return self._report['Relative s53']

    def s55(self) -> float:
        return self._report['Relative s55']


class RNA3DMotifReport(_AdvancedBaseReport):
    def __init__(self, report: dict = None):
        super().__init__()
        self._update({
            'PDB ID': '',
            'Motif ID': '',
            'Common Name': '',
            'Annotation': ''
        })
        if report:
            self._update(report)

    @staticmethod
    def report_type() -> str:
        return 'motif'

    def pdb_id(self) -> str:
        return self._report['PDB ID']

    def motif_id(self) -> str:
        return self._report['Motif ID']

    def common_name(self) -> str:
        return self._report['Common Name']

    def annotation(self) -> str:
        return self._report['Annotation']


AdvancedReport = TypeVar('AdvancedReport', NDBStatusReport, CellDimensionsReport, CitationReport, RefinementDataReport,
                         NABackboneTorsionReport, BasePairParameterReport, BasePairStepParameterReport,
                         DescriptorReport, SequencesReport, StatisticReport, RNA3DBasePairRelFreqReport,
                         RNA3DBasePhosphateRelFreqReport, RNA3DBaseStackingRelFreqReport, RNA3DMotifReport)
