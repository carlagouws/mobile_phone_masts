import datetime as dt
import unittest
from unittest import mock
from parameterized import parameterized
from mobile_phone_masts import MobilePhoneMasts


class TestMobilePhoneMast(unittest.TestCase):
    @parameterized.expand(
        [
            ["10 Jun 2009", dt.date(2009, 6, 10)],
            ["10-Jun-09", dt.date(2009, 6, 10)],
        ]
    )
    def test_str_to_date(self, date_str, expected_result):
        result = MobilePhoneMasts("test_dataset_2.csv")._str_to_date(date_str)
        self.assertEqual(result, expected_result)

    @mock.patch("mobile_phone_masts.MobilePhoneMasts._read_data")
    def test_str_to_date_exception_handling(self, mock_read_data):
        with self.assertRaises(ValueError) as e:
            MobilePhoneMasts("no_file")._str_to_date("test_date")
        self.assertEqual(
            e.exception.args[0], "Unexpected datetime format for date test_date"
        )

    @mock.patch("mobile_phone_masts.MobilePhoneMasts._read_data")
    def test_correct_datatypes(self, mock_read_data):
        test_data = [
            "Shakespeare Towers",
            "",
            "",
            "",
            "LS9",
            "Shakespeare Towers ref 1704255985",
            "EverythingEverywhere Ltd & Hutchinson3GUK Ltd",
            "10 Jun 2009",
            "09 Jun 2019",
            "10",
            "12750.00",
        ]
        expected_result = [
            "Shakespeare Towers",
            "",
            "",
            "",
            "LS9",
            "Shakespeare Towers ref 1704255985",
            "EverythingEverywhere Ltd & Hutchinson3GUK Ltd",
            dt.date(2009, 6, 10),
            dt.date(2019, 6, 9),
            10,
            12750.0,
        ]
        result = MobilePhoneMasts("no_file")._correct_datatypes(test_data)
        self.assertEqual(result, expected_result)

    def test_read_data(self):
        expected_headers = [
            "Property Name",
            "Property Address [1]",
            "Property  Address [2]",
            "Property Address [3]",
            "Property Address [4]",
            "Unit Name",
            "Tenant Name",
            "Lease Start Date",
            "Lease End Date",
            "Lease Years",
            "Current Rent",
        ]
        expected_data = [
            [
                "Shakespeare Towers",
                "",
                "",
                "",
                "LS9",
                "Shakespeare Towers ref 1704255985",
                "EverythingEverywhere Ltd & Hutchinson3GUK Ltd",
                dt.date(2009, 6, 10),
                dt.date(2019, 6, 9),
                10,
                12750.0,
            ]
        ]
        result = MobilePhoneMasts("test_dataset_2.csv")
        self.assertEqual(result.headers, expected_headers)
        self.assertEqual(result.data, expected_data)

    def test_sorted_by_current_rent(self):
        expected_result = ["Current Rent", 6600.0, 12750.0, 14730.08, 15296.63, 23950.0]
        result = [
            i[-1] for i in MobilePhoneMasts("test_dataset.csv").sorted_by_current_rent()
        ]
        self.assertEqual(result, expected_result)

    def test_lease_years_of_25(self):
        expected_result = [
            [
                "Property Name",
                "Property Address [1]",
                "Property  Address [2]",
                "Property Address [3]",
                "Property Address [4]",
                "Unit Name",
                "Tenant Name",
                "Lease Start Date",
                "Lease End Date",
                "Lease Years",
                "Current Rent",
            ],
            [
                "Grayson Heights",
                "Eden Mount",
                "Burley Park",
                "Leeds",
                "LS5",
                "Grayson Heights LDS175   LS0029",
                "Everything Everywhere Ltd&Hutchison 3G UK Ltd",
                dt.date(2009, 8, 1),
                dt.date(2019, 7, 31),
                25,
                14730.08,
            ],
        ]
        result = MobilePhoneMasts("test_dataset.csv").lease_years_of_25()
        self.assertEqual(result, expected_result)

    def test_total_rent(self):
        tenants = MobilePhoneMasts("test_dataset.csv")
        self.assertEqual(tenants.total_rent(tenants.data), 73326.71)
