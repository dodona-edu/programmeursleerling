There is a collection of methods that are designed to operate on
strings. All of these methods are applied to a string to perform some
operation. Since strings are immutable, they never change the string
they work on, but they always return a changed version of the string.

Like the `format()` method introduced in Chapter
<a href="#ch:simplefunctions" data-reference-type="ref" data-reference="ch:simplefunctions">6</a>,
all these methods are called using the syntax `<string>.<method>()`,
i.e., you have to write the string that they work on before the method
call, with a period in between. You will encounter this more often, and
why this is implemented in this way will be explained later in the
course, in the chapters about object orientation.

Most of these methods are not part of a specific module, but can be
called without importing them. There is a `string` module that contains
specific constants and methods that can be used in your programs, but
the methods I discuss here can all be used without importing the
`string` module.

### `strip()`

`strip()` removes from a string leading and trailing spaces, including
leading and trailing newlines and other characters that may be viewed as
spaces. If instead of spaces, you want to remove different characters,
you can add a string parameter that consists of all characters you want
to be removed.

```python
s = "    And now for something completely different \n    "
print( "["+s+"]" )
s = s.strip()
print( "["+s+"]" )
```

### `upper()` and `lower()`

`upper()` creates a version of a string of which all letters are
capitals. `lower()` is equivalent, but uses only lower case letters.
Neither method uses parameters.

```python
s = "The Meaning of Life"
print( s )
print( s.upper() )
print( s.lower() )
```

### `find()`

`find()` can be used to search in a string for the starting index of a
particular substring. As parameters it gets the substring, and
optionally a starting index to search from, and an ending index. It
returns the lowest index where the substring starts, or -1 if the
substring is not found.

```python
s = "Humpty Dumpty sat on the wall"
print( s.find( "sat" ) )
print( s.find( "t" ) )
print( s.find( "t", 12 ) )
print( s.find( "q" ) )
```

### `replace()`

`replace()` replaces all occurrences of a substring with another
substring. As parameters it gets the substring to look for, and the
substring to replace it with. Optionally, it gets a parameter that
indicates the maximum number of replacements to be made.

I must stress again that strings are immutable, so the `replace()`
function is not actually changing the string. It returns a new string
that is a copy of the string with the replacements made.

```python
s = 'Humpty Dumpty sat on the wall'
print( s.replace( 'sat on', 'fell off' ) )
```

### `split()`

`split()` splits a string up in words, based on a given character or
substring which is used as separator. The separator is given as the
parameter, and if no separator is given, the white space is used, i.e.,
you split a string in the actual words (though punctuation attached to
words is considered part of the words). If there are multiple
occurrences of the separator next to each other, the extra ones are
ignored (i.e., with the white space as separator, it does not matter if
there is a single white space between two words, or multiple).

The result of this split is a so-called "list" of words. Lists are
discussed in a coming chapter, so for now I will not say much about
them. I just indicate that if you want to access the separate words, you
can use the `for <word> in <``list``>:` construction.

```python
s = 'Humpty Dumpty      sat    on the wall   '
wordlist = s.split()
for word in wordlist:
    print( word )
```

A very useful property of splitting is that we can decode some basic
file formats. For example, a comma separated value (CSV) file is a very
simple format, of which the basic setup is that each line consists of
values that are separated by a comma. These values can be split from
each other using the `split()` method.[^6]

```python
csv = "2016,September,28,Data Processing,Tilburg University"
values = csv.split( ',' )
for value in values:
    print( value )
```

### `join()`

`join()` is the opposite of `split()`. `join()` joins a list of words
together, separated by a specific separator. This sounds like it would
be a method of lists, but for historic reasons it is defined as a method
for strings. Since all string methods are called using the format
`<string>.<method>()`, there must be a string in front of the call to
`join()`. That string is the separator that you want to use, while the
parameter of the method is the list that you want to join together. The
return value, as always, is the resulting string.

```python
s = "Humpty;Dumpty;sat;on;the;wall"
wordlist = s.split( ';' )
s = " ".join( wordlist )
print( s )
```

### Practice

In the string
`"How much woot would a wootchuck chuck if a wootchuck could chuck woot."`
the word `"wood"` is misspelled. Use `replace()` to replace all
occurrences of this spelling error with the correct spelling.

Display the contents of the string `"Nobody expects the Spanish`
`Inquisition!# In fact, those who do expect the Spanish Inquisition..."`
up to, but not including, the hash mark (`#`). Use `find()` to get the
index of the hash mark.

Write a program that prints a "cleaned" version of all the words in a
string. Everything that is not a letter should be removed and be
considered a separator. All the letters should be lower case. For
example, the string `"I'm sorry, sir."` should produce four words,
namely `"i"`, `"m"`, `"sorry"`, and `"sir"`. You can use the function
for string cleaning which you wrote as an exercise above.

[^6]: In actuality it will be a bit more convoluted as there might be
    commas in the fields that are stored in the CSV file, so it depends
    a bit on the contents of the file whether this simple approach will
    work. More on CSV files will be said in Chapter
    <a href="#ch:fileformats" data-reference-type="ref" data-reference="ch:fileformats">27</a>.
