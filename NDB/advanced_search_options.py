from datetime import date, datetime
from NDB.enums import ReportType, YesNoIgnore, AndOr, DnaRnaEither, GreaterLowerEqual, DrugBinding, SpaceGroup, \
    RFactor, BasePair, BasePhosphate, BaseStack, GreaterLower, InternalLoopMotif, HairpinLoopMotif, ResolutionCutoff, \
    EnzymeFunction, RegulatoryFunction, StructuralFunction, OtherFunction, NaFeature, StrandDescription, \
    ConformationType
from typing import List, Optional


class AdvancedSearchOptions(object):
    def __init__(self, report_type: ReportType = ReportType.NDBStatus):
        self._options = {
            'search_report': report_type.value,
        }
        self.reset()

    def reset(self) -> None:
        """
        Reset advanced search options to defaults

        :return: None
        :rtype: None
        """
        self._options.update({
            'q_nasct_des': [],
            'q_prbmd_sfn': [],
            'i_prbmd_ofn': AndOr.And.value,
            'c_detal_rfc': AndOr.And.value,
            'q_detal_res': '',
            'q_biocn_lid': '',
            'q_biocn_lig': YesNoIgnore.Ignore.value,
            'c_biocn_drg': AndOr.And.value,
            'c_citat_ann': AndOr.And.value,
            'c_detal_anb': AndOr.And.value,
            'c_detal_ana': AndOr.And.value,
            'c_bph_int': AndOr.And.value,
            'c_detal_ang': AndOr.And.value,
            'c_detal_lnc': AndOr.And.value,
            'c_bph_count': '',
            'q_seqnc': '',
            'i_nasct_des': AndOr.Or.value,
            'q_biocn_hyb': YesNoIgnore.Ignore.value,
            'q_detal_grp': SpaceGroup.Nothing.value,
            'c_prbmd_oth': AndOr.And.value,
            'c_bp_count': '',
            'c_etype_sfc': AndOr.And.value,
            'c_etype_nmr': AndOr.And.value,
            'q_biocn_rna': YesNoIgnore.Ignore.value,
            'c_biocn_pro': AndOr.And.value,
            'q_bph_f_op': GreaterLower.GreaterEqual.value,
            'q_bp_count': '',
            'c_nasct_ftr': AndOr.And.value,
            'q_detal_vla': '',
            'q_detal_vlb': '',
            'q_detal_vlc': '',
            'c_prbmd_reg': AndOr.And.value,
            'c_namod_bas': AndOr.And.value,
            'q_biocn_drg': YesNoIgnore.Ignore.value,
            'q_namod_sgr': YesNoIgnore.Ignore.value,
            'q_bph_f_int': BasePhosphate.Nothing.value,
            'c_bs_f_count': AndOr.And.value,
            'c_bs_count': '',
            'q_etype_nra': YesNoIgnore.Ignore.value,
            'q_bph_int': BasePhosphate.Nothing.value,
            'c_bp_int': AndOr.And.value,
            'q_detal_olc': GreaterLowerEqual.Equal.value,
            'q_detal_vag': '',
            'c_bs_int': AndOr.And.value,
            'q_prbmd_efn': [],
            'q_detal_vab': '',
            'q_detal_vaa': '',
            'q_detal_oab': GreaterLowerEqual.Equal.value,
            'i_prbmd_sfn': AndOr.And.value,
            'q_detal_oaa': GreaterLowerEqual.Equal.value,
            'q_bp_f_op': GreaterLower.GreaterEqual.value,
            'q_detal_oag': GreaterLowerEqual.Equal.value,
            'q_hairpin_motif': [],
            'q_bp_f_int': BasePair.Nothing.value,
            'q_namod_phs': YesNoIgnore.Ignore.value,
            'c_int_motif': AndOr.And.value,
            'q_authr': '',
            'c_nr_list': AndOr.And.value,
            'c_detal_res': AndOr.And.value,
            'q_citat_ann': '',
            'c_authr': AndOr.And.value,
            'q_etype_cry': YesNoIgnore.Ignore.value,
            'c_bp_f_count': AndOr.And.value,
            'q_etype_nmr': YesNoIgnore.Ignore.value,
            'q_int_motif': [],
            'c_etype_cry': AndOr.And.value,
            'q_bph_count': '',
            'q_bp_int': BasePair.Nothing.value,
            'q_nr_list': ResolutionCutoff.Nothing.value,
            'c_biocn_dna': AndOr.And.value,
            'q_prbmd_rfn': [],
            'q_prbmd_enz': DnaRnaEither.Either.value,
            'i_hairpin_motif': AndOr.Or.value,
            'q_bs_int': BaseStack.Nothing.value,
            'q_detal_ola': GreaterLowerEqual.Equal.value,
            'c_biocn_lnm': AndOr.And.value,
            'q_detal_olb': GreaterLowerEqual.Equal.value,
            'q_nasct_typ': ConformationType.Nothing.value,
            'q_bs_op': '',
            'c_biocn_hyb': AndOr.And.value,
            'q_biocn_pro': YesNoIgnore.Ignore.value,
            'c_etype_nra': AndOr.And.value,
            'q_bs_f_int': BaseStack.Nothing.value,
            'q_etype_sfc': YesNoIgnore.Ignore.value,
            'c_biocn_rna': AndOr.And.value,
            'q_prbmd_reg': DnaRnaEither.Either.value,
            'i_nasct_ftr': AndOr.And.value,
            'c_detal_grp': AndOr.And.value,
            'q_citat_rel': '',
            'c_biocn_lig': AndOr.And.value,
            'c_prbmd_enz': AndOr.And.value,
            'c_nasct_des': AndOr.And.value,
            'c_hairpin_motif': AndOr.And.value,
            'q_lnmin': '',
            'q_prbmd_str': DnaRnaEither.Either.value,
            'q_biocn_dbt': [],
            'i_prbmd_efn': AndOr.And.value,
            'q_nasct_ftr': [],
            'c_seqln': AndOr.And.value,
            'c_citat_rel': AndOr.And.value,
            'q_prbmd_ofn': [],
            'q_bs_f_op': GreaterLower.GreaterEqual.value,
            'c_namod_phs': AndOr.And.value,
            'c_prbmd_str': AndOr.And.value,
            'q_bs_count': '',
            'c_biocn_lid': AndOr.And.value,
            'q_biocn_dna': YesNoIgnore.Ignore.value,
            'c_nasct_typ': AndOr.And.value,
            'q_namod_bas': YesNoIgnore.Ignore.value,
            'c_detal_lnb': AndOr.And.value,
            'c_namod_sgr': AndOr.And.value,
            'q_prbmd_oth': DnaRnaEither.Either.value,
            'c_detal_lna': AndOr.And.value,
            'i_prbmd_rfn': AndOr.And.value,
            'q_bp_op': '',
            'i_biocn_dbt': AndOr.And.value,
            'c_seqnc': AndOr.And.value,
            'q_ndbid': '',
            'q_bp_f_count': 0.1,
            'q_bs_f_count': 0.1,
            'q_biocn_lnm': '',
            'q_bph_f_count': 0.1,
            'q_lnmax': '',
            'q_pdbid': '',
            'q_bph_op': '',
            'c_bph_f_count': AndOr.And.value,
            'i_int_motif': AndOr.Or.value,
            'q_detal_rfc': RFactor.Nothing.value,
            'chkAllStructure': 'on',
            'repType': 'csv'
        })

    def set_dna(self, and_or: AndOr = AndOr.And, yes_no_ignore: YesNoIgnore = YesNoIgnore.Ignore) -> None:
        self._options['c_biocn_dna'] = and_or.value
        self._options['q_biocn_dna'] = yes_no_ignore.value

    def get_dna(self) -> (AndOr, YesNoIgnore):
        return AndOr(self._options['c_biocn_dna']), YesNoIgnore(self._options['q_biocn_dna'])

    def set_rna(self, and_or: AndOr = AndOr.And, yes_no_ignore: YesNoIgnore = YesNoIgnore.Ignore) -> None:
        self._options['c_biocn_rna'] = and_or.value
        self._options['q_biocn_rna'] = yes_no_ignore.value

    def get_rna(self) -> (AndOr, YesNoIgnore):
        return AndOr(self._options['c_biocn_rna']), YesNoIgnore(self._options['q_biocn_rna'])

    def set_hybrid(self, and_or: AndOr = AndOr.And, yes_no_ignore: YesNoIgnore = YesNoIgnore.Ignore) -> None:
        self._options['c_biocn_hyb'] = and_or.value
        self._options['q_biocn_hyb'] = yes_no_ignore.value

    def get_hybrid(self) -> (AndOr, YesNoIgnore):
        return AndOr(self._options['c_biocn_hyb']), YesNoIgnore(self._options['q_biocn_hyb'])

    def set_protein(self, and_or: AndOr = AndOr.And, yes_no_ignore: YesNoIgnore = YesNoIgnore.Ignore) -> None:
        self._options['c_biocn_pro'] = and_or.value
        self._options['q_biocn_pro'] = yes_no_ignore.value

    def get_protein(self) -> (AndOr, YesNoIgnore):
        return AndOr(self._options['c_biocn_pro']), YesNoIgnore(self._options['q_biocn_pro'])

    def set_ligand(self, and_or: AndOr = AndOr.And, yes_no_ignore: YesNoIgnore = YesNoIgnore.Ignore) -> None:
        self._options['c_biocn_lig'] = and_or.value
        self._options['q_biocn_lig'] = yes_no_ignore.value

    def get_ligand(self) -> (AndOr, YesNoIgnore):
        return AndOr(self._options['c_biocn_lig']), YesNoIgnore(self._options['q_biocn_lig'])

    def set_ligand_id(self, and_or: AndOr = AndOr.And, ligand_id: str = '') -> None:
        self._options['c_biocn_lid'] = and_or.value
        self._options['q_biocn_lid'] = ligand_id

    def get_ligand_id(self) -> (AndOr, YesNoIgnore):
        return AndOr(self._options['c_biocn_lid']), self._options['q_biocn_lid']

    def set_ligand_name(self, and_or: AndOr = AndOr.And, ligand_name: str = '') -> None:
        self._options['c_biocn_lim'] = and_or.value
        self._options['q_biocn_lim'] = ligand_name

    def get_ligand_name(self) -> (AndOr, YesNoIgnore):
        return AndOr(self._options['c_biocn_lim']), self._options['q_biocn_lim']

    def set_drug(self, and_or: AndOr = AndOr.And, yes_no_ignore: YesNoIgnore = YesNoIgnore.Ignore) -> None:
        self._options['c_biocn_drg'] = and_or.value
        self._options['q_biocn_drg'] = yes_no_ignore.value

    def get_drug(self) -> (AndOr, YesNoIgnore):
        """
        :return: tuple of drug (AndOr, YesNoIgnore)
        """
        return AndOr(self._options['c_biocn_drg']), YesNoIgnore(self._options['q_biocn_drg'])

    def set_drug_binding(self, and_or: AndOr = AndOr.And, *types: List[DrugBinding]) -> None:
        """
        Sets drug_binding property - to get it work ensure to call set_drug()!!!

        :param and_or: AndOr
        :param types: list of DrugBinding
        """
        self._options['i_biocn_dbt'] = and_or.value
        self._options['q_biocn_dbt'] = [x.value for x in types] if types else []

    def get_drug_binding(self) -> (AndOr, List[DrugBinding]):
        return AndOr(self._options['i_biocn_dbt']), [DrugBinding(x) for x in self._options['q_biocn_dbt']]

    def set_crystal_structure(self, and_or: AndOr = AndOr.And, yes_no_ignore: YesNoIgnore = YesNoIgnore.Ignore) -> None:
        self._options['c_etype_cry'] = and_or.value
        self._options['q_etype_cry'] = yes_no_ignore.value

    def get_crystal_structure(self) -> (AndOr, YesNoIgnore):
        return AndOr(self._options['c_etype_cry']), YesNoIgnore(self._options['q_etype_cry'])

    def set_structure_factors(self, and_or: AndOr = AndOr.And, yes_no_ignore: YesNoIgnore = YesNoIgnore.Ignore) -> None:
        self._options['c_etype_sfc'] = and_or.value
        self._options['q_etype_sfc'] = yes_no_ignore.value

    def get_structure_factors(self) -> (AndOr, YesNoIgnore):
        return AndOr(self._options['c_etype_sfc']), YesNoIgnore(self._options['q_etype_sfc'])

    def set_nmr(self, and_or: AndOr = AndOr.And, yes_no_ignore: YesNoIgnore = YesNoIgnore.Ignore) -> None:
        self._options['c_etype_nmr'] = and_or.value
        self._options['q_etype_nmr'] = yes_no_ignore.value

    def get_nmr(self) -> (AndOr, YesNoIgnore):
        return AndOr(self._options['c_etype_nmr']), YesNoIgnore(self._options['q_etype_nmr'])

    def set_nmr_restraints(self, and_or: AndOr = AndOr.And, yes_no_ignore: YesNoIgnore = YesNoIgnore.Ignore) -> None:
        self._options['c_etype_nra'] = and_or.value
        self._options['q_etype_nra'] = yes_no_ignore.value

    def get_nmr_restraints(self) -> (AndOr, YesNoIgnore):
        return AndOr(self._options['c_etype_nra']), YesNoIgnore(self._options['q_etype_nra'])

    def set_space_group(self, and_or: AndOr = AndOr.And, space_group: SpaceGroup = SpaceGroup.Nothing) -> None:
        self._options['c_detal_grp'] = and_or.value
        self._options['q_detal_grp'] = space_group.value

    def get_space_group(self) -> (AndOr, SpaceGroup):
        return AndOr(self._options['c_detal_grp']), SpaceGroup(self._options['q_detal_grp'])

    def set_cell_alpha(self, and_or: AndOr = AndOr.And,
                       greater_lower_equal: GreaterLowerEqual = GreaterLowerEqual.Equal,
                       value: Optional[float] = None) -> None:
        self._options['c_detal_ana'] = and_or.value
        self._options['q_detal_oaa'] = greater_lower_equal.value
        self._options['q_detal_vaa'] = value if value else ''

    def get_cell_alpha(self) -> (AndOr, GreaterLowerEqual, Optional[float]):
        return AndOr(self._options['c_detal_ana']), GreaterLowerEqual(self._options['q_detal_oaa']), \
               float(self._options['q_detal_vaa']) if self._options['q_detal_vaa'] else None

    def set_cell_beta(self, and_or: AndOr = AndOr.And,
                      greater_lower_equal: GreaterLowerEqual = GreaterLowerEqual.Equal,
                      value: Optional[float] = None) -> None:
        self._options['c_detal_anb'] = and_or.value
        self._options['q_detal_oab'] = greater_lower_equal.value
        self._options['q_detal_vab'] = value if value else ''

    def get_cell_beta(self) -> (AndOr, GreaterLowerEqual, Optional[float]):
        return AndOr(self._options['c_detal_anb']), GreaterLowerEqual(self._options['q_detal_oab']), \
               float(self._options['q_detal_vab']) if self._options['q_detal_vab'] else None

    def set_cell_gamma(self, and_or: AndOr = AndOr.And,
                       greater_lower_equal: GreaterLowerEqual = GreaterLowerEqual.Equal,
                       value: Optional[float] = None) -> None:
        self._options['c_detal_ang'] = and_or.value
        self._options['q_detal_oag'] = greater_lower_equal.value
        self._options['q_detal_vag'] = value if value else ''

    def get_cell_gamma(self) -> (AndOr, GreaterLowerEqual, Optional[float]):
        return AndOr(self._options['c_detal_ang']), GreaterLowerEqual(self._options['q_detal_oag']), \
               float(self._options['q_detal_vag']) if self._options['q_detal_vag'] else None

    def set_cell_a(self, and_or: AndOr = AndOr.And,
                   greater_lower_equal: GreaterLowerEqual = GreaterLowerEqual.Equal,
                   value: Optional[float] = None) -> None:
        self._options['c_detal_lna'] = and_or.value
        self._options['q_detal_ola'] = greater_lower_equal.value
        self._options['q_detal_vla'] = value if value else ''

    def get_cell_a(self) -> (AndOr, GreaterLowerEqual, Optional[float]):
        return AndOr(self._options['c_detal_lna']), GreaterLowerEqual(self._options['q_detal_ola']), \
               float(self._options['q_detal_vla']) if self._options['q_detal_vla'] else None

    def set_cell_b(self, and_or: AndOr = AndOr.And,
                   greater_lower_equal: GreaterLowerEqual = GreaterLowerEqual.Equal,
                   value: Optional[float] = None) -> None:
        self._options['c_detal_lnb'] = and_or.value
        self._options['q_detal_olb'] = greater_lower_equal.value
        self._options['q_detal_vlb'] = value if value else ''

    def get_cell_b(self) -> (AndOr, GreaterLowerEqual, Optional[float]):
        return AndOr(self._options['c_detal_lnb']), GreaterLowerEqual(self._options['q_detal_olb']), \
               float(self._options['q_detal_vlb']) if self._options['q_detal_vlb'] else None

    def set_cell_c(self, and_or: AndOr = AndOr.And,
                   greater_lower_equal: GreaterLowerEqual = GreaterLowerEqual.Equal,
                   value: Optional[float] = None) -> None:
        self._options['c_detal_lnc'] = and_or.value
        self._options['q_detal_olc'] = greater_lower_equal.value
        self._options['q_detal_vlc'] = value if value else ''

    def get_cell_c(self) -> (AndOr, GreaterLowerEqual, Optional[float]):
        return AndOr(self._options['c_detal_lnc']), GreaterLowerEqual(self._options['q_detal_olc']), \
               float(self._options['q_detal_vlc']) if self._options['q_detal_vlc'] else None

    def set_cell_resolution(self, and_or: AndOr = AndOr.And, better_than: Optional[float] = None) -> None:
        self._options['c_detal_res'] = and_or.value
        self._options['q_detal_res'] = better_than if better_than else ''

    def get_cell_resolution(self) -> (AndOr, Optional[float]):
        return AndOr(self._options['c_detal_res']), \
               float(self._options['q_detal_res']) if self._options['q_detal_res'] else None

    def set_cell_r_factor(self, and_or: AndOr = AndOr.And, r_factor: RFactor = RFactor.Nothing) -> None:
        self._options['c_detal_rfc'] = and_or.value
        self._options['q_detal_rfc'] = r_factor.value

    def get_cell_r_factor(self) -> (AndOr, RFactor):
        return AndOr(self._options['c_detal_rfc']), RFactor(self._options['q_detal_rfc'])

    def set_ndb_id(self, ndb_id: str = '') -> None:
        self._options['q_ndbid'] = ndb_id

    def get_ndb_id(self) -> str:
        return self._options['q_ndbid']

    def set_pdb_id(self, pdb_id: str = '') -> None:
        self._options['q_pdbid'] = pdb_id

    def get_pdb_id(self) -> str:
        return self._options['q_pdbid']

    def set_author(self, and_or: AndOr = AndOr.And, author: str = '') -> None:
        self._options['c_authr'] = and_or.value
        self._options['q_authr'] = author

    def get_author(self) -> (AndOr, str):
        return AndOr(self._options['c_authr']), self._options['q_authr']

    def set_publication_year(self, and_or: AndOr = AndOr.And, year: str = '') -> None:
        self._options['c_citat_ann'] = and_or.value
        self._options['q_citat_ann'] = year

    def get_publication_year(self) -> (AndOr, str):
        return AndOr(self._options['c_citat_ann']), self._options['q_citat_ann']

    def set_released(self, and_or: AndOr = AndOr.And, since_date: Optional[date] = None) -> None:
        self._options['c_citat_rel'] = and_or.value
        self._options['q_citat_rel'] = since_date.isoformat() if since_date else ''

    def get_released(self) -> (AndOr, Optional[date]):
        return AndOr(self._options['c_citat_rel']), datetime.strptime(date, '%Y-$m-$d').date() \
            if self._options['q_citat_rel'] else None

    def set_base_pair(self, and_or: AndOr = AndOr.And, base_pair: BasePair = BasePair.Nothing) -> None:
        self._options['c_bp_int'] = and_or.value
        self._options['q_bp_int'] = base_pair.value

    def get_base_pair(self) -> (AndOr, BasePair):
        return AndOr(self._options['c_bp_int']), BasePair(self._options['q_bp_int'])

    def set_base_phosphate(self, and_or: AndOr = AndOr.And,
                           base_phosphate: BasePhosphate = BasePhosphate.Nothing) -> None:
        self._options['c_bph_int'] = and_or.value
        self._options['q_bph_int'] = base_phosphate.value

    def get_base_phosphate(self) -> (AndOr, BasePhosphate):
        return AndOr(self._options['c_bph_int']), BasePhosphate(self._options['q_bph_int'])

    def set_base_stack(self, and_or: AndOr = AndOr.And, base_stack: BaseStack = BaseStack.Nothing) -> None:
        self._options['c_bs_int'] = and_or.value
        self._options['q_bs_int'] = base_stack.value

    def get_base_stack(self) -> (AndOr, BaseStack):
        return AndOr(self._options['c_bs_int']), BaseStack(self._options['q_bs_int'])

    def set_base_pair_relative(self, and_or: AndOr = AndOr.And, base_pair: BasePair = BasePair.Nothing,
                               greater_lower: GreaterLower= GreaterLower.GreaterEqual, freq: float= 0.1) -> None:
        self._options['c_bp_f_count'] = and_or.value
        self._options['q_bp_f_int'] = base_pair.value
        self._options['q_bp_f_op'] = greater_lower.value
        self._options['q_bp_f_count'] = freq

    def get_base_pair_relative(self) -> (AndOr, BasePair, GreaterLower, float):
        return AndOr(self._options['c_bp_f_count']), BasePair(self._options['q_bp_f_int']), \
               GreaterLower(self._options['q_bp_f_op']), self._options['q_bp_f_count']

    def set_base_phosphate_relative(self, and_or: AndOr = AndOr.And,
                                    base_phosphate: BasePhosphate = BasePhosphate.Nothing,
                                    greater_lower: GreaterLower = GreaterLower.GreaterEqual, freq: float = 0.1) -> None:
        self._options['c_bph_f_count'] = and_or.value
        self._options['q_bph_f_int'] = base_phosphate.value
        self._options['q_bph_f_op'] = greater_lower.value
        self._options['q_bph_f_count'] = freq

    def get_base_phosphate_relative(self) -> (AndOr, BasePhosphate, GreaterLower, float):
        return AndOr(self._options['c_bph_f_count']), BasePhosphate(self._options['q_bph_f_int']), \
               GreaterLower(self._options['q_bph_f_op']), self._options['q_bph_f_count']

    def set_base_stack_relative(self, and_or: AndOr = AndOr.And, base_stack: BaseStack = BaseStack.Nothing,
                                greater_lower: GreaterLower = GreaterLower.GreaterEqual, freq: float = 0.1) -> None:
        self._options['c_bs_f_count'] = and_or.value
        self._options['q_bs_f_int'] = base_stack.value
        self._options['q_bs_f_op'] = greater_lower.value
        self._options['q_bs_f_count'] = freq

    def get_base_stack_relative(self) -> (AndOr, BaseStack, GreaterLower, float):
        return AndOr(self._options['c_bs_f_count']), BaseStack(self._options['q_bs_f_int']), \
               GreaterLower(self._options['q_bs_f_op']), self._options['q_bs_f_count']

    def set_internal_loop_motif(self, and_or: AndOr = AndOr.And, *motifs: List[HairpinLoopMotif]) -> None:
        self._options['c_int_motif'] = and_or.value
        self._options['q_int_motif'] = [x.value for x in motifs] if motifs else []

    def get_internal_loop_motif(self) -> (AndOr, List[InternalLoopMotif]):
        return AndOr(self._options['c_int_motif']), [InternalLoopMotif(x) for x in self._options['q_int_motif']]

    def set_hairpin_loop_motif(self, and_or: AndOr = AndOr.And, *motifs: List[HairpinLoopMotif]) -> None:
        self._options['c_hairpin_motif'] = and_or.value
        self._options['q_hairpin_motif'] = [x.value for x in motifs] if motifs else []

    def get_hairpin_loop_motif(self) -> (AndOr, List[HairpinLoopMotif]):
        return AndOr(self._options['c_hairpin_motif']), [HairpinLoopMotif(x) for x in self._options['q_hairpin_motif']]

    def set_non_redundant_list(self, and_or: AndOr = AndOr.And,
                               resolution: ResolutionCutoff= ResolutionCutoff.Nothing) -> None:
        self._options['c_nr_list'] = and_or.value
        self._options['q_nr_list'] = resolution.value

    def get_non_redundant_list(self) -> (AndOr, ResolutionCutoff):
        return AndOr(self._options['c_nr_list']), ResolutionCutoff(self._options['q_nr_list'])

    def set_na_pattern(self, and_or: AndOr = AndOr.And, pattern: str = '') -> None:
        self._options['c_seqnc'] = and_or.value
        self._options['q_seqnc'] = pattern

    def get_na_pattern(self) -> (AndOr, str):
        return AndOr(self._options['c_seqnc']), self._options['q_seqnc']

    def set_oligo_seq_between(self, and_or: AndOr = AndOr.And, from_len: Optional[int]= None,
                              to_len: Optional[int]= None) -> None:
        self._options['c_seqln'] = and_or.value
        self._options['q_lnmin'] = from_len if from_len else ''
        self._options['q_lnmax'] = to_len if to_len else ''

    def get_oligo_seq_between(self) -> (AndOr, Optional[int], Optional[int]):
        return AndOr(self._options['c_seqln']), \
               int(self._options['q_lnmin']) if self._options['q_lnmin'] else None, \
               int(self._options['q_lnmax']) if self._options['q_lnmax'] else None

    def set_base(self, and_or: AndOr = AndOr.And, yes_no_ignore: YesNoIgnore = YesNoIgnore.Ignore) -> None:
        self._options['c_namod_bas'] = and_or.value
        self._options['q_namod_bas'] = yes_no_ignore.value

    def get_base(self) -> (AndOr, YesNoIgnore):
        return AndOr(self._options['c_namod_bas']), YesNoIgnore(self._options['q_namod_bas'])

    def set_sugar(self, and_or: AndOr = AndOr.And, yes_no_ignore: YesNoIgnore = YesNoIgnore.Ignore) -> None:
        self._options['c_namod_sgr'] = and_or.value
        self._options['q_namod_sgr'] = yes_no_ignore.value

    def get_sugar(self) -> (AndOr, YesNoIgnore):
        return AndOr(self._options['c_namod_sgr']), YesNoIgnore(self._options['q_namod_sgr'])

    def set_phosphate(self, and_or: AndOr = AndOr.And, yes_no_ignore: YesNoIgnore = YesNoIgnore.Ignore) -> None:
        self._options['c_namod_phs'] = and_or.value
        self._options['q_namod_phs'] = yes_no_ignore.value

    def get_phosphate(self) -> (AndOr, YesNoIgnore):
        return AndOr(self._options['c_namod_phs']), YesNoIgnore(self._options['q_namod_phs'])

    def set_enzyme_binding(self, and_or: AndOr= AndOr.And, dna_rna_either: DnaRnaEither= DnaRnaEither.Either,
                           func_clause: AndOr= AndOr.And, *functions: List[EnzymeFunction]) -> None:
        self._options['c_prbmd_enz'] = and_or.value
        self._options['q_prbmd_enz'] = dna_rna_either.value
        self._options['i_prbmd_efn'] = func_clause.value
        self._options['q_prbmd_efn'] = [x.value for x in functions] if functions else []

    def get_enzyme_binding(self) -> (AndOr, DnaRnaEither, AndOr, List[EnzymeFunction]):
        return AndOr(self._options['c_prbmd_enz']), DnaRnaEither(self._options['q_prbmd_enz']), \
               AndOr(self._options['i_prbmd_efn']), [EnzymeFunction(x) for x in self._options['q_prbmd_efn']]

    def set_regulatory_binding(self, and_or: AndOr = AndOr.And, dna_rna_either: DnaRnaEither = DnaRnaEither.Either,
                               func_clause: AndOr = AndOr.And, *functions: List[RegulatoryFunction]) -> None:
        self._options['c_prbmd_reg'] = and_or.value
        self._options['q_prbmd_reg'] = dna_rna_either.value
        self._options['i_prbmd_rfn'] = func_clause.value
        self._options['q_prbmd_rfn'] = [x.value for x in functions] if functions else []

    def get_regulatory_binding(self) -> (AndOr, DnaRnaEither, AndOr, List[RegulatoryFunction]):
        return AndOr(self._options['c_prbmd_reg']), DnaRnaEither(self._options['q_prbmd_reg']), \
           AndOr(self._options['i_prbmd_rfn']), [RegulatoryFunction(x) for x in self._options['q_prbmd_rfn']]

    def set_structural_binding(self, and_or: AndOr = AndOr.And, dna_rna_either: DnaRnaEither = DnaRnaEither.Either,
                               func_clause: AndOr = AndOr.And, *functions: List[StructuralFunction]) -> None:
        self._options['c_prbmd_str'] = and_or.value
        self._options['q_prbmd_str'] = dna_rna_either.value
        self._options['i_prbmd_sfn'] = func_clause.value
        self._options['q_prbmd_sfn'] = [x.value for x in functions] if functions else []

    def get_structural_binding(self) -> (AndOr, DnaRnaEither, AndOr, List[StructuralFunction]):
        return AndOr(self._options['c_prbmd_str']), DnaRnaEither(self._options['q_prbmd_str']), \
           AndOr(self._options['i_prbmd_sfn']), [StructuralFunction(x) for x in self._options['q_prbmd_sfn']]

    def set_other_binding(self, and_or: AndOr = AndOr.And, dna_rna_either: DnaRnaEither = DnaRnaEither.Either,
                          func_clause: AndOr = AndOr.And, *functions: List[OtherFunction]) -> None:
        self._options['c_prbmd_oth'] = and_or.value
        self._options['q_prbmd_oth'] = dna_rna_either.value
        self._options['i_prbmd_ofn'] = func_clause.value
        self._options['q_prbmd_ofn'] = [x.value for x in functions] if functions else []

    def get_other_binding(self) -> (AndOr, DnaRnaEither, AndOr, List[OtherFunction]):
        return AndOr(self._options['c_prbmd_oth']), DnaRnaEither(self._options['q_prbmd_oth']), \
               AndOr(self._options['i_prbmd_ofn']), [OtherFunction(x) for x in self._options['q_prbmd_ofn']]

    def set_na_features(self, and_or: AndOr = AndOr.And, func_clause: AndOr = AndOr.And,
                        *features: List[NaFeature]) -> None:
        self._options['c_nasct_ftr'] = and_or.value
        self._options['i_nasct_ftr'] = func_clause.value
        self._options['q_nasct_ftr'] = [x.value for x in features] if features else []

    def get_na_features(self) -> (AndOr, AndOr, List[NaFeature]):
        return AndOr(self._options['c_nasct_ftr']), AndOr(self._options['i_nasct_ftr']),\
               [NaFeature(x) for x in self._options['q_nasct_ftr']]

    def set_strand_desc(self, and_or: AndOr = AndOr.And, *descriptions: List[StrandDescription]) -> None:
        self._options['c_nasct_des'] = and_or.value
        self._options['q_nasct_des'] = [x.value for x in descriptions] if descriptions else []

    def get_strand_desc(self) -> (AndOr, List[StrandDescription]):
        return AndOr(self._options['c_nasct_des']), [StrandDescription(x) for x in self._options['q_nasct_des']]

    def set_conformation(self, and_or: AndOr = AndOr.And,
                         conformation: ConformationType= ConformationType.Nothing) -> None:
        self._options['c_nasct_typ'] = and_or.value
        self._options['q_nasct_typ'] = conformation.value

    def get_conformation(self) -> (AndOr, ConformationType):
        return AndOr(self._options['c_nasct_typ']), ConformationType(self._options['q_nasct_typ'])

    def get(self) -> dict:
        """Method to get dictionary of advanced search options.

        :return: dictionary with options
        :rtype: dict
        """
        return self._options

    def __str__(self) -> str:
        return str(self._options)
