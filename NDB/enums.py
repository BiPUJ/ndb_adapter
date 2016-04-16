from enum import Enum
from NDB.search_report import *


class ReportType(Enum):
    NDBStatus = NDBStatusReport
    CellDimensions = CellDimensionsReport
    Citation = CitationReport
    RefinementData = RefinementDataReport
    NABackboneTorsion = NABackboneTorsionReport
    BasePairParameter = BasePairParameterReport
    BasePairStepParameter = BasePairStepParameterReport
    Descriptor = DescriptorReport
    Sequences = SequencesReport
    RNABasePairRelFreq = RNA3DBasePairRelFreqReport
    RNABasePhosphateRelFreq = RNA3DBasePhosphateRelFreqReport
    RNABaseStackingRelFreq = RNA3DBaseStackingRelFreqReport
    RNAMotif = RNA3DMotifReport


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
    Nothing = ''
    All = 'all'
    OneHalf = '1.5'
    Two = '2.0'
    TwoHalf = '2.5'
    Three = '3.0'
    ThreeHalf = '3.5'
    Four = '4.0'
    Twenty = '20.0'


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


class GreaterLower(Enum):
    GreaterEqual = 'gtEq'
    LowerEqual = 'ltEq'


class GreaterLowerEqual(Enum):
    Equal = 'eq'
    GreaterEqual = 'gtEq'
    LowerEqual = 'ltEq'


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


class SpaceGroup(Enum):
    Nothing = ''
    B_2_21_2 = 'B 2 21 2'
    C_1_2_1 = 'C 1 2 1'
    C_2_2_2 = 'C 2 2 2'
    C_2_2_21 = 'C 2 2 21'
    F_2_2_2 = 'F 2 2 2'
    F_2_3 = 'F 2 3'
    F_4_3_2 = 'F 4 3 2'
    H_3 = 'H 3'
    H_3_2 = 'H 3 2'
    I_2_2_2 = 'I 2 2 2'
    I_2_3 = 'I 2 3'
    I_21_21_21 = 'I 21 21 21'
    I_21_3 = 'I 21 3'
    I_4 = 'I 4'
    I_4_2_2 = 'I 4 2 2'
    I_4_3_2 = 'I 4 3 2'
    I_41 = 'I 41'
    I_41_2_2 = 'I 41 2 2'
    I_41_3_2 = 'I 41 3 2'
    P_minus1 = 'P -1'
    P_1 = 'P 1'
    P_1_1_21 = 'P 1 1 21'
    P_1_2_1 = 'P 1 2 1'
    P_1_21_1 = 'P 1 21 1'
    P_2_2_21 = 'P 2 2 21'
    P_2_21_21 = 'P 2 21 21'
    P_2_3 = 'P 2 3'
    P_21_2_21 = 'P 21 2 21'
    P_21_21_2 = 'P 21 21 2'
    P_21_21_21 = 'P 21 21 21'
    P_21_3 = 'P 21 3'
    P_3 = 'P 3'
    P_3_1_2 = 'P 3 1 2'
    P_3_2_1 = 'P 3 2 1'
    P_31 = 'P 31'
    P_31_1_2 = 'P 31 1 2'
    P_31_2_1 = 'P 31 2 1'
    P_32 = 'P 32'
    P_32_1_2 = 'P 32 1 2'
    P_32_2_1 = 'P 32 2 1'
    P_4 = 'P 4'
    P_4_2_2 = 'P 4 2 2'
    P_4_21_2 = 'P 4 21 2'
    P_41 = 'P 41'
    P_41_2_2 = 'P 41 2 2'
    P_41_21_2 = 'P 41 21 2'
    P_41_3_2 = 'P 41 3 2'
    P_42 = 'P 42'
    P_42_2_2 = 'P 42 2 2'
    P_42_21_2 = 'P 42 21 2'
    P_42_3_2 = 'P 42 3 2'
    P_43 = 'P 43'
    P_43_2_2 = 'P 43 2 2'
    P_43_21_2 = 'P 43 21 2'
    P_43_3_2 = 'P 43 3 2'
    P_6 = 'P 6'
    P_6_2_2 = 'P 6 2 2'
    P_61 = 'P 61'
    P_61_2_2 = 'P 61 2 2'
    P_62 = 'P 62'
    P_62_2_2 = 'P 62 2 2'
    P_63 = 'P 63'
    P_63_2_2 = 'P 63 2 2'
    P_64 = 'P 64'
    P_64_2_2 = 'P 64 2 2'
    P_65 = 'P 65'
    P_65_2_2 = 'P 65 2 2'
    R_3_2 = 'R 3 2'


