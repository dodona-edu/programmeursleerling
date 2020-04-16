The fourteen most common letters in
the English language are: `etaoinshrdlcum`. Write a text compression
program based on this fact. The compression program stores these letters
in half-bytes. A half-byte can take the numbers zero to 15. If you only
use the numbers 1 to 15, each number can represent one of these fourteen
most common letters, and you can use the number 15 for the space. So you
can store two of these letters (or space) in a byte (the value for the
whole byte would be 16 times the value for the first letter, plus the
second letter). If in the text you encounter a letter that is not
amongst these fifteen, you indicate that by storing a zero-half-byte,
followed by a whole byte that represents the unencoded letter. Of
course, in this setup it is possible that the full byte is actually
divided over two bytes, namely the second half-byte of one byte, and the
first half-byte of the other byte.

Hint: an easy approach is to build a list of half-bytes. For the most
common letters, you store their index-value for the string
`"etaoinshrdlcum "` plus 1 (which is a value in the range 1 to 15;
notice that the last character in the string is the space). For the
other characters, you store three half bytes, namely zero, followed by
the ordinal value of the character divided by 16 (rounded down),
followed by that ordinal value modulo 16. Once the half-byte-list is
finished, you can turn it into a byte list by taking pairs of
half-bytes, multiplying the first by 16 and adding the second. Create a
byte string using `bytes()` casting.

For testing: the string `"Hello, world\`"!, which is 13 characters in
length, will become the 11-character byte string
`b'\\x04\\x81\\xbb@,\\xf0wI\\xba\\x02\\x10'` if you follow the procedure
outlined above (which assigns `e` the value 1, `t` the value 2,
etcetera).

A note on the translation of `"Hello, world\`"! to the given byte string
(see Figure
<a href="#f:compression" data-reference-type="ref" data-reference="f:compression">19.1</a>):
You may remember that a hexadecimal representation of a byte consists of
two hexadecimal digits, i.e., each digit is a half-byte. Using that
information, you can see how the translation has been done. The first
byte is `\x04`, i.e., the first half-byte is zero. That means that the
first character is given literally, i.e., it consists of the second
half-byte of `\x04`, and the first half-byte of the next byte, which is
`\x81`. That is the byte `\x48`. If you look up the hexadecimal code 48
in the ASCII table (given in the chapter on strings), you see that that
is the character `H`. The following half-byte is the second half-byte of
`\x81`, i.e., it is 1. Since this is not zero, it is one of the most
common characters, namely the first one, which is `e`. So now you see
how `"Hello, world\`"! is compressed as the byte string provided. The
byte string does contain a few characters that are not displayed as
their hexadecimal code; if you really want to know which hexadecimal
code they represent, look them up in the ASCII table.

By the way, despite the long description, the whole program needs less
than 30 lines of code, including comments, empty lines, and testing
statements.  

![compression](media/compression.png "compression"){:width="65%" data-caption="Compression example."}