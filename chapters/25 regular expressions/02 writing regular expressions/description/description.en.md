Now the basics of using regular expression in Python via the `re` module
have been explained, I can get into the actual writing of regular
expressions.

### Regular expressions with square brackets

The simplest regular expression is a string of characters, which
describes a pattern consisting of exactly that string of characters. You
may also describe a range of characters using square brackets `[` and
`]`. For instance, the regular expression `[aeiou]` describes any of the
characters `"a"`, `"e"`, `"i"`, `"o"`, or `"u"`. This means that if
`[aeiou]` is part of a regular expression, at that location in the
pattern one of these letters must reside (note: exactly one of them, so
not multiple). For instance, to search for the words `"ball"`, `"bell"`,
`"bill"`, `"boll"` and `"bull"`, the regular expression `b[aeiou]ll` can
be used.

```python
import re

slist = re.findall( r"b[aeiou]ll", "Bill Gates and Uwe Boll \
drank Red Bull at a football match in Campbell." )
print( slist )
```

Change the regular expression above so that it not only finds the words
"ball" and "bell", but also "Bill", "Boll", and "Bull".

You can use a dash within the square brackets between two characters to
indicate that they represent not only these two characters, but also all
the characters in between. For instance, the regular expression
`[a-dqx-z]` is equivalent to `[abcdqxyz]`. To describe any of the
letters of the alpabet, either as capital or lower case, you can use
`[A-Za-z]`.

Moreover, if you place a caret (`^`) right next to the opening square
bracket, that means that you want the opposite of what is within the
square brackets. For instance, `[^0-9]` indicates any character except
for a digit.

### Special sequences

In a regular expression, just like in strings, the backslash character
(\\) indicates that the character that follows it has a special meaning,
i.e., it is an escape sequence. The escape sequences that hold for
strings also hold for regular expressions, but regular expressions have
many more. There are also a few meta-characters that are interpreted in
a particular way. The following special sequences are defined (there are
more, but these are the most common ones):

| symbol | meaning |
|:-------:|:----------|
| `\b` | word boundary (zero-width) |
| `\B` | not a word boundary (zero-width) |
| `\d` | digit `[0-9]` |
| `\D` | not a digit`[^0-9]` |
| `\n` | newline |
| `\r` | return |
| `\s` | whitespace (including tabulation) |
| `\S` | not a whitespace |
| `\t` | tabulation |
| `\w` | alphanumeric character `[A-Za-z0-9_]` |
| `\W` | not an alphanumeric character `[^A-Za-z0-9_]` |
| `\/` | forward slash |
| `\\` | backslash |
| `\"` | double quote |
| `\'` | single quote |
| `^` | start of a string (zero-width) |
| ` $` | end of a string (zero-width) |
| `.` | any character |
{:class="table table-striped table-condensed" style="width:auto;margin-left:auto;margin-right:auto;"}

Note that "zero-width" means that the sequence does not represent a
character, but a position in the string between two characters (or the
start or end of the string). For instance, the regular expression `^A`
represents a string that starts with the letter `"A"`.

Moverover, you can place characters or substrings between parentheses,
in which case the characters are "grouped." Within a group, you can
indicate a choice between multiple (sequences of) characters by placing
pipe-lines (`|`) between them. For instance, the regular expression
`(apple|banana|orange)` is the string `"apple"` or the string `"banana"`
or the string `"orange"`.

You should be aware that some of these special sequences (in particular
those without a backslash, the parentheses, and the pipe-line) do not
work like indicated here when placed within square brackets. For
instance, a period within square brackets does not mean "any character,"
but an actual period.

### Repetition

Where regular patterns get really interesting is when repetitions are
used. Several of the meta-characters are used to indicate that (part of)
a regular expression is repeated multiple times. In particular, the
following repetition operators are often used:

| symbol | meaning |
|:-------:|:----------|
| `*` | zero or more times |
| `+` | one or more times |
| `?` | zero or one time |
| `{p,q}` | at least p and at most q times |
| `{p,}` | at least p times |
| `{p}` | exactly p times |
{:class="table table-striped table-condensed" style="width:auto;margin-left:auto;margin-right:auto;"}

You place such an operator after the (part of the) expression it
repeats. For instance, `ab*c` means the letter `"a"`, followed by zero
or more times the letter `"b"`, followed by the letter `"c"`. Thus, it
matches the strings `"ac"`, `"abc"`, `"abbc"`, `"abbbc"`, `"abbbbc"`,
etcetera.

