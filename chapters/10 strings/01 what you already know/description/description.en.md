In Chapter
<a href="#ch:expressions" data-reference-type="ref" data-reference="ch:expressions">4</a>,
strings were quickly introduced. The brief discussion in that chapter
ended with the statement that a string is a text, enclosed by either
single or double quotes, which might be of any length, including zero
characters long. The chapter also explained that you can concatenate two
strings using the `+`, and that you can create a string that is the
repetition of a shorter string by using a `*`. For example:

```python
s1 = "apple"
s2 = 'banana'
print( s1 )
print( s2 )
print( s1 + s2 )
print( 3 * s1 )
print( s2 * 3 )
print( 2 * s1 + 2 * s2 )
```

Chapter
<a href="#ch:simplefunctions" data-reference-type="ref" data-reference="ch:simplefunctions">6</a>
introduced the `format()` function to format strings. It also explained
how you can get the length of a string using the `len()` function.

String comparisons were explained in Chapter
<a href="#ch:conditions" data-reference-type="ref" data-reference="ch:conditions">7</a>,
in particular the fact that the comparison operators compare strings
using alphabetical rules, whereby capitals are always lower in the
alphabet than lower case letters. This will be explained more in-depth
in the present chapter. Chapter
<a href="#ch:conditions" data-reference-type="ref" data-reference="ch:conditions">7</a>
also explained how the `in` operator can be used to test the presence of
characters or substrings in strings.

Chapter
<a href="#ch:iterations" data-reference-type="ref" data-reference="ch:iterations">8</a>
explained how you can use a `for` loop to traverse all the characters in
a string.

```python
s1 = "orange"
s2 = "banana"
for letter in s1:
    if letter in s2:
        print( s1, "and", s2, "share the letter", letter )
```
