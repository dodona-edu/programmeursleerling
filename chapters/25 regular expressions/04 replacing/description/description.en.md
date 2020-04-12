While regular expressions are mainly used for searching, you can also
use regular expressions to replace substrings in a string with different
substrings. You can use the `sub()` method for this. `sub()` gets as
arguments the to-be-replaced pattern, the replacement, and the string.
The `sub()` method returns the new string (remember that strings are
immutable, so `sub()` will not actually change your original string,
even if it is stored in a variable; you will have to store its return
value if you want access to the new string).

The replacement is usually just a string, but it may contain references
to groups in the original pattern. You will have to use a format that is
different from the `\x` format shown before. If you want to refer to
group `x` in the pattern (`x` being a number), you write `\g<x>`. The
reason for the difference is disambiguation; it allows you to
distinguish a reference to, for instance, group 2 followed by a
character zero, from a reference to group 20.

```python
import re

s = re.sub( r"([iy])se", "\g<1>ze", "Whether you categorise, \
emphasise, or analyse, you should use American spelling!" )
print( s )
```
