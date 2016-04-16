from NDB.enums import RnaType, RnaStructures, ResolutionCutoff
from NDB.search_options import SearchOptions


class RnaSearchOptions(SearchOptions):
    def __init__(self):
        super().__init__('rna')
        self._update({'rnaFunc': '',
                      'seqType': RnaStructures.All.value,
                      'nrResVal': ResolutionCutoff.All.value})

    def set_rna_type(self, rna_type: RnaType= RnaType.All) -> None:
        self._update({'rnaFunc': rna_type.value})

    def get_rna_type(self) -> RnaType:
        return RnaType(self._options['rnaFunc'])

    def set_non_redundant_list(self, structures: RnaStructures = RnaStructures.All,
                               resolution: ResolutionCutoff = ResolutionCutoff.All) -> None:
        self._update({'seqType': structures.value,
                      'nrResVal': resolution.value})

    def get_non_redundant_list(self) -> (RnaStructures, ResolutionCutoff):
        return RnaStructures(self._options['seqType']), ResolutionCutoff(self._options['nrResVal'])
