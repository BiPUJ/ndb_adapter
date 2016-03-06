from NDB.ndb import NDB
from NDB.enums import ReportType


def main():
    report = NDB.advanced_search(rep_type=ReportType.Citation)
    print(report)

if __name__ == '__main__':
    main()

