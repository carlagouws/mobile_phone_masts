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
        sorted_data = sorted(self.data, key=itemgetter(-1))


def main():
    data_list = MobilePhoneMasts("dataset.csv")
    data_list.sorted_by_current_rent()


main()