class RFactor(Enum):
    Nothing = ''
    Zero_Ten = '10'
    Zero_Fifteen = '15'
    Zero_Twenty = '20'
    Zero_TwentyFive = '25'
    Zero_Thirty = '30'
    Zero_ThirtyFive = '35'


class BasePair(Enum):
    """Enum for base pair interaction

        :cvar Nothing: empty value
        :cvar cWW: (cis Watson-Crick/Watson-Crick)
        :cvar tWW: (trans Watson-Crick/Watson-Crick)
        :cvar cWH: (cis Watson-Crick/Hoogsteen)
        :cvar tWH: (trans Watson-Crick/Hoogsteen)
        :cvar cWS: (cis Watson-Crick/Sugar Edge)
        :cvar tWS: (trans Watson-Crick/Sugar Edge)
        :cvar cHH: (cis Hoogsteen/Hoogsteen)
        :cvar tHH: (trans Hoogsteen/Hoogsteen)
        :cvar cHS: (cis Hoogsteen/Sugar Edge)
        :cvar tHS: (trans Hoogsteen/Sugar Edge)
        :cvar cSS: (cis Sugar Edge/Sugar Edge)
        :cvar tSS: (trans Sugar Edge/Sugar Edge)
    """
    Nothing = ''
    cWW = 'cWW'
    tWW = 'tWW'
    cWH = 'cWH'
    tWH = 'tWH'
    cWS = 'cWS'
    tWS = 'tWS'
    cHH = 'cHH'
    tHH = 'tHH'
    cHS = 'cHS'
    tHS = 'tHS'
    cSS = 'cSS'
    tSS = 'tSS'


class BasePhosphate(Enum):
    """Enum for base phosphate interaction

        :cvar Nothing: empty values
        :cvar BPh_1: 1BPh (base-phosphate position 1)
        :cvar BPh_2: 2BPh (base-phosphate position 2)
        :cvar BPh_3: 3BPh (base-phosphate position 3)
        :cvar BPh_4: 4BPh (base-phosphate position 4)
        :cvar BPh_5: 5BPh (base-phosphate position 5)
        :cvar BPh_6: 6BPh (base-phosphate position 6)
        :cvar BPh_7: 7BPh (base-phosphate position 7)
        :cvar BPh_8: 8BPh (base-phosphate position 8)
        :cvar BPh_9: 9BPh (base-phosphate position 9)
        :cvar BPh_0: 0BPh (base-phosphate position 10)
    """
    Nothing = ''
    BPh_1 = '1BPh'
    BPh_2 = '2BPh'
    BPh_3 = '3BPh'
    BPh_4 = '4BPh'
    BPh_5 = '5BPh'
    BPh_6 = '6BPh'
    BPh_7 = '7BPh'
    BPh_8 = '8BPh'
    BPh_9 = '9BPh'
    BPh_0 = '0BPh'


class BaseStack(Enum):
    """Enum for base stack interaction

        :cvar Nothing: empty value
        :cvar s_33: s33 (stack, 3′ face on 3′ face)
        :cvar s_35: s35 (stack, 3′ face on 5′ face)
        :cvar s_55: s55 (stack, 5′ face on 5′ face)
    """
    Nothing = ''
    s_33 = 's33'
    s_35 = 's35'
    s_55 = 's55'


class InternalLoopMotif(Enum):
    """Enum for internal loop motif

        :cvar Nothing: empty value
        :cvar All: all motifs
        :cvar SarcinRicin: Sarcin-ricin motif
        :cvar KinkTurn: Kink-turn motif
        :cvar CLoop: C-loop motif
        :cvar DoubleSheared: Double-sheared motif
        :cvar TripleSheared: Triple-sheared motif
    """
    Nothing = ''
    All = 'All'
    SarcinRicin = 'Sarcin-ricin'
    KinkTurn = 'Kink-turn'
    CLoop = 'C-loop'
    DoubleSheared = 'Double-sheared'
    TripleSheared = 'Triple-sheared'


class HairpinLoopMotif(Enum):
    """Enum for hairpin loop motif

        :cvar Nothing: empty value
        :cvar All: all motifs
        :cvar TLoop: T-loop motif
        :cvar GNRA: GNRA motif
        :cvar UNCG: UNCG motif
    """
    Nothing = ''
    All = 'All'
    TLoop = 'T-loop'
    GNRA = 'GNRA'
    UNCG = 'UNCG'


