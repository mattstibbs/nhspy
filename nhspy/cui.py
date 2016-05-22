#!/usr/bin/env python
# coding=utf-8
"""
# nhspy : Implementation of cui

Summary :
    Implements Common User Interface formatting for key functionality
Use Case :
    As a Developer I want standard common user Interface Library So that I can develop applications which will
    display data in a consistent manner

Testable Statements :
    Can I input date/time information in the CUI date format (dd-mmm-YYYY HH:MM)
    Can I manipulate date/time information is manner compliant with python standard libraries
    Can I output date/time information in the CUI date format (dd-mmm-YYYY HH:MM)
    ....
"""

import re
from datetime import datetime
from numbers import Real

__author__ = 'Tony Flury : anthony.flury@btinternet.com'
__created__ = '21 May 2016'


class _Core(object):
    """ _Core mixin - a place for common cui functionality
        All Cui Data types must inherit from _Core
    """
    fmt_spec = re.compile(
        r"""
         (?x)                           # Allow Verbose
         (
            (?P<fill>.?)                # Optional Fill Character
            (?P<align>[<>^]?)           # Optional Align Character
         )
         (?P<width>\d*?)                # Optional Width specifier
         v                              # Format type is v
          """)

    def __format__(self, format_spec):
        raise NotImplemented(
            "All cui data types must implement their own __format__ method if their "
            "other baseclass does not support it")

# noinspection PyInitNewSignature
class DateTime(datetime, _Core):
    """Date class - supports all the normal date/tme functions, and nhs cui formatting"""

    def __new__(cls, initial=None):
        """ Create a CUI compliant DateTime Object, from the initial value
            initial : Either
                    numeric - a timestamps of seconds since 1970-01-01 00:00
                    datetime - a value derived from the datetime module
                    string - a text value in nhs standard format (e.g. 01-Jan-1970 01:20)
                if initial is not provided - defaults to now()
        """

        initial_date = None

        if initial is None:
            initial_date = datetime.now()

        if isinstance(initial, Real):
            initial_date = datetime.utcfromtimestamp(initial)

        if isinstance(initial, str):
            initial_date = datetime.strptime(initial, '%d-%b-%Y %H:%M')

        if isinstance(initial, datetime):
            initial_date = initial

        if initial_date is None:
            raise ValueError(
                'Invalid value for initial argument - must be a numeric, string, datetime, Callable or None')

        return datetime.__new__(cls, initial_date.year, initial_date.month, initial_date.day,
                                initial_date.hour, initial_date.minute, initial_date.second, initial_date.microsecond,
                                initial_date.tzinfo)

    def __format__(self, format_spec):
        """ Magic method to implement customised formatting"""
        if not format_spec:  # No format spec - always return the ISO format
            return super(DateTime, self).__str__()

        fmt_match = DateTime.fmt_spec.match(format_spec)
        if fmt_match:
            val, fmt = self.strftime('%d-%b-%Y %H:%M'), format_spec[:-1] + "s"
            return "{val:{fmt}}".format(fmt=fmt, val=val)
        else:
            val, fmt = self, format_spec
            return super(DateTime, self).__format__(fmt)

    def __str__(self):
        return "{me:v}".format(me=self)


class NHSNumber(str, _Core):
    # noinspection PyMissingConstructor
    def __init__(self, number):
        """ Create a CUI compliant NHSNumber - basically a string with customised formatting

        :param number: The initial number - with or without separators
        """
        pass

    def __format__(self, format_spec):
        """ Magic method to implement customised formatting"""
        pass


class Name(_Core):
    def __init__(self, last_name='', first_name=''):
        """ Create a CUI compliant NHSNumber - basically a string with customised formatting

            :param last_name : The person's last name
            :param first_name : The person's first name
        """
        pass

    def __format__(self, format_spec):
        """ Magic method to implement customised formatting"""
        pass
