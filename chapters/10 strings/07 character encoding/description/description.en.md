All systems use a particular way of encoding characters. The basic
encoding that (almost) every system supports is the standard ASCII code.
This is a 7-bits code, which can represent 128 different characters.
Several of these (in particular those with the lowest-numbered
encodings) are control characters that have a special function. Most of
these special functions are only useful for archaic computer systems,
but the tabulation, newline, and backspace characters are found amongst
them. If you only use characters on a standard US keyboard, you are
limited to ASCII characters.

Nowadays, many systems use Unicode. Unicode supports far more
characters. There are different formats for storing characters in
Unicode. The best-known is UTF-8, which uses one byte for each of the
ASCII characters, but multiple bytes for all the other characters (a
byte is a group of 8 bits, whereby each bit contains either a 1 or a
zero). Other Unicode encodings use multiple bytes to store any
character. Python, be default, works with UTF-8, which means that it
also supports regular ASCII encodings.

### ASCII

Below I display the ASCII table. The only characters I have left off are
those which are control sequences. These have the numbers zero to 31,
and 127. 32 is the space. I also display the hexadecimal code for each
character next to the decimal code. (If you wonder why I even bother
listing those hexadecimal codes: they become relevant in a later
chapter.)

As you can see, each character has a number attached to it. To find out
what a character's number is in a program, you can use the `ord()`
function. For instance, `ord("A")` returns the number of `"A"`, which,
as you can see, is 65. The counterpart of the `ord()` function is the
`chr()` function. `chr()` gets a number as argument, and returns the
character that belongs to that number. For instance, `chr(65)` is the
letter `"A"`.

    DC HX      DC HX      DC HX      DC HX      DC HX      DC HX
    32 20      48 30 0    64 40 @    80 50 P    96 60 `   112 70 p
    33 21 !    49 31 1    65 41 A    81 51 Q    97 61 a   113 71 q
    34 22 "    50 32 2    66 42 B    82 52 R    98 62 b   114 72 r
    35 23 #    51 33 3    67 43 C    83 53 S    99 63 c   115 73 s
    36 24 $    52 34 4    68 44 D    84 54 T   100 64 d   116 74 t
    37 25 %    53 35 5    69 45 E    85 55 U   101 65 e   117 75 u
    38 26 &    54 36 6    70 46 F    86 56 V   102 66 f   118 76 v
    39 27 '    55 37 7    71 47 G    87 57 W   103 67 g   119 77 w
    40 28 (    56 38 8    72 48 H    88 58 X   104 68 h   120 78 x
    41 29 )    57 39 9    73 49 I    89 59 Y   105 69 i   121 79 y
    42 2A *    58 3A :    74 4A J    90 5A Z   106 6A j   122 7A z
    43 2B +    59 3B ;    75 4B K    91 5B [   107 6B k   123 7B {
    44 2C ,    60 3C <    76 4C L    92 5C \   108 6C l   124 7C |
    45 2D -    61 3D =    77 4D M    93 5D ]   109 6D m   125 7D }
    46 2E .    62 3E >    78 4E N    94 5E ^   110 6E n   126 7E ~
    47 2F /    63 3F ?    79 4F O    95 5F _   111 6F o

A comparison of strings which use only these characters use the numbers
of the characters to determine which string is "smaller." For instance,
the string `"orange"` is smaller than the string `"ordinal"`, because
the first character that differs between them is the third one, which is
`"a"` for `"orange"` and `"d"` for `"ordinal"`, and since the number for
`"a"` is lower than the number for `"d"`, the string `"orange"` is
considered to be smaller than the string `"ordinal"`. This is,
basically, an alphabetic comparison. If characters occur in a string
that are not letters, you can check in the ASCII table which is
considered lower. Notice how all the digits are lower than letters.

```python
print( ord( 'A' ) )
print( ord( 'a' ) )
print( chr( 65 ) )
print( chr( 97 ) )
print( "orange" < "ordinal" )
```

You can use these numbers that are associated with characters to do all
kinds of neat calculations. For instance, if I want to know which the
twelfth letter after `"g"` is, I can calculate that as follows:

```python
print( "The 12th letter after g is", chr( ord( "g" )+12 ) )
```

For another example of what you can do with character codes, here is a
program that generates the ASCII table as a matrix:

```python
print( ' ', end='' )
for i in range(16):
    if i < 10:
        print( ' '+chr( ord( '0' )+i ), end='' )
    else:
        print( ' '+chr( ord( 'A' )+i-10 ), end='' )
print()
for i in range( 2, 8 ):
    print( i, end='' )
    for j in range( 16 ):
        c = i*16+j
        print( ' '+chr( c ), end='' )
    print()
```

Note that I highly prefer you using the `ord()` and `chr()` functions if
you want to juggle character encoding. If you want to refer to the
character code of the letter `"A"`, do not write 65, but write
`ord("A")` instead. 65 is only meaningful to people who know ASCII
encodings, and your programs should be meaningful to anybody. Moreover,
while ASCII is a widely-used standard, there are still computers out
there which use different encoding mechanisms, in which the code for
`"A"` is not necessarily 65 (I am looking at you, IBM).

### UTF-8

Python supports Unicode, in particular the most common Unicode encoding
scheme UTF-8. This means that you can use all kinds of "weird"
characters. I explained that in the naming of functions and variables
you can use "letters," which you probably assumed meant `"A"` to `"Z"`
and `"a"` to `"z"`. The funny thing is that it depends on the language
codes of your computer what is considered a letter. For instance, if
your computer tells Python that the language is German, then you can
also use characters with umlauts. I strongly discourage using such
letters in variable and function names, by the way. Not only are they
hard to type, but they also make your program less portable.

In UTF-8, the regular characters which you find on a keyboard are
represented in strings exactly as you would expect. However, "special"
characters can be incorporated too, but look quite different. Since
Python supports UTF-8, you have to be careful when you copy texts from,
for instance, a word processor document. Word processors have the
disturbing habit of changing characters into other characters, like
turning straight quotes into round quotes. If you copy such round quotes
into your program, Python will accept the characters, but will not
interpret them as, for instance, string boundaries.

If you want to display Unicode characters, you can do so by using
Unicode encodings. You have to know the UTF-8 number of the character
that you want to display. If you know that, you can use a code
`\uxxxx`, where `xxxx` is a hexadecimal number, to incorporate a
Unicode character in a string. For example, the code below displays the
capitals of the Greek alphabet:[^7]

```python
alpha = "\u0391"
for i in range( 25 ):
    print( chr( ord( alpha )+i ), end=" " )
```

In general, you will not need to worry too much about character
encodings. I recommend that you restrict yourself to ASCII whenever
possible. In cases where you have to deal with Unicode characters,
things usually work correctly automatically, since the standard Python
functionalities support Unicode. Occasionally I have run into
translation problems from Unicode to ASCII, in particular where files
were concerned. It will be a while before you run into problems like
that, and I will bring it up again in Chapter
<a href="#ch:textfiles" data-reference-type="ref" data-reference="ch:textfiles">17</a>
and later.

[^7]: There is one weird character in this display, between the Rho and
    the Sigma, which is `\u03A2`, which is evidently not a legal Unicode
    character.
