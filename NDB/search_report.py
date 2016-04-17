from typing import TypeVar


def _assign_numbers(dic: dict):
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
            'Resolution': 0,
            'R work': 0,
            'R free': 0
        }
        if report:
            self._report.update(report)

    @property
    def pdb_id(self) -> str:
        return self._report['PDB ID']

    @property
    def ndb_id(self) -> str:
        return self._report['NDB ID']

    @property
    def title(self) -> str:
        return self._report['Title']

    @property
    def classification(self) -> str:
        return self._report['Classification']

    @property
    def release_date(self) -> str:
        return self._report['PDB Release Date']

    @property
    def authors(self) -> str:
        return self._report['Authors']

    @property
    def citation_title(self) -> str:
        return self._report['Citation Title']

    @property
    def citation_detail(self) -> str:
        return self._report['Citation Detail']

    @property
    def experimental_method(self) -> str:
        return self._report['Experiment']

    @property
    def resolution(self) -> float:
        return self._report['Resolution']

    @property
    def r_work(self) -> float:
        return self._report['R work']

    @property
    def r_free(self) -> float:
        return self._report['R free']

    @property
    def dict(self) -> dict:
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

    @property
    def ndb_id(self) -> str:
        return self._report['NDB ID']

    @property
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

    @property
    def pdb_id(self) -> str:
        return self._report['PDB ID']

    @property
    def title(self) -> str:
        return self._report['Title']

    @property
    def release_date(self) -> str:
        return self._report['NDB Release Date']

    @property
    def deposition_date(self) -> str:
        return self._report['Initial Deposition Date']

    @property
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
            self._update(_assign_numbers(report))

    @staticmethod
    def report_type() -> str:
        return 'cellDim'

    @property
    def cell_a(self) -> float:
        return self._report['Length A']

    @property
    def cell_b(self) -> float:
        return self._report['Length B']

    @property
    def cell_c(self) -> float:
        return self._report['Length C']

    @property
    def cell_alpha(self) -> float:
        return self._report['Angle Alpha']

    @property
    def cell_beta(self) -> float:
        return self._report['Angle Beta']

    @property
    def cell_gamma(self) -> float:
        return self._report['Angle Gamma']

    @property
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
            self._update(_assign_numbers(report))

    @staticmethod
    def report_type() -> str:
        return 'citation'

    @property
    def pdb_id(self) -> str:
        return self._report['PDB ID']

    @property
    def citation_title(self) -> str:
        return self._report['Citation Title']

    @property
    def citation_authors(self) -> str:
        return self._report['Citation Authors']

    @property
    def journal(self) -> str:
        return self._report['Journal']

    @property
    def pubmed_id(self) -> str:
        return self._report['Pubmed ID']

    @property
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
            self._update(_assign_numbers(report))

    @staticmethod
    def report_type() -> str:
        return 'ref'

    @property
    def r_work(self) -> float:
        return self._report['R-value_work']

    @property
    def r_obs(self) -> float:
        return self._report['R-value_obs']

    @property
    def r_free(self) -> float:
        return self._report['R-value_free']

    @property
    def higher_resolution(self) -> float:
        return self._report['Higher Resolution Limit']

    @property
    def lower_resolution(self) -> float:
        return self._report['Lower Resolution Limit']

    @property
    def reflections(self) -> int:
        return self._report['Reflections Observed']

    @property
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
            self._update(_assign_numbers(report))

    @staticmethod
    def report_type() -> str:
        return 'nabt'

    @property
    def model_id(self) -> str:
        return self._report['Model ID']

    @property
    def chain_id(self) -> str:
        return self._report['Chain ID']

    @property
    def residue_number(self) -> int:
        return self._report['Residue Num']

    @property
    def residue_name(self) -> str:
        return self._report['Residue Name']

    @property
    def o3_p_o5_c5(self) -> float:
        return self._report["O3'-P-O5'-C5'"]

    @property
    def p_o5_c5_c4(self) -> float:
        return self._report["P-O5'-C5'-C4'"]

    @property
    def o5_c5_c4_c3(self) -> float:
        return self._report["O5'-C5'-C4'-C3'"]

    @property
    def c5_c4_c3_o3(self) -> float:
        return self._report["C5'-C4'-C3'-O3'"]

    @property
    def c4_c3_o3_p(self) -> float:
        return self._report["C4'-C3'-O3'-P"]

    @property
    def c3_o3_p_o5(self) -> float:
        return self._report["C3'-O3'-P-O5'"]

    @property
    def o4_c1_n1_9_c2_4(self) -> float:
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
            self._update(_assign_numbers(report))

    @staticmethod
    def report_type() -> str:
        return 'bpp'

    @property
    def model_num(self) -> int:
        return self._report['Model Number']

    @property
    def pair_num(self) -> int:
        return self._report['Pair Number']

    @property
    def pair_name(self) -> str:
        return self._report['Pair Name']

    @property
    def shear(self) -> float:
        return self._report['Shear']

    @property
    def stretch(self) -> float:
        return self._report['Stretch']

    @property
    def stagger(self) -> float:
        return self._report['Stagger']

    @property
    def buckle(self) -> float:
        return self._report['Buckle']

    @property
    def propellor(self) -> float:
        return self._report['Propellor']

    @property
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
            self._update(_assign_numbers(report))

    @staticmethod
    def report_type() -> str:
        return 'bpsp'

    @property
    def model_num(self) -> int:
        return self._report['Model Number']

    @property
    def step_num(self) -> int:
        return self._report['Step Number']

    @property
    def step_name(self) -> str:
        return self._report['Step Name']

    @property
    def shift(self) -> float:
        return self._report['Shift']

    @property
    def slide(self) -> float:
        return self._report['Slide']

    @property
    def rise(self) -> float:
        return self._report['Rise']

    @property
    def tilt(self) -> float:
        return self._report['Tilt']

    @property
    def roll(self) -> float:
        return self._report['Roll']

    @property
    def x_disp(self) -> float:
        return self._report['X-Displacement']

    @property
    def y_disp(self) -> float:
        return self._report['Y-Displacement']

    @property
    def helical_rise(self) -> float:
        return self._report['Helical Rise']

    @property
    def inclination(self) -> float:
        return self._report['Inclination']

    @property
    def tip(self) -> float:
        return self._report['Tip']

    @property
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

    @property
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

    @property
    def sequence(self) -> str:
        return self._report['NA Sequence']

    @property
    def description(self) -> str:
        return self._report['Structure Description']