class EnzymeFunction(Enum):
    Nothing = ''
    All = 'ENZYME'
    Topoisomerase = 'TOPOISOMERASE'
    Synthetase = 'SYNTHETASE'
    Thrombin = 'THROMBIN'
    DNAPolymerase = 'DNA POLYMERASE'
    DNAReverseTranscriptase = 'DNA POLYMERASE/REVERSE TRANSCRIPTASE'
    DNAEndonuclease = 'DNA NUCLEASE/ENDONUCLEASE'
    DNAExonuclease = 'DNA NUCLEASE/EXONUCLEASE'
    Glycosylase = 'GLYCOSYLASE'
    Helicase = 'HELICASE'
    Kinase = 'KINASE'
    Ligase = 'LIGASE'
    Lyase = 'LYASE'
    MethylaseMethytransferase = 'METHYLASE OR METHYLTRANSFERASE'
    mRNACapping = 'MRNA CAPPING'
    Phosphatase = 'PHOSPHATASE'
    Integrase = 'RECOMBINASE/INTEGRASE'
    Invertase = 'RECOMBINASE/INVERTASE'
    Resolvase = 'RECOMBINASE/RESOLVASE'
    Transposase = 'RECOMBINASE/TRANSPOSASE'
    RecombinaseOther = 'RECOMBINASE/OTHER'
    RNAPolymerase = 'RNA POLYMERASE'
    RNAEndonuclease = 'RNA NUCLEASE/ENDONUCLEASE'
    RNAExonuclease = 'RNA NUCLEASE/EXONUCLEASE'
    tRNAModifying = 'TRNA MODIFYING'
    Other = 'OTHER'


class RegulatoryFunction(Enum):
    Nothing = ''
    All = 'REGULATORY'
    DnaRepairActivator = 'DNA Repair Activator'
    DnaRepairRepressor = 'DNA Repair Repressor'
    RecombinationActivator = 'Recombination Activator'
    RecombinationReporessor = 'Recombination Repressor'
    ReplicationActivator = 'Replication Factor/Activator'
    ReplicationReporessor = 'Replication Factor/Repressor'
    SpliceosomalProtein = 'Spliceosomal Protein'
    TranscriptionActivatorRepressor = 'Transcription Factor/Activator And Repressor'
    TranscriptionActivator = 'Transcription Factor/Activator'
    TranscriptionCoactivator = 'Transcription Factor/Coactivator'
    TranscriptionCorepressor = 'Transcription Factor/Corepressor'
    TranscriptionElongation = 'Transcription Factor/Elongation'
    Transcription = 'Transcription Factor/General'
    TranscriptionReporessor = 'Transcription Factor/Repressor'
    TranscriptionTermination = 'Transcription Factor/Termination'
    TranslationElongation = 'Translation Factor/Elongation'
    TranslationInitiator = 'Translation Factor/Initiator'
    TranslationTermination = 'Translation Factor/Termination'


class StructuralFunction(Enum):
    Nothing = ''
    All = 'STRUCTURAL'
    Chromosomal = 'Chromosomal'
    Histone = 'Histone'
    HMG = 'HMG'
    Ribonucleoprotein = 'Ribonucleoprotein'
    RibosomalProtein = 'Ribosomal Protein'
    SignalRecognitionParticle = 'Signal Recognition Particle'
    TelomereBinding = 'Telomere Binding'
    ViralCoat = 'Viral Coat'


class OtherFunction(Enum):
    Nothing = ''
    All = 'OTHER'
    Antibiotic = 'Antibiotic'
    Antibody = 'Antibody'
    Other = 'Other'


class NaFeature(Enum):
    Nothing = ''
    All = 'loop'
    HairpinLoop = 'hairpin loop'
    InternalLoop = 'internal loop'
    Bulge = 'bulge'
    Hammerhead = 'hammerhead'
    ThreeWayJunction = 'three_way_junction'
    FourWayJunction = 'holliday_junction'
    NonWatsonCrickBaseParing ='type_11_pair'
    MismatchBaseParing = 'mismat'


class StrandDescription(Enum):
    Nothing = ''
    DoubleHelix = 'double helix'
    TripleHelix = 'triple helix'
    QuadrupleHelix = 'quadruple helix'


class ConformationType(Enum):
    Nothing = ''
    All = 'all'
    A = 'A'
    B = 'B'
    RH = 'RH'
    T = 'T'
    U = 'U'
    Z = 'Z'
