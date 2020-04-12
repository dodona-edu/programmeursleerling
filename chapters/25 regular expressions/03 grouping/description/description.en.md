As shown above, when parentheses are used in regular expressions, they
create so-called "groups." Take for instance the regular expression
`(\d{1,2})-(\d{1,2})-(\d{4})`, which describes a sequence that could
represent a date: one or two digits, followed by a dash, followed by one
or two digits, followed by a dash, followed by four digits (if you do
not understand this regular expression, check back in previous sections
of this chapter until you do understand it). This expression contains
three groups: the first containing one or two digits, the second
containing one or two digits, and the third one containing the four
digits at the end. The code below searches for this pattern in a string.

```python
import re

pDate = re.compile( r"(\d{1,2})-(\d{1,2})-(\d{4})" )
m = pDate.search( "In response to your letter of 25-3-2015, \
I decided to hire a hitman to get you." )
if m:
    print( "Date {}; day {}; month {}; year {}".format( 
            m.group(0), m.group(1), m.group(2), m.group(3) ) )
```

When you run the code, you see that it not only gets out the result as a
whole (using the method `group()` or `group(0)`), but that you can also
access each of the groups that is found in the result, using methods
`group(1)` for the day, `group(2)` for the month, and `group(3)` for the
year. You can also use the method `groups()` to get a tuple with all the
groups.

### `findall()` and groups

The `findall()` methods returns a list of pattern objects. In the
examples where it was used until now, it returned a list of strings.
Indeed, pattern objects are strings if there is at most one group in the
regular expression. If there are multiple groups, pattern objects are
actually tuples that contain all the groups.

```python
import re

pDate = re.compile( r"(\d{1,2})-(\d{1,2})-(\d{4})" )
datelist = pDate.findall( "In response to your letter of \
25-3-2015, on 27-3-2015 I decided to hire a hitman to get you." )
for date in datelist:
    print( date )
```

### Named groups

It is possible to give each group a name, by placing the construct
`?P<name>` (where you replace "name" with the name you want the group to
have – you leave the `<` and `>` in the expression in this case)
immediately after the opening parenthesis. You can then refer to the
groups by these names, instead of their index.

```python
import re

pDate = re.compile(
    r"(?P<day>\d{1,2})-(?P<month>\d{1,2})-(?P<year>\d{4})")
m = pDate.search( "In response to your letter of 25-3-2015, \
I curse you." )
if m:
    print( "day is {}".format( m.group('day') ) )
    print( "month is {}".format( m.group('month') ) )
    print( "year is {}".format( m.group('year') ) )
```

### Referring within a regular expression

Suppose that you have to create a regular expression that represents a
string that contains an arbitrary non-space character twice. For
instance, the string "regular" would not have a match, but the string
"expression" would (as it contains two `"e"`s and two `"s"`s). This
cannot be done with the regular expression features that we discussed
until now. It can be solved, however, with groups, and special
references within a regular expression, namely as follows: using the
special sequence `\\x`, whereby `x` is a number, you refer to the group
with index `x` in the match. Thus, a regular expression that represents
a string with an arbitrary non-space character twice is `(\\S).*\\1`.

Since at this point this regular expression might still be a bit hard to
understand, let's look at it in depth. The `\\S` is a special sequence
that represents a non-space character. Putting it in parentheses turns
it into a group, and since this is the first (and only) group in the
expression, its index is 1. The `.*` represents a sequence of zero or
more characters, which can be anything (the period is a meta-character
that represents any character). Finally, the `\\1` refers to the first
group, and says that here you want to have exactly the same thing as the
first group represents. If you are wondering why you do not need to
represent anything that can be placed before the `\\S`, or anything that
can come after the `\\1`, then the answer is that you are not specifying
that this regular expression represents a string as a whole, so as long
as it occurs anywhere in the string, it matches.

Test this pattern with the code below, by replacing the string
`"Monty Python's Flying Circus"` with different strings, and running the
code to examine the results.

```python
import re

m = re.search( r"(\S).*\1", "Monty Python's Flying Circus" )
if m:
    print( "The character {} occurs twice".format( m.group(1) ) )
else:
    print( "No match was found." )
```

Can you change the regular expression in the code above so that it
checks if the string contains a character at least three times?

Can you change the regular expression so that it checks whether it
contains at least two characters twice? This is quite hard and therefore
optional, but if you try to do it, make sure that you test it with at
least the strings `"aaaa"`, `"aabb"`, `"abab"` and `"abba"`. These all
should match, unless you also want the two repeated characters
different, then `"aaaa"` should not match (but note that that makes the
regular expression even harder to design).
