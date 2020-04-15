`"\n"` is a so-called "escape sequence." An escape sequence is a string
character written as a backslash followed by a code, which can be one or
multiple characters. Python interprets escape sequences in a string as a
special character.

Besides the newline character `"\n"`, in Chapter
<a href="#ch:expressions" data-reference-type="ref" data-reference="ch:expressions">4</a>
I also introduced the special characters `"\'"` and `"\""`, which can be
used to place a single respectively double quote in a string, regardless
of what characters surround the string. I also mentioned that you can
use `"\\"` to insert a "real" backslash in a string.

Besides these, there are a few more escape sequences which lead to a
special character. Most of these are archaic and you do not need to
worry about them. The two I want to mention are `"\t"` which represents
a single tabulation, and `"\xnn"` whereby `nn` stands for two
hexadecimal digits, which represents the character with hexadecimal
number `nn`. For example, `"\x20"` is the character expressed by the
hexadecimal number 20, which is the same as the decimal number 32, which
is the space (this will be explained later in this chapter).

In case you never learned about hexadecimal counting: hexadecimals use a
numbering scheme that uses 16 different digits, namely 0 to 9, and A to
F. A direct translation from hexadecimals to decimals turns A into 10, B
into 11, etcetera. In decimal counting, the value of a multi-digit
number is found by multiplying the digits by increasing powers of 10,
from right to left, e.g. `1426` is

$$\begin{align} 1426 &= 1 \times 10^3 + 4 \times 10^2 + 2 \times 10^1 + 6 \times 10^0 \\ &= 1 \times 1000 + 4 \times 100 + 2 \times 10 + 6 \times 1 \end{align}$$

For hexadecimal numbers you do the same
thing, but multiply by powers of 16, e.g., the hexadecimal number `4AF2` is

$$\begin{align} \text{4AF2} &= 4 \times 16^3 + 10 \times 16^2 + 15 \times 16^1 + 2 \times 16^0 \\ &= 4 \times 4096 + 10 \times 256 + 15 \times 16 + 2 \times 1 \end{align}$$

Programmers tend to like hexadecimal
numbers, as computers work with bytes as the smallest unit of memory
storage, and a byte can store 256 different values, i.e., any byte value
can be expressed by a hexadecimal number of two digits.

Why it is useful to know about hexadecimal counting and hexadecimal
representation of characters follows later in the book.
