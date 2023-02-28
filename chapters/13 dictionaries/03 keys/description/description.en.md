As I said, any immutable data type can be a dictionary key. This means
that strings, integers, and floats can all be used as keys. You may
remember that tuples are also immutable, which entails that you can use
tuples as keys. This can occasionally be useful.

A very straightforward example of tuples being useful as keys is a
dictionary in which you want to store information associated with points
in two-dimensional space (a discussion of which was given in Chapter
12).
There is no good way in which you can store the identification of a
point in a single number or string. It is not impossible (for instance,
you could store the number-pair as their string-representations,
concatenated with a comma in between) but it becomes ambiguous and
convoluted (for instance, the string-keys `"2,3"`, `"2, 3"`, `"+2,+3"`,
and `"02,03"` would all be representing the same tuple but different
keys).
