The `datetime` module contains functions that allow the manipulation of
date and time. The module contains various classes for date and time
manipulation, of which the most important ones are `datetime`,
`timedelta`, `date`, and `time`. `datetime` contains attributes `year`,
`month`, `day`, `hour`, `minute`, `second`, `microsecond`, and `tzinfo`
(the last attribute provides time zone information). `date` and `time`
contain subsets of these attributes. Objects of these types are
immutable.

I restrict myself to discussing the `datetime` and `timedelta` classes,
though related functions and methods exist for the other classes.

`datetime` objects hold a date and a time. Amongst the methods for
`datetime` objects are:

-   `now()` creates a `datetime` object that contains the current day
    and time. You would typically use a class call to get a value for
    `now()`.

-   `datetime()` creates a `datetime` object using given arguments. The
    first three arguments are not optional, and are year, month, and
    day. The others, hour, minute, second, microsecond, and tzinfo are
    optional. Arguments can either be given in this order, or by
    specifying `<argument>=<value>`, with `<argument>` an argument name
    as specified above.

```python
from datetime import datetime

print( datetime.now() )
```

When printing `datetime` objects you get a specific format as output. If
you want a different format (including printing such things as the day
of the week) then the `datetime` module has functions that allow you to
specify different kinds of formatting. For more information, see the
Python reference.

To calculate with `datetime` objects, you need `timedelta`. A
`timedelta` object specifies a difference between two `datetime`
objects. A `timedelta` object stores `days`, `seconds`, and
`microseconds`. You can create `timedelta` objects with other
period-representing arguments, but it only stores the three mentioned
here; other arguments are recalculated into these three.

You can perform all kinds of calculations with `timedelta` objects, but
the most useful ones are concerning the difference between `datetime`
objects. So you can add a `timedelta` object to a `datetime` object to
get a new `datetime` object, or subtract two `datetime` objects from
each other to get their difference as a `timedelta` object.

```python
from datetime import datetime, timedelta

thisyear = datetime.now().year
xmasthisyear = datetime( thisyear, 12, 25, 23, 59, 59 )
thisday = datetime.now()
days = xmasthisyear - thisday

if days.days < 0:
    print( "Christmas will come again next year." )
elif days.days == 0:
    print( "It's Christmas!" )
else:
    print( "Only", days.days, "days to Christmas!" )
```
