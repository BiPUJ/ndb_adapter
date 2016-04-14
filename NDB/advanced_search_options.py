from NDB.enums import ReportType, YesNoIgnore, AndOr, DnaRnaEither, GreaterLowerEqual, DrugBinding


class AdvancedSearchOptions(object):
    def __init__(self, report_type: ReportType= ReportType.NDBStatus):
        self._options = {
            'search_report': report_type.value,
            'q_nasct_des': '',
            'q_prbmd_sfn': '',
            'i_prbmd_ofn': AndOr.And.value,
            'c_detal_rfc': AndOr.And.value,
            'q_detal_res': '',
            'q_biocn_lid': '',
            'q_biocn_lig': '',
            'c_biocn_drg': '',
            'c_citat_ann': '',
            'c_detal_anb': '',
            'c_detal_ana': '',
            'c_bph_int': AndOr.And.value,
            'c_detal_ang': AndOr.And.value,
            'c_detal_lnc': AndOr.And.value,
            'c_bph_count': '',
            'q_bs_f_count': '0.1',
            'q_seqnc': '',
            'i_nasct_des': AndOr.Or.value,
            'q_biocn_hyb': YesNoIgnore.Ignore.value,
            'q_detal_grp': '',
            'c_prbmd_oth': AndOr.And.value,
            'c_bp_count': '',
            'c_etype_sfc': AndOr.And.value,
            'c_etype_nmr': AndOr.And.value,
            'q_biocn_rna': YesNoIgnore.Ignore.value,
            'c_biocn_pro': AndOr.And.value,
            'q_bph_f_op': GreaterLowerEqual.GreaterEqual.value,
            'q_bp_count': '',
            'c_nasct_ftr': AndOr.And.value,
            'q_detal_vla': '',
            'q_detal_vlb': '',
            'q_detal_vlc': '',
            'c_prbmd_reg': AndOr.And.value,
            'c_namod_bas': AndOr.And.value,
            'q_biocn_drg': YesNoIgnore.Ignore.value,
            'q_namod_sgr': YesNoIgnore.Ignore.value,
            'q_bph_f_int': '',
            'c_bs_f_count': AndOr.And.value,
            'c_bs_count': '',
            'q_etype_nra': YesNoIgnore.Ignore.value,
            'q_bph_int': '',
            'c_bp_int': AndOr.And.value,
            'q_detal_olc': GreaterLowerEqual.Equal.value,
            'q_detal_vag': '',
            'c_bs_int': AndOr.And.value,
            'q_prbmd_efn': '',
            'q_detal_vab': '',
            'q_detal_vaa': '',
            'q_detal_oab': GreaterLowerEqual.Equal.value,
            'i_prbmd_sfn': AndOr.And.value,
            'q_detal_oaa': GreaterLowerEqual.Equal.value,
            'q_bp_f_op': GreaterLowerEqual.GreaterEqual.value,
            'q_detal_oag': GreaterLowerEqual.Equal.value,
            'q_hairpin_motif': '',
            'q_bp_f_int': '',
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
            'q_int_motif': '',
            'c_etype_cry': AndOr.And.value,
            'q_bph_count': '',
            'q_bp_int': '',
            'q_nr_list': '',
            'c_biocn_dna': AndOr.And.value,
            'q_prbmd_rfn': '',
            'q_prbmd_enz': DnaRnaEither.Either.value,
            'i_hairpin_motif': AndOr.Or.value,
            'q_bs_int': '',
            'q_detal_ola': GreaterLowerEqual.Equal.value,
            'c_biocn_lnm': AndOr.And.value,
            'q_detal_olb': GreaterLowerEqual.Equal.value,
            'q_nasct_typ': '',
            'q_bs_op': '',
            'c_biocn_hyb': AndOr.And.value,
            'q_biocn_pro': YesNoIgnore.Ignore.value,
            'c_etype_nra': AndOr.And.value,
            'q_bs_f_int': '',
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
            'q_nasct_ftr': '',
            'c_seqln': AndOr.And.value,
            'c_citat_rel': AndOr.And.value,
            'q_prbmd_ofn': '',
            'q_bs_f_op': GreaterLowerEqual.GreaterEqual.value,
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
            'q_bp_f_count': '0.1',
            'q_biocn_lnm': '',
            'q_bph_f_count': '0.1',
            'q_lnmax': '',
            'q_pdbid': '',
            'q_bph_op': '',
            'c_bph_f_count': '',
            'i_int_motif': AndOr.Or.value,
            'q_detal_rfc': '',
            'chkAllStructure': 'on',
            'repType': 'csv'
        }

    def set_dna(self, and_or: AndOr= AndOr.And, yes_no_ignore: YesNoIgnore= YesNoIgnore.Ignore) -> None:
        self._options['c_biocn_dna'] = and_or.value
        self._options['q_biocn_dna'] = yes_no_ignore.value

    def get_dna(self) -> tuple:
        return AndOr(self._options['c_biocn_dna']), YesNoIgnore(self._options['q_biocn_dna'])

    def set_rna(self, and_or: AndOr = AndOr.And, yes_no_ignore: YesNoIgnore = YesNoIgnore.Ignore) -> None:
        self._options['c_biocn_rna'] = and_or.value
        self._options['q_biocn_rna'] = yes_no_ignore.value

    def get_rna(self) -> tuple:
        return AndOr(self._options['c_biocn_rna']), YesNoIgnore(self._options['q_biocn_rna'])

    def set_hybrid(self, and_or: AndOr = AndOr.And, yes_no_ignore: YesNoIgnore = YesNoIgnore.Ignore) -> None:
        self._options['c_biocn_hyb'] = and_or.value
        self._options['q_biocn_hyb'] = yes_no_ignore.value

    def get_hybrid(self) -> tuple:
        return AndOr(self._options['c_biocn_hyb']), YesNoIgnore(self._options['q_biocn_hyb'])

    def set_protein(self, and_or: AndOr = AndOr.And, yes_no_ignore: YesNoIgnore = YesNoIgnore.Ignore) -> None:
        self._options['c_biocn_pro'] = and_or.value
        self._options['q_biocn_pro'] = yes_no_ignore.value

    def get_protein(self) -> tuple:
        return AndOr(self._options['c_biocn_pro']), YesNoIgnore(self._options['q_biocn_pro'])

    def set_ligand(self, and_or: AndOr = AndOr.And, yes_no_ignore: YesNoIgnore = YesNoIgnore.Ignore) -> None:
        self._options['c_biocn_lig'] = and_or.value
        self._options['q_biocn_lig'] = yes_no_ignore.value

    def get_ligand(self) -> tuple:
        return AndOr(self._options['c_biocn_lig']), YesNoIgnore(self._options['q_biocn_lig'])

    def set_ligand_id(self, and_or: AndOr = AndOr.And, ligand_id: str= '') -> None:
        self._options['c_biocn_lid'] = and_or.value
        self._options['q_biocn_lid'] = ligand_id

    def get_ligand_id(self) -> tuple:
        return AndOr(self._options['c_biocn_lid']), self._options['q_biocn_lid']

    def set_ligand_name(self, and_or: AndOr = AndOr.And, ligand_name: str = '') -> None:
        self._options['c_biocn_lim'] = and_or.value
        self._options['q_biocn_lim'] = ligand_name

    def get_ligand_name(self) -> tuple:
        return AndOr(self._options['c_biocn_lim']), self._options['q_biocn_lim']

    def set_drug(self, and_or: AndOr = AndOr.And, yes_no_ignore: YesNoIgnore = YesNoIgnore.Ignore) -> None:
        self._options['c_biocn_drg'] = and_or.value
        self._options['q_biocn_drg'] = yes_no_ignore.value

    def get_drug(self) -> tuple:
        """
        :return: tuple of drug (AndOr, YesNoIgnore)
        """
        return AndOr(self._options['c_biocn_drg']), YesNoIgnore(self._options['q_biocn_drg'])

    def set_drug_binding(self, and_or: AndOr = AndOr.And, *drug_binding_enum: DrugBinding) -> None:
        """
        Sets drug_binding property - to get it work ensure to call set_drug()!!!

        :param and_or: AndOr
        :param drug_binding_enum: list of DrugBinding
        :rtype: None
        """
        self._options['i_biocn_dbt'] = and_or.value
        self._options['q_biocn_dbt'] = [x.value for x in drug_binding_enum] if drug_binding_enum else []

    def get(self) -> dict:
        """
        :return: dictionary with options
        """
        return self._options

    def __str__(self) -> str:
        return str(self._options)
