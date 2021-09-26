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

    # def test_sorted_by_current_rent(self):
