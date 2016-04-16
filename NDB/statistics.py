from typing import List, Dict
from NDB.search_report import StatisticReport


class Statistics(object):
    def __init__(self):
        self.min = {}       # type: Dict[str, float]
        self.max = {}       # type: Dict[str, float]
        self.mean = {}      # type: Dict[str, float]
        self.std_dev = {}   # type: Dict[str, float]

    def set_report(self, report: List[StatisticReport]):
        for row in report:
            row_dict = row.get_stats()
            try:
                if row_dict['Stat'] == 'Min':
                    for k, v in row_dict.items():
                        self.min[k] = float(v)
                elif row_dict['Stat'] == 'Max':
                    for k, v in row_dict.items():
                        self.max[k] = float(v)
                elif row_dict['Stat'] == 'Mean':
                    for k, v in row_dict.items():
                        self.mean[k] = float(v)
                elif row_dict['Stat'] == 'Standard Deviation':
                    for k, v in row_dict.items():
                        self.std_dev[k] = float(v)
            except ValueError:
                pass

    def __str__(self):
        return "Min: " + str(self.min) + "\n" \
            "Max: " + str(self.max) + "\n" \
            "Mean: " + str(self.mean) + "\n" \
            "Standard Deviation: " + str(self.std_dev)
