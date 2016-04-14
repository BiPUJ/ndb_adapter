from NDB.enums import Polymer, ProteinFunc, ExpMethod


class SearchOptions(object):
    def __init__(self, search_type: str):
        self._options = {
            'strGalType': search_type,
            'galType': 'table',
            'limit': '10',
            'start': '0',
            'polType': Polymer.All.value,
            'protFunc': ProteinFunc.All.value,
            'expMeth': ExpMethod.All.value,
            'filterTxt': ''
        }

    def _update(self, options) -> None:
        self._options.update(options)

    def set_polymer(self, polymer: Polymer) -> None:
        self._options['polType'] = polymer.value

    def get_polymer(self) -> Polymer:
        return Polymer(self._options['polType'])

    def set_protein_func(self, protein: ProteinFunc) -> None:
        self._options['protFunc'] = protein.value

    def get_protein_func(self) -> ProteinFunc:
        return ProteinFunc(self._options['protFunc'])

    def set_experimental_method(self, method: ExpMethod) -> None:
        self._options['expMeth'] = method.value

    def get_experimental_method(self) -> ExpMethod:
        return ExpMethod(self._options['expMeth'])

    def set_filter_text(self, text: str) -> None:
        self._options['filterTxt'] = text

    def get_filter_text(self) -> str:
        return self._options['filterTxt']

    def get(self) -> dict:
        return self._options

    def __str__(self):
        return str(self._options)
