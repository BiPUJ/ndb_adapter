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


