

class NDBBase(object):
    """Base class for NDB

    :cvar siteUrl: ndb site url
    :cvar _advancedUrl: private advanced search url
    :cvar _summaryUrl: private summary url
    :cvar _dnaUrl: private dna search url
    :cvar _rnaUrl: private rna search url
    """
    siteUrl = 'http://ndbserver.rutgers.edu'
    _advancedUrl = siteUrl + '/service/ndb/report/advSearchReport'
    _summaryUrl = siteUrl + '/service/ndb/atlas/summary'
    _dnaUrl = siteUrl + '/service/ndb/atlas/gallery/dna'
    _rnaUrl = siteUrl + '/service/ndb/atlas/gallery/rna'