class StatisticReport(object):
    def __init__(self, report: dict= None):
        self._stats = report

    @property
    def stats(self):
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
            self._update(_assign_numbers(report))

    @staticmethod
    def report_type() -> str:
        return 'bpFreq'

    @property
    def pdb_id(self) -> str:
        return self._report['PDB ID']

    @property
    def cww(self) -> float:
        return self._report['Relative cWW']

    @property
    def tww(self) -> float:
        return self._report['Relative tWW']

    @property
    def cwh(self) -> float:
        return self._report['Relative cWH']

    @property
    def twh(self) -> float:
        return self._report['Relative tWH']

    @property
    def cws(self) -> float:
        return self._report['Relative cWS']

    @property
    def tws(self) -> float:
        return self._report['Relative tWS']

    @property
    def chh(self) -> float:
        return self._report['Relative cHH']

    @property
    def thh(self) -> float:
        return self._report['Relative tHH']

    @property
    def chs(self) -> float:
        return self._report['Relative cHS']

    @property
    def ths(self) -> float:
        return self._report['Relative tHS']

    @property
    def css(self) -> float:
        return self._report['Relative cSS']

    @property
    def tss(self) -> float:
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
            self._update(_assign_numbers(report))

    @staticmethod
    def report_type() -> str:
        return 'bphsFreq'

    @property
    def pdb_id(self) -> str:
        return self._report['PDB ID']

    @property
    def cww(self) -> float:
        return self._report['Relative cWW']

    @property
    def bph_1(self) -> float:
        return self._report['Relative 1BPh']

    @property
    def bph_2(self) -> float:
        return self._report['Relative 2BPh']

    @property
    def bph_3(self) -> float:
        return self._report['Relative 3BPh']

    @property
    def bph_4(self) -> float:
        return self._report['Relative 4BPh']

    @property
    def bph_5(self) -> float:
        return self._report['Relative 5BPh']

    @property
    def bph_6(self) -> float:
        return self._report['Relative 6BPh']

    @property
    def bph_7(self) -> float:
        return self._report['Relative 7BPh']

    @property
    def bph_8(self) -> float:
        return self._report['Relative 8BPh']

    @property
    def bph_9(self) -> float:
        return self._report['Relative 9BPh']

    @property
    def bph_0(self) -> float:
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
            self._update(_assign_numbers(report))

    @staticmethod
    def report_type() -> str:
        return 'stackFreq'

    @property
    def pdb_id(self) -> str:
        return self._report['PDB ID']

    @property
    def s33(self) -> float:
        return self._report['Relative s33']

    @property
    def s53(self) -> float:
        return self._report['Relative s53']

    @property
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

    @property
    def pdb_id(self) -> str:
        return self._report['PDB ID']

    @property
    def motif_id(self) -> str:
        return self._report['Motif ID']

    @property
    def common_name(self) -> str:
        return self._report['Common Name']

    @property
    def annotation(self) -> str:
        return self._report['Annotation']


AdvancedReport = TypeVar('AdvancedReport', NDBStatusReport, CellDimensionsReport, CitationReport, RefinementDataReport,
                         NABackboneTorsionReport, BasePairParameterReport, BasePairStepParameterReport,
                         DescriptorReport, SequencesReport, StatisticReport, RNA3DBasePairRelFreqReport,
                         RNA3DBasePhosphateRelFreqReport, RNA3DBaseStackingRelFreqReport, RNA3DMotifReport)
