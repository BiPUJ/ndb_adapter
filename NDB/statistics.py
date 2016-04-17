from typing import List
from NDB.search_report import StatisticReport


class Statistics(object):
    """Class for search statistics"""
    def __init__(self):
        """Default constructor"""
        self.min = {}
        """Dictionary of min values"""
        self.max = {}
        """Dictionary of max values"""
        self.mean = {}
        """Dictionary of mean values"""
        self.std_dev = {}
        """Dictionary of standard division values"""

    def set_report(self, report: List[StatisticReport]) -> None:
        """Sets statistic from report

        :param report: list of statistic report
        :type report: List[StatisticReport]
        :return: None
        """
        for row in report:
            row_dict = row.stats
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
