As I showed several times before, a string is a collection of characters
in a specific order. You can access the individual characters of a
string using indices.

### String indices

Each symbol in a string has a position, this position can be referred to
by the index number of the position. The index numbers start at 0 and
then increase to the length of the string. The following table shows the
word "python" in the first row and the indices for each letter in the
second and third rows:

| p | y | t | h | o | n |
|:-:|:-:|:-:|:-:|:-:|:-:|
| 0 | 1 | 2 | 3 | 4 | 5 |
| -6 | -5 | -4 | -3 | -2 | -1 |
{:class="table table-striped table-condensed" style="width:auto;margin-left:auto;margin-right:auto;"}

As you can see, you can use positive indices, which start at the first
letter of the string and increase until the end of the string is
reached, or negative indices, which start with -1 for the last letter of
the string and decrease until the first letter of the string is reached.

As the length of a string `s` is `len(s)`, the last letter of the string
has index `len(s)-1`. With negative indices, the first letter of the
string has index `-len(s)`.

If a string is stored in a variable, the individual letters of the
string can be accessed by the variable name and the index of the
requested letter between square brackets (`[]`) next to it.

```python
fruit = "orange"
print( fruit[1] ) 
print( fruit[2] ) 
print( fruit[3] )
print( fruit[-2] )
print( fruit[-6] )
print( fruit[0] )
print( fruit[-3] )
```

You can also use variables as indices, and even calculations or function
calls. You must make sure, however, that calculations result in
integers, because you cannot use floats as indices. Below are some
examples, most of which are so convoluted that I do not see any reason
to incorporate them like this in a program. But they show what is
possible.

```python
from math import sqrt

fruit = "orange"
x = 3

print( fruit[3-2] )
print( fruit[int( sqrt( 4 ) )] )
print( fruit[2**2] )
print( fruit[int( (x-len( fruit ))/3 )] )
print( fruit[-len( fruit )])
print( fruit[-x] )
```

In principle, you can also use an index with the actual string rather
than a variable that contains it, e.g., `"orange"[2]` is the letter
`"a"`. For obvious reasons no one ever does that, though.

Besides using single indices you can also access a substring (also
called a "slice") from a string by using two numbers between the square
brackets with a colon (:) in between. The first of these numbers is the
index where the substring starts, the second where it ends. The
substring does not include the letter at the second index. By leaving
out the left number you indicate that the substring starts at the
beginning of the string (i.e., at index 0). By leaving out the right
number you indicate that the substring ranges up to and includes the
last character of the string.

If you try to access a character using an index that is beyond the
reaches of a string, you get a runtime error ("index out of bounds").
For a range of indices to access substrings such limitations do not
exist; you can use numbers that are outside the bounds of the string.

```python
fruit = "orange"
print( fruit[:] )
print( fruit[0:] )
print( fruit[:6] )
print( fruit[:100] )
print( fruit[:len( fruit )] )
print( fruit[1:-1] )
print( fruit[2], fruit[1:6] )
```

### Traversing strings

I already explained how you can traverse the characters of a string
using a `for` loop:

```python
fruit = 'apple'
for char in fruit:
    print( char, '- ', end='' )
```

Now you know about indices, you probably realize you can also use those
to traverse the characters of a string:

```python
fruit = 'apple'

for i in range( 0, len( fruit ) ):
    print( fruit[i], "- ", end="" )
print()

i = 0
while i < len( fruit ):
    print( fruit[i], "- ", end="" )
    i += 1
```

If you just want to traverse the individual characters of a string, the
first method, using `for <character> in <string>:`, is by far the most
elegant and readable. However, occasionally you have to solve problems
in which you might prefer one of the other methods.

Write code that for a string prints the indices of all of its vowels (a,
e, i, o, and u). This can be done with a `for` loop or a `while` loop,
though the `while` loop is more suitable.

Write code that uses two strings. For each character in the first string
that has exactly the same character at the same index in the second
string, you print the character and the index. Watch out that you do not
get an "index out of bounds" runtime error. Test it with the strings
`"The Holy Grail"` and `"Life of Brian"`.

Write a function that takes a string as argument, and creates a new
string that is a copy of the argument, except that every non-letter is
replaced by a space (e.g., `"ph@t l00t"` is changed to `"ph t l  t"`).
To write such a function, you will start with an empty string, and
traverse the characters of the argument one by one. When you encounter a
character that is acceptable, you add it to the new string. When it is
not acceptable, you add a space to the new string. Note that you can
check whether a character is acceptable by simple comparisons. For
example, any lower case letter can be found using the test
`if ch >= 'a' and ch <= 'z':`.

### Extended slices

Slices in python can take a third argument, which is the step size (or
"stride") that is taken between indices. It is similar to the third
argument for the `range()` function. The format for slices then becomes
`<string>[<begin>:<end>:<step>]`. By default the step size is 1.

The most common use for the step size is to use a negative step size in
order to create a reversed version of a string.

```python
fruit = "banana"
print( fruit[::2] )
print( fruit[1::2] )
print( fruit[::-1] ) 
print( fruit[::-2] ) 
```

Reversing a string using `[::-1]` is conceptually similar to traversing
the string from the last character to the beginning of the string using
backward steps of size 1.

```python
fruit = "banana"
print( fruit[::-1] )
for i in range( 5, -1, -1 ):
    print( fruit[i] )
```
