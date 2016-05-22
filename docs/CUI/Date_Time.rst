========================
CUI Date Time Processing
========================

The CUI defines the standard date time format as dd-mmm-YYYY HH:MM (eg. 08-Aug-1970 08:40).

The CUI date/time is a class which allows dates to be manipulated as if they were python standard library datetimes, with the addition of an easy way of inputing and outputing the datetime in the standard CUI format above.

Recognising that not every interface will produce date/times in the CUI format, it is also posible to easily create CUI standard dates/times from other input formats, such as POSIX timestamps and standard library datetime instances.

.. warning::

  The current implementation of the CUI Date/time class is not fully timezone aware. This **WILL** be resolved in a upcoming update.


DateTime Class
--------------

.. code-block:: python

    nhspy.cui.DateTime( initial=None )

The ``initial`` argument is as follows :

    - ``initial`` is None : The DateTime instance is created from the current local date/time.
    - ``initial`` is a number (integer, floating point or a Decimal), then this number is a POSIX timestamp (count of seconds since 01-Jan-1970 00:00. The DateTime class will accept and process fractional timestamps correctly, although the standard CUI format displays data with a resolution of 1 minute only.
    - ``initial`` is a string, then it is expected to be formatted in a CUI Date format (dd-mmm-YYYY HH:MM). If the string is not formatted in the expected format, a ValueError exception will be raised.
    - ``initial`` is a Python standard library datetime, the DateTime instance will represent the same date/time as the datetime instance.

Manipulating DateTime instances
-------------------------------

DateTime instances can be manipulated the same as any standard library datetime. Elements can be extracted by using the standard datetime attributes :

+-----------------+-----------------------------------------+---------------------------------+
| Attribute       | Definition                              | Range                           |
+=================+=========================================+=================================+
| year            | The year                                | From ``MINYEAR`` to ``MAXYEAR`` |
+-----------------+-----------------------------------------+---------------------------------+
| month           | The month number (from 1)               | From 1 to 12 inclusive          |
+-----------------+-----------------------------------------+---------------------------------+
| day             | The day of the month                    | From 1 to 31 inclusive          |
+-----------------+-----------------------------------------+---------------------------------+
| hour            | The hour on the 24 hour clock           | From 0 to 23 inclusive          |
+-----------------+-----------------------------------------+---------------------------------+
| minute          | Minutes past the current hour           | From 0 to 59 inclusive          |
+-----------------+-----------------------------------------+---------------------------------+
| second          | Seconds within the current minute       | From 0 to 59 inclusive          |
+-----------------+-----------------------------------------+---------------------------------+
| microsecond     | microseconds with the current second    | From 0 to 999999 inclusive      |
+-----------------+-----------------------------------------+---------------------------------+

DateTime instances can be compared to standard library datetimes, and can have timedelta instances added and subtracted from them. In all cases they behave exactly the same as standard library datetimes. See the `Python Standard Library datetime module`_ for more details.

.. _`Python Standard Library datetime module`: https://docs.python.org/2.7/library/datetime.html

Output for CUI DateTime
-----------------------

The DateTime class is intended to work well with the standard ``.format`` output method to allow
control over the formatting of how the information is output.

A format type of `v` will always output the DateTime in the CUI DateTime format :

.. code-block:: Python

    >>> from nhspy.cui import DateTime
    >>> "{0:v}".format(DateTime(0)) # Create CUI Date format for 1970/01/01 00:00 (timestamp=0)
    '01-Jan-1970 00:00'

With the `v` format type the full format specifier is :

    **[[fill]align][width]v** where :

      - ``fill`` : A single fill character which is used when the output is aligned within a fixed width. Defaults to a space.
      - ``align`` : One of ``>`` (right align - default) ``<`` (left align) or ``^`` (centered).
      - ``width`` : An integer given the the minimum text width for the output. Note the standard format is always 17 characters long.

If the ``v`` format is not used, then the following other output formats can be used :

    - an empty format string (i.e. no type, alignment, width or other fill character) will generate a string containing the date in ISO format : 'YYYY-mm-dd HH:MM:SS.
    - The format specifier might also contain one or more datetime part format specifiers, as would be passed to ``.strftime``. See also See the `Python Standard Library datetime module - strftime & strptime behaviour`_ for more details.

.. _`Python Standard Library datetime module - strftime & strptime behaviour`: https://docs.python.org/2.7/library/datetime.html?highlight=datetime.__format__#strftime-strptime-behavior
