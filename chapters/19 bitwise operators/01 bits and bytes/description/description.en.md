A bit is the smallest size data unit that a computer can handle. A
single bit can have only two different values, namely 1 and zero.

While "prehistoric" computers were indeed programmed by directly dealing
with single ones and zeroes, very quickly computers were introduced that
handled groups of bits. The smallest unit in that respect is the "byte,"
which consists of 8 bits. Today, the concept of a byte still permeates
most computer languages, even though computers have been enhanced to use
larger collections of bytes as smallest data units (notably, most
computers today either deal with 32-bits or 64-bits data units).

### Binary counting

A byte consists of 8 bits, which you can display as a sequence of ones
and zeroes, e.g., `11010010`. As such, a byte can be used to represent a
number in binary code. If a byte is used to represent a positive number,
that number can be calculated by multiplying the right-most bit by 1,
the bit next to that by 2, the bit next to that by 4, etcetera, and
adding up all those values. For instance, the sequence `11010010` is
`1*128+1*64+0*32+1*16+0*8+0*4+1*2+0*1`, which is 210. Note that this is
similar to calculating the value of decimal numbers, where the rightmost
digit is multiplied by 1, the digit next to that by 10, the digit next
to that by 100, etcetera, and adding up all those resulting values. It
is also similar to hexadecimal counting, which was discussed in Chapter
11.

When bits are numbered, by convention numbering starts at zero at the
rightmost end, and numbers are increased when counting to the left,
i.e., the rightmost bit has number 0, the bit next to that has number 1,
the bit next to that has number 2, etcetera. The reason is that the
rightmost bit represents the value $$2^0$$ (which, in case you forgot,
equals 1), the bit next to it the value $$2^1$$, the bit next to that
$$2^2$$, etcetera.

|                   |       |          |        |          |        |        |          |        |       |
|:------------------|------:|---------:|-------:|---------:|-------:|-------:|---------:|-------:|:------|
| Byte              |      1|         1|       0|         1|       0|       0|         1|       0|       |
| Number of bit     |      7|         6|       5|         4|       3|       2|         1|       0|       |
| Represented value |  $$2^7$$|     $$2^6$$|   $$2^5$$|     $$2^4$$|   $$2^3$$|   $$2^2$$|     $$2^1$$|   $$2^0$$|       |
| Byte value        |  $$2^7$$|  \+ $$2^6$$|  \+ $$0$$|  \+ $$2^4$$|  \+ $$0$$|  \+ $$0$$|  \+ $$2^1$$|  \+ $$0$$| = 210 |
{:class="table table-striped table-condensed" style="width:auto;margin-left:auto;margin-right:auto;"}

Write some code that calculates the decimal number represented by a
binary string of 8 ones and zeroes. The nicest solution uses a loop, a
multiplier, and a total. The total starts at 0. The multiplier (which is
the represented value in the example above) starts at 1, and every time
the loop is traversed it is multiplied by 2. The loop processes the
string from right to left (or the reversed string from left to right),
and if the character encountered is a "1," it adds the multiplier to a
total. This will end up with the number represented by the string as the
total.

The lowest number that can be expressed by a byte is $$00000000$$, which
equals zero. The highest is $$11111111$$, which equals 255. Thus, there
are 256 different values that can be expressed by one byte.

### Character encoding

The most basic character encoding mechanism is ASCII. The ASCII table
was shown in Chapter
11,
including hexadecimal codes. You may have noticed that the codes used
ran from (hexadecimal) 20 to 7E. The codes below 20 are used for special
sequences (such as the newline character). The code 7F usually represent
the `Del` key. No other codes are in use, which means that all ASCII
characters can be represented by 7 bits, or the 8-bit sequences
$$00000000$$ to $$01111111$$.

While computers use bytes as basic data unit, the ASCII character set
does not use 128 of all the values that can be stored in a byte. All
these unused bytes have a 1 as their leftmost bit. Naturally, some
character encodings were introduced that assign a character to all 256
different values that a byte can take. A typical one is `latin-1`, which
is discussed in Chapter
17.
Unfortunately, not all encoding mechanisms assign the same characters to
the numbers between 128 and 255. However, all encoding mechanisms in use
today at least have the basic ASCII characters for the values 0 to 127.

Python is based on Unicode encoding. Specifically, it uses UTF-8 as
character encoding mechanism (discussed in Chapters
11
and
17).
UTF-8 encoding works as follows:

-   A byte that has a zero as leftmost bit is an ASCII character.

-   A byte that has a 1 as leftmost bit is the start of a sequence of
    multiple bytes that represent one character. The sequence consists
    of a leading byte (the leftmost byte) and one or more continuation
    bytes.

-   For a multibyte sequence, the leading byte has, from left to right,
    several bits with value 1, followed by a bit with value zero,
    followed by the remaining bits. The length of the total multibyte
    sequence is as many bytes as there are bits with value 1 to the left
    of the leftmost zero. E.g., if the leading byte has value $$1110xxxx$$
    (where each $$x$$ is some bit value), the whole sequence is three
    bytes long. This includes the leading byte. The minimum sequence
    length is two bytes, and the maximum sequence length is six bytes
    (the leading byte will then be $$1111110x$$).

-   Each continuation byte has 10 as the two leftmost bits.

-   In practice, UTF-8 encoding is restricted to at most 4-byte
    sequences, and some of the 4-byte sequences have been excluded.

This means that UTF-8 can express a great many different characters.
However, it also means that, due to the way characters are encoded, some
bit patterns do not express UTF-8 characters. While any bit pattern
expresses a legal string with `latin-1` encoding, it is possible to
construct a bit pattern that does not express a legal UTF-8 encoding.
This may cause those annoying `UnicodeDecodeError`s when reading files.

### Number encoding

The way that numbers are encoded as bit patterns is somewhat tricky, and
in general you do not need to bother with it. You should know that
positive integers are always encoded as multi-byte patterns, that have a
zero as their leftmost bit. The rest of the pattern is like you would
expect, and as explained above.

Negative numbers, however, are encoded rather differently. They use the
so-called "two's complement" system. When a negative number is encoded,
first the absolute value of that number (i.e., the positive version) is
taken. From this number, all the bits are "flipped," i.e., every 1
becomes a zero and every zero becomes a 1. Finally, 1 is numerically
added to the result. The bit pattern of a negative number therefore
always has a 1 as its leftmost bit.

For example, to encode $$-1$$, first the bit pattern of 1 is taken, which
is …$$00000001$$. All the bits are flipped, which gives …$$11111110$$.
Finally, 1 is added the the result, which gives …$$11111111$$. Thus,
$$-1$$ is encoded as a sequence of only $$1$$s.

As for floating point numbers, these use scientific notation, whereby
part of the multi-byte pattern is used as exponent.

The reason that I am explaining all of this, is to indicate that if you
want to handle bit patterns in a Python program, and you want to treat
these patterns as numbers, you best work only with positive integers, as
the bit patterns of those are easily understood.
