import csv
from operator import itemgetter
import datetime as dt


class MobilePhoneMasts:
    def __init__(self, filename):
        self._read_data(filename)

    def _str_to_date(self, date_str):
        for format in ["%d %b %Y", "%d-%b-%y"]:
            try:
                return dt.datetime.strptime(date_str, format).date()
            except ValueError:
                continue
        raise ValueError("Unexpected datetime format for date " + f"{date_str}")

    def _correct_datatypes(self, row):
        row[7] = self._str_to_date(row[7])
        row[8] = self._str_to_date(row[8])
        row[9] = int(row[9])
        row[10] = float(row[10])
        return row

    def _read_data(self, filename):
        with open(filename) as csv_file:
            reader = csv.reader(csv_file)
            self.headers = next(reader)
            self.data = [self._correct_datatypes(row) for row in reader]

    def sorted_by_current_rent(self):
        sorted_list = sorted(self.data, key=itemgetter(-1))
        sorted_list.insert(0, self.headers)
        return sorted_list

    def lease_years_of_25(self):
        valid_tenants = [row for row in self.data if row[-2] == 25]
        valid_tenants.insert(0, self.headers)
        return valid_tenants

    def total_rent(self, tenants):
        total_rent = 0.0
        for row in tenants:
            if isinstance(row[-1], str):
                continue
            total_rent += row[-1]
        return total_rent


