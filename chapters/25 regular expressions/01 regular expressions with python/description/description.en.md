Regular expressions are text strings that describe a "pattern" that can
be found in textual data. For example, the regular expression `a+`
describes a pattern that consists of a sequence of one or more times the
letter "a." In the string "aardvark" this pattern can be found twice,
namely as the "aa" at the start of the string, and the single "a" in the
second half of the string.

A regular expression always consists of a string, which may contain any
character. Some characters are "meta-characters" which have a special
meaning in regular expressions. You should be careful when using them
(how you should use them will be discussed later). The meta-characters
are:

    . ^ $ * + ? { } [ ] \ | ( )

I will discuss how to write regular expressions later in this chapter.
First, I need to discuss how to use regular expressions in Python code.

### The `re` module

To use regular expressions in Python, you must import the `re` module.

A regular expression can be considered a piece of code. That code can be
"compiled" by the `re` module to produce a "pattern object." That
pattern object can then be used to search for the pattern in data. For
instance, in the following code, the regular expression `a+` is compiled
to produce a pattern stored as `pAplus`, which is then used to search
for the pattern in the string "aardvark." It stores the occurrences of
the pattern as a list, and prints that list.

```python
import re

pAplus = re.compile( r"a+" )
lAplus = pAplus.findall( "aardvark" )
print( lAplus )
```

You can change the word "aardvark" into something else, and see how that
affects the output.

You might be wondering what that letter "r" is doing in front of the
regular expression string. Why did I write `r"a+"` instead of just
`"a+"`? This letter "r" tells Python that it should consider the string
as "raw data," i.e., it should not try to convert parts of the string
according to standard Python string interpretations. This is mainly
necessary when the regular expression contains `"\\b"`, which for
regular expressions means "word boundary" (I will get to that later in
this chapter), but for Python is an escape sequence that means
"backspace." So it is good practice to always put that "r" in front of a
regular expression, to avoid problems.

While it is seldom done in practice, you may add an optional second
parameter (a so-called "flag") to the `compile()` call, which indicates
a special way to use the created pattern. The parameter `re.I` indicates
that the pattern should be used case-insensitively, while `re.S`
indicates that the pattern should also process newlines, and `re.M`
indicates that the pattern should match the meta-characters `^` and `\$`
to every line of the text, and not just the text as a whole. You may
combine them by putting pipe-lines (`|`) between them.

### Shorthand

You are allowed to skip the compile-step, and call the pattern search
using a class call to the `re` module. Instead of calling methods of the
pattern that the compilation produced, I can directly call the method
for `re`, and use the regular expression as the first parameter. The
code above then becomes:

```python
import re

lAplus = re.findall( r"a+", "aardvark" )
print( lAplus )
```

If you run this code, you will notice that the output is exactly the
same as for the first bit of code. The second approach still compiles
the regular expression, but does not store the pattern. If a pattern is
only needed a few times in a program, the second approach is fine.
However, if it is used many times, the first approach is preferred, as
in the first approach the compilation of the regular expression (which
takes by far the most time of the whole process) is only done once, as
opposed to every time.

### Match objects

The `findall()` method used above returns the occurrences of the pattern
in the target string. Often you need more information than just the
actual patterns; for instance, you might want to know where the pattern
occurs in the target string. The `re` module has methods that result in
so-called "match objects," which are objects that contain, besides the
textual result, more information, such as the index where the result is
found in the target string. For example, the `search()` method returns a
match object for the first occurrence of a pattern in a string.

```python
import re

m = re.search( r"a+", "Look out for the aardvark!" )
print( "{} is found at index {}".format( m.group(), m.start() ) )
```

As you can see, the match object has several useful methods. These are:

-   `group()` to return the found pattern

-   `start()` to return the index at which the pattern starts

-   `end()` to return the index where the pattern has ended

The `group()` method has some handy applications which you can control
with parameters, which I will get to later.

The `match()` method is similar to the `search()` method, but checks if
the pattern exists at the very start of a string. Both methods will
return `None` if the pattern is not found, which as a condition is
processed by Python as `False`.

```python
import re

m = re.match( r"a+", "Look out for the aardvark!" )
if m:
    print( "{} starts the string".format( m.group() ) )
else:
    print( "The pattern is not found at the start of the string")    
```

### Lists of matches

I already showed that the `findall()` method creates a list of
occurrences of a pattern in a string. The `finditer()` method is its
complement, which creates a list (or rather, an iterator) of match
objects for where the pattern occurs in a string. The best way to
process such a list is by using the `for m in ...` approach. For
example:

```python
import re

mlist = re.finditer( r"a+", 
    "Look out! A dangerous aardvark is on the loose!" )
for m in mlist:
    print( "{} starts at index {} and ends at index {}.".format( 
        m.group(), m.start(), m.end() ) )
```
