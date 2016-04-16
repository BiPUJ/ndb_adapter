from NDB.ndb import NDB
from NDB.enums import ReportType


def main():
    #report = NDB.advanced_search()
    #report = NDB.rna_search()
    report = NDB.summary('5F8K')
    print(str(report))

if __name__ == '__main__':
    main()

