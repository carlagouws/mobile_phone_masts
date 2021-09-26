import csv
import difflib
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

    def _get_unique_tenant_names(self):
        tenant_names = [row[6] for row in self.data]
        return sorted(set(tenant_names))

    def _get_unique_list_of_lists(self, list_of_lists):
        new_list_of_lists = []
        for item in list_of_lists:
            if item in new_list_of_lists:
                continue
            else:
                new_list_of_lists.append(item)
        return new_list_of_lists

    def _get_close_tenant_name_matches(self):
        list_of_tenants = self._get_unique_tenant_names()
        close_matches = []
        for tenant in list_of_tenants:
            close_matches.append(sorted(difflib.get_close_matches(tenant, list_of_tenants)))
        return self._get_unique_list_of_lists(close_matches)

    def count_number_masts_per_tenant(self):
        dict_of_masts = {}
        for tenant in self._get_close_tenant_name_matches():
            counter = 0
            for row in self.data:
                if row[6] in tenant:
                    counter += 1
            dict_of_masts[tenant[0]] = counter
        return dict_of_masts

    def _get_date_range(self, start, end):
        date_range = []
        while start <= end:
            date_range.append(start)
            start += dt.timedelta(days=1)
        return date_range

    def _format_row_dates(self, row):
        row[7] = row[7].strftime("%d/%m/%Y")
        row[8] = row[8].strftime("%d/%m/%Y")
        return row

    def rentals_lease_start_date_filter(self, start, end):
        date_range = self._get_date_range(start, end)
        applicable_rows = []
        for row in self.data:
            if row[7] in date_range:
                applicable_rows.append(self._format_row_dates(row))
        applicable_rows.insert(0, self.headers)
        return applicable_rows


