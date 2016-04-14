from enum import Enum


class ReportType(Enum):
    NDBStatus = 'ndbStatus'
    CellDimensions = 'cellDim'
    Citation = 'citation'
    RefinementData = 'ref'
    NABackboneTorsion = 'nabt'
    BasePairParameter = 'bpp'
    BasePairStepParameter = 'bpsp'
    Descriptor = 'desc'
    Sequences = 'naSeq'
    RNA3DBasePairRelFreq = 'bpFreq'
    RNA3DBasePhosphateRelFreq = 'bphsFreq'
    RNA3DBaseStackingRelFreq = 'stackFreq'
    RNAMotif = 'motif'


class Polymer(Enum):
    All = 'all'
    DNAOnly = 'onlyDna'
    ProteinDNA = 'protDna'
    DrugDNA = 'drugDna'
    HybridsChimera = 'hybNChimera'
    PeptideNucleicAcid = 'pepNucAcid'


class ProteinFunc(Enum):
    All = 'all'
    Enzymes = 'enzymes'
    Structural = 'structural'
    Regulatory = 'regulatory'
    Other = 'other'


class StructuralFeatures(Enum):
    All = 'all'
    SingleStranded = 'single'
    aDNA = 'A'
    bDNA = 'B'
    zDNA = 'Z'
    OtherDoubleHelical = 'other'
    TripleHelices = 'triple'
    QuadrupleHelices = 'quadruple'


class ExpMethod(Enum):
    All = 'all'
    XRAY = 'x-ray'
    NMR = 'nmr'


class RnaStructures(Enum):
    All = 'all'
    NonRedundant = 'nr'


class ResolutionCutoff(Enum):
    All = 'all'
    OneHalfA = '1.5'
    TwoA = '2.0'
    TwoHalfA = '2.5'
    ThreeA = '3.0'
    ThreeHalfA = '3.5'
    FourA = '4.0'
    TwentyA = '20.0'


class RnaType(Enum):
    All = 'all'
    tRNA = 'trna'
    tRNAFrag = 'trnaFr'
    Ribosome = 'ribosome'
    Ribozyme = 'ribozyme'
    Harpin = 'hairpin'
    Hammerhead = 'hammhd'
    Group1Intron = 'gr1In'
    Group2Intron = 'gr2In'
    RnaseP = 'rnase'
    Polymerase = 'polymerase'
    Ligase = 'ligase'
    Leadzyme = 'leadzyme'
    RibozymeFrag = 'ribozymeFr'
    Virus = 'virus'
    ViralFrag = 'viralfr'
    Riboswitch = 'riboswitch'
    RiboswitchFrag = 'riboswitchFr'
    Aptamer = 'aptamer'
    Telomerase = 'telomerase'
    SmallNucleotideFrag = 'singleStranded'
    DoubleHelices = 'duplex'
    TripleHelices = 'triplexes'
    QuadrupleHelices = 'quadruplexes'


class YesNoIgnore(Enum):
    Yes = 'Y'
    No = 'N'
    Ignore = 'Ignore'


class AndOr(Enum):
    And = "AND"
    Or = "OR"


class DnaRnaEither(Enum):
    DNA = 'DNA'
    RNA = 'RNA'
    Either = 'EITHER'


class GreaterLowerEqual(Enum):
    GreaterEqual = 'gtEq'
    LowerEqual = 'ltEq'
    Equal = 'eq'


class DrugBinding(Enum):
    Intercalation = 'Intercalation'
    OutsideBinder = 'Outside binder'
    IntercalationCovalent = 'Intercalation, Covalent'
    OutsideBinderCovalent = 'Outside binder, Covalent'
    MajorGrooveBinder = 'Major Groove Binder'
    MinorGrooveBinder = 'Minor Groove Binder'
    MajorGrooveBinderCovalent = 'Major Groove Binder, Covalent'
    MinorGrooveBinderCovalent = 'Minor Groove Binder, Covalent'
    IntercalationMajorGrooveBinder = 'Intercalation, Major Groove Binder'
    IntercalationMinorGrooveBinder = 'Intercalation, Minor Groove Binder'
    BisIntercalation = 'Bis-Intercalation'
    DoubleMajorGrooveBinder = 'Double Major Groove Binder'
    DoubleMinorGrooveBinder = 'Double Minor Groove Binder'
    CovalentMetalBonds = 'Covalent Metal Bonds'
