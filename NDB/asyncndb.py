import aiohttp
import NDB.report_parser as parser
from NDB.enums import ReportType
from NDB.ndb_base import NDBBase


class NDB(NDBBase):

    # search_report:
    # q_nasct_des:
    # q_prbmd_sfn:
    # i_prbmd_ofn:AND
    # c_detal_rfc:AND
    # q_detal_res:
    # q_biocn_lid:
    # q_biocn_lig:Ignore
    # c_biocn_drg:AND
    # c_citat_ann:AND
    # c_detal_anb:AND
    # c_detal_ana:AND
    # c_bph_int:AND
    # c_detal_ang:AND
    # c_detal_lnc:AND
    # c_bph_count:
    # q_bs_f_count:0.1
    # q_seqnc:
    # i_nasct_des:OR
    # q_biocn_hyb:Ignore
    # q_detal_grp:
    # c_prbmd_oth:AND
    # c_bp_count:
    # c_etype_sfc:AND
    # c_etype_nmr:AND
    # q_biocn_rna:Ignore
    # c_biocn_pro:AND
    # q_bph_f_op:gtEq
    # q_bp_count:
    # c_nasct_ftr:and
    # q_detal_vla:
    # q_detal_vlb:
    # q_detal_vlc:
    # c_prbmd_reg:AND
    # c_namod_bas:and
    # q_biocn_drg:Ignore
    # q_namod_sgr:Ignore
    # q_bph_f_int:
    # c_bs_f_count:AND
    # c_bs_count:
    # q_etype_nra:Ignore
    # q_bph_int:
    # c_bp_int:AND
    # q_detal_olc:eq
    # q_detal_vag:
    # c_bs_int:AND
    # q_prbmd_efn:
    # q_detal_vab:
    # q_detal_vaa:
    # q_detal_oab:eq
    # i_prbmd_sfn:AND
    # q_detal_oaa:eq
    # q_bp_f_op:gtEq
    # q_detal_oag:eq
    # q_hairpin_motif:
    # q_bp_f_int:
    # q_namod_phs:Ignore
    # c_int_motif:and
    # q_authr:
    # c_nr_list:AND
    # c_detal_res:AND
    # q_citat_ann:
    # c_authr:and
    # q_etype_cry:Ignore
    # c_bp_f_count:AND
    # q_etype_nmr:Ignore
    # q_int_motif:
    # c_etype_cry:AND
    # q_bph_count:
    # q_bp_int:
    # q_nr_list:
    # c_biocn_dna:AND
    # q_prbmd_rfn:
    # q_prbmd_enz:EITHER
    # i_hairpin_motif:OR
    # q_bs_int:
    # q_detal_ola:eq
    # c_biocn_lnm:AND
    # q_detal_olb:eq
    # q_nasct_typ:
    # q_bs_op:
    # c_biocn_hyb:AND
    # q_biocn_pro:Ignore
    # c_etype_nra:AND
    # q_bs_f_int:from NDB import *
    # q_etype_sfc:Ignore
    # c_biocn_rna:AND
    # q_prbmd_reg:EITHER
    # i_nasct_ftr:AND
    # c_detal_grp:AND
    # q_citat_rel:
    # c_biocn_lig:AND
    # c_prbmd_enz:AND
    # c_nasct_des:and
    # c_hairpin_motif:and
    # q_lnmin:
    # q_prbmd_str:EITHER
    # q_biocn_dbt:
    # i_prbmd_efn:AND
    # q_nasct_ftr:
    # c_seqln:AND
    # c_citat_rel:AND
    # q_prbmd_ofn:
    # q_bs_f_op:gtEq
    # c_namod_phs:and
    # c_prbmd_str:AND
    # q_bs_count:
    # c_biocn_lid:AND
    # q_biocn_dna:Ignore
    # c_nasct_typ:and
    # q_namod_bas:Ignore
    # c_detal_lnb:AND
    # c_namod_sgr:and
    # q_prbmd_oth:EITHER
    # c_detal_lna:AND
    # i_prbmd_rfn:AND
    # q_bp_op:
    # i_biocn_dbt:AND
    # c_seqnc:AND
    # q_ndbid:
    # q_bp_f_count:0.1
    # q_biocn_lnm:
    # q_bph_f_count:0.1
    # q_lnmax:
    # q_pdbid:
    # q_bph_op:
    # c_bph_f_count:
    # i_int_motif:OR
    # q_detal_rfc:
    # repType:
    @staticmethod
    async def advanced_search(rep_type=ReportType.NDBStatus):
        params = {
            'search_report': rep_type.value,
            'chkAllStructure': 'on',
            'repType': 'csv'
        }

        with aiohttp.ClientSession() as session:
            async with session.post(NDBBase.advancedUrl, data=params) as resp:
                text = await resp.text()
                report = parser.parse_advanced_search_report(text)
                return report

    @staticmethod
    async def dna_search():
        params = {
            'strGalType': 'dna',
            'galType': 'table',
            'limit': '10',
            'start': '0',
            'polType': 'all',
            'protFunc': 'all',
            'stFeature': 'all',
            'expMeth': 'all',
            'filterTxt': ''
        }

        with aiohttp.ClientSession() as session:
            async with session.post(NDBBase.dnaUrl, data=params) as resp:
                text = await resp.text()
                report = parser.parse_search_report(text)
                return report

    @staticmethod
    async def rna_search():
        params = {
            'strGalType': 'rna',
            'galType': 'table',
            'limit': '10',
            'start': '0',
            'polType': 'all',
            'rnaFunc': 'all',
            'protFunc': 'all',
            'seqType': 'all',
            'expMeth': 'all',
            'filterTxt': ''
        }

        with aiohttp.ClientSession() as session:
            async with session.post(NDBBase.rnaUrl, data=params) as resp:
                text = await resp.text()
                report = parser.parse_search_report(text)
                return report
