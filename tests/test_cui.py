#!/usr/bin/env python
# coding=utf-8
"""
# nhspy : Test Suite for test_cui.py

Summary :
    <summary of module/class being tested>
Use Case :
    As a <actor> I want <outcome> So that <justification>

Testable Statements :
    Can I <Boolean statement>
    ....
"""

import unittest
from datetime import datetime, timedelta

import nhspy.cui as cui

__version__ = "0.1"
__author__ = 'Tony Flury : anthony.flury@btinternet.com'
__created__ = '21 May 2016'


class TestCUIDate(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_000_001_DefaultCreation(self):
        """DateTime object with default parameters is created correctly"""
        now = datetime.now()
        cui_datetime = cui.DateTime()
        self.assertIsInstance(cui_datetime, cui.DateTime)
        self.assertLessEqual(cui_datetime-now, timedelta(milliseconds=100))

    def test_010_001_CreateFromTimeStamp(self):
        """DateTime object can be created from a valid timestamp"""
        ts = 1000.0
        cui_datetime = cui.DateTime( initial=ts)
        ts_date = datetime.utcfromtimestamp(ts)
        self.assertEqual(cui_datetime, ts_date)

    def test_010_002_CreateFromInvalidTimeStamp(self):
        """DateTime object cannot be created from a invalid timestamp"""
        ts = -62135596800 # 00:00 1st Jan 1 AD
        ts = ts - 86400
        with self.assertRaises(ValueError):
            cui_datetime = cui.DateTime(initial=ts)
            print cui_datetime

    def test_020_001_CreateFromStringNoLeadingZero(self):
        """DateTime Object created from a string in CUI format - day of month > 10"""
        date_str = '17-Aug-1966 08:40'
        dt = datetime(year=1966, month=8, day=17, hour=8, minute=40, second=0, microsecond=0, tzinfo=None)
        cui_datetime = cui.DateTime(initial=date_str)
        self.assertEqual(cui_datetime, dt)

    def test_020_002_CreateFromStringLeadingZero(self):
        """DateTime Object created from a string in CUI format - Leading zero day of month"""
        date_str = '07-Aug-1966 08:40'
        dt = datetime(year=1966, month=8, day=7, hour=8, minute=40, second=0, microsecond=0, tzinfo=None)
        cui_datetime = cui.DateTime(initial=date_str)
        self.assertEqual(cui_datetime, dt)

    def test_020_003_CreateFromStringInvalidDay(self):
        """DateTime Object created from a string in CUI format - Invalid day of month"""
        date_str = '32-Aug-1966 08:40'
        with self.assertRaises(ValueError):
            cui_datetime = cui.DateTime(initial=date_str)

    def test_020_004_CreateFromStringInvalidMonth(self):
        """DateTime Object created from a string in CUI format - Invalid month"""
        date_str = '01-Bed-1966 08:40'
        with self.assertRaises(ValueError):
            cui_datetime = cui.DateTime(initial=date_str)

    def test_020_005_CreateFromStringInvalidYear(self):
        """DateTime Object created from a string in CUI format - Invalid year"""
        date_str = '01-Aug-ABCD 08:40'
        with self.assertRaises(ValueError):
            cui_datetime = cui.DateTime(initial=date_str)

    def test_020_006_CreateFromStringInvalidHour(self):
        """DateTime Object created from a string in CUI format - Invalid Hour"""
        date_str = '01-Aug-1966 25:40'
        with self.assertRaises(ValueError):
            cui_datetime = cui.DateTime(initial=date_str)

    def test_020_007_CreateFromStringInvalidHour(self):
        """DateTime Object created from a string in CUI format - Invalid Minute"""
        date_str = '01-Aug-1966 08:64'
        with self.assertRaises(ValueError):
            cui_datetime = cui.DateTime(initial=date_str)

    def test_030_001_CreateFromStandardDateTime(self):
        """DateTime Object created from a datetime.datetime object from the standard Libary"""
        then = datetime.now() + timedelta(days=1)
        cui_datetime = cui.DateTime(initial=then)
        self.assertEqual(cui_datetime, then)

    def test_040_001_CreationInvalidValueTypeList(self):
        """DateTime object cannot be created an Invalid Type - for instance a list"""
        with self.assertRaises(ValueError):
            cui_datetime = cui.DateTime(initial = [])

    def test_040_002_CreationInvalidValueTypeTuple(self):
        """DateTime object cannot be created an Invalid Type - for instance a tuple"""
        with self.assertRaises(ValueError):
            cui_datetime = cui.DateTime(initial=(0,))

    def test_040_003_CreationInvalidValueTypeDictionary(self):
        """DateTime object cannot be created an Invalid Type - for instance a dictionary"""
        with self.assertRaises(ValueError):
            cui_datetime = cui.DateTime(initial=dict())

    def test_050_001_FormattingISOFormat(self):
        """DateTime object can be formatted as a ISO standard time"""
        dt = datetime(day=17, month=8, year=1966, hour=8, minute=40, tzinfo=None)
        dt_str = "{}".format(cui.DateTime(initial=dt))
        self.assertEqual(dt_str, '1966-08-17 08:40:00')

    def test_050_002_FormattingCUIFormat(self):
        """DateTime object can be formatted as a CUI standard format"""
        dt = datetime(day=17, month=8, year=1966, hour=8, minute=40, tzinfo=None)
        dt_str = "{0:v}".format(cui.DateTime(initial=dt))
        self.assertEqual(dt_str, '17-Aug-1966 08:40')

    def test_050_003_FormattingCUIFormatPaddingAlignWidth(self):
        """DateTime object can be formatted as a CUI standard format with Padding, width and alignment"""
        dt = datetime(day=17, month=8, year=1966, hour=8, minute=40, tzinfo=None)
        dt_str = "{0:#>20v}".format(cui.DateTime(initial=dt))
        self.assertEqual(dt_str, '###17-Aug-1966 08:40')

    def test_050_004_FormattingCUIFormatCenter(self):
        """DateTime object can be formatted as a CUI standard format centered"""
        dt = datetime(day=17, month=8, year=1966, hour=8, minute=40, tzinfo=None)
        dt_str = "{0: ^20v}".format(cui.DateTime(initial=dt))
        self.assertEqual(dt_str, ' 17-Aug-1966 08:40  ')

    def test_050_005_FormattingCUIDateFormatting(self):
        """DateTime object can be formatted using the normal datetime format strings"""
        dt = datetime(day=17, month=8, year=1966, hour=8, minute=40, tzinfo=None)
        dt_str = "{0:%Y/%m/%d}".format(cui.DateTime(initial=dt))
        self.assertEqual(dt_str, '1966/08/17')

    def test_060_001_strMethod(self):
        """DateTime object formatted using the str() method"""
        dt = datetime(day=17, month=8, year=1966, hour=8, minute=40, tzinfo=None)
        dt_str = str(cui.DateTime(initial=dt))
        self.assertEqual(dt_str, '17-Aug-1966 08:40')

def load_tests(loader, tests=None, pattern=None):
    classes = [TestCUIDate]
    suite = unittest.TestSuite()
    for test_class in classes:
        tests = loader.loadTestsFromTestCase(test_class)
        suite.addTests(tests)
    return suite

if __name__ == '__main__':
    ldr = unittest.TestLoader()

    test_suite = load_tests(ldr)

    unittest.TextTestRunner(verbosity=2).run(test_suite)
