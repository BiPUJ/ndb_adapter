from NDB.enums import StructuralFeatures
from NDB.search_options import SearchOptions


class DnaSearchOptions(SearchOptions):
    def __init__(self):
        super().__init__('dna')
        self._update({'stFeature': StructuralFeatures.All.value})

    def set_structural_features(self, structural: StructuralFeatures) -> None:
        self._update({'stFeature': structural.value})

    def get_structural_features(self) -> StructuralFeatures:
        return StructuralFeatures(self._options['stFeature'])