A repetition operator after a group (between parentheses) indicates the
repetition of the whole group. For instance, `(ab)*c` matches the
strings `"c"`, `"abc"`, `"ababc"`, `"abababc"`, `"ababababc"`, etcetera.

Regular expression matching for repetitions is greedy. It will always
try to match the earliest occurring pattern first, extended to its
longest possible extension. For example:

```python
import re

mlist = re.finditer(r"ba+","A sheep says 'baaaaah' to Ali Baba.")
for m in mlist:
    print( "{} is found at {}.".format(m.group(), m.start()))
```

Change the regular expression in the code above so that it finds any
`"b"` followed by one or more `"a"`s, where the `"b"` might be
captitalized. The output should be `"baaaaa"`, `"Ba"` and `"ba"`.

Once you have solved the previous exercise, change the regular
expression so that it finds the pattern consisting of a `"b"` or `"B"`
followed by a sequence of one or more `"a"`s, repeated one or more
times. The output should be `"baaaaa"` and `"Baba"`. You will need to
use parentheses for this. When you think that your regular expression is
correct, also test it on several other strings.

Here is another one, which searches for occurrences of one or more
`"a"`s:

```python
import re

mlist = re.finditer(r"a+","A sheep says 'baaaaah' to Ali Baba.")
for m in mlist:
    print( "{} is found at {}.".format(m.group(), m.start()))
```

When you run this code, you see that it finds four occurrences of the
pattern: three times a single `"a"`, and one time a sequence of five
`"a"`s. You might wonder why the pattern matching process does not also
find the four `"a"`s starting at position 16, the three `"a"`s starting
at position 17, the two `"a"`s starting at position 18, and the single
`"a"` starting at position 19. The reason is that the `finditer()` and
`findall()` methods, when they find a match, continue searching
immediately after the end of the last found match. Normally, this is the
behavior that you want.

Now change the `r"a+"` in the code above to `r"a*"`, which changes it to
searching for zero or more `"a"`s. Before running the code, think about
what you expect the outcome to be. Then run the code and see if your
prediction was correct. If it wasn't, do you now realize why the outcome
is what it is?

You may have noticed that regular expressions may become overly complex
fast. It is a good idea to comment them so that you can understand them
on later examination.

### Practice

With all you learned until now, you should be able to do the following
exercise. It is wise to solve this one before continuing with the
remainder of this chapter. The exercise consists of a piece of code that
you have to complete.

When you run the code below, it tries to search for all the regular
expressions in `relist`, in all the strings in `slist`. It prints for
each string the numbers of all the regular expressions for which matches
are found. Your goal is to fill in the regular expressions in `relist`
according to the specification in the comments to the right of each
expression. Note that the first seven regular expressions need to cover
the string as a whole, so you should have them start with a caret and
end with a dollar sign, which indicates that the expression should match
the string from the start to the end.

```python
import re

# List of strings used for testing.
slist = [ "aaabbb", "aaaaaa", "abbaba", "aaa", "gErbil ottEr",
    "tango samba rumba", " hello world ", " Hello World " ]

# List of regular expressions to be completed by the student.
relist = [
    r"",  # 1. Only a's followed by only b's, including ""
    r"",  # 2. Only a's, including ""
    r"",  # 3. Only a's and b's, in any order, including "" 
    r"",  # 4. Exactly three a's
    r"",  # 5. Neither a's nor b's, but "" allowed
    r"",  # 6. An even number of a's (and nothing else)
    r"",  # 7. Exactly two words, regardless of white spaces
    r"",  # 8. Contains a word that ends in "ba"
    r""   # 9. Contains a word that starts with a capital
]

for s in slist:
    print( s, ':', sep='', end=' ' )
    for i in range( len( relist ) ):
        m = re.search( relist[i], s )
        if m:
            print( i+1, end=' ' )
    print()
```

The correct output is:

```
aaabbb: 1 3   
aaaaaa: 1 2 3 6    
abbaba: 3 8    
aaa: 1 2 3 4     
bEver ottEr: 7    
tango samba rumba: 8     
 hello world : 5 7     
 Hello World : 5 7 9
```

Make sure that you can do all of these correctly before you continue!
