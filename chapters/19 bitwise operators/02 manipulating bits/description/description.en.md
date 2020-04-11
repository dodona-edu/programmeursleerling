Python offers a variety of operators that allow the manipulation of data
items at the level of bits. These are the following:

| operator | betekenis |
|:--------:|:----------|
| `<<` | shift left |
| `>>` | shift right |
| `&` | bitwise and |
| `|` | bitwise or |
| `~` | bitwise not |
| `^` | bitwise exclusive or |
{:class="table table-striped table-condensed" style="width:auto;margin-left:auto;margin-right:auto;"}

They are used as follows.

### Shifting bits

When you have a data item, you can use the `<<` and `>>` to shift its
bits to the left or right. `x<<y` shifts the bits of `x` by `y` places
to the left, bringing in zeroes from the right. `x>>y` shifts the bits
of `x` by `y` places to the right, copying the leftmost bit of `x` at
the left while shifting, and losing the bits of `x` at the right. `x`
and `y` must both be numbers.

For example, the exclamation mark `\`! has decimal code 33, which is
written as $00100001$ in binary. Shifting this pattern one place to the
left gives $01000010$, i.e., 66 in decimal, which is the code for the
capital B. You can reverse this by shifting the pattern of B one place
to the right.

```python
code = "!"
print( chr(ord(code)<<1) )
code = "B"
print( chr(ord(code)>>1) )
```

You might have noticed that shifting a number one place to the left
amounts to doubling the number, while shifting it one place to the right
amounts to halving it (while rounding down). Indeed, you can double the
value expressed by a bit pattern by placing a zero to the right of it –
and you can halve it (using integer division) by removing the rightmost
bit.

```python
print( "345 quadrupled makes", 345<<2 )
print( "345 divided by 8 makes", 345>>3 )
```

### Bitwise `and`

The bitwise `and` operator (`&`) takes two bit patterns, and produces a
new pattern that is all zeroes, except for those places where both bit
patterns had a 1, which will then also have a 1 in the output pattern.
For instance, if the input patterns are the number 11 ($00001011$) and
the number 6 ($00000110$), then the bitwise `and` operator produces the
pattern $00000010$, which is the number 2.

```python
print( 11 & 6 )
```

The bitwise `and` is an easy way to take (positive) numbers modulo a
power of 2. For instance, if you want to take a number modulo 16, this
is the same as performing the bitwise `and` on the number with 15, which
is $00001111$. Check that the value of 345 modulo 32 is the same as
taking `345 & 31`.

### Bitwise `or`

The bitwise `or` operator (`|`) takes two bit patterns, and produces a
new pattern that is all ones, except for those places where both bit
patterns had a 0, which will then also have a 0 in the output pattern.
For instance, if the input patterns are the number 11 ($00001011$) and
the number 6 ($00000110$), then the bitwise `or` operator produces the
pattern $00001111$, which is the number 15.

```python
print( 11 | 6 )
```

To set a single bit in a pattern to the value 1 (this is usually called
"setting a bit"), you can use the bitwise `or` and a pattern that
consists of only zeroes, except for a 1 in the spot where you want to
set the bit. An easy way to create a bit pattern with only one bit set,
is to start with the number 1, and use the shift-left operator to shift
that bit to the left as far as you need. Now take a number and set the
bit with index 7 (i.e., the eight bit from the right) to 1.

### Bitwise `not`

The bitwise `not` operator (`\~`) is placed in front of a bit pattern,
and then produces a new pattern that has all the bits of the original
pattern "flipped," i.e., each zero becomes a 1 and each 1 becomes a
zero. For instance, if the input pattern is the number 11 ($00001011$),
then the bitwise `not` produces the pattern $11110100$, which is the
number $-12$. If you wonder why it is $-12$ and not $-11$: this is the
result of the two's complement encoding, which I explained above. Don't
worry too much about it.

```python
print( ~11 )
```

To clear a single bit in a pattern (i.e., setting it to the value zero),
you can use the bitwise `and` and a pattern that consists of only 1s,
except for a zero in the spot where you want to clear the bit. An easy
way to create a bit pattern consisting on only ones, except for a zero
in the intended spot, is to start with the number 1, and use the
shift-left operator to shift that bit to the left as far as you need.
Then invert the pattern with the bitwise `not` operator. Now take a
number and clear the bit with index 3 (i.e., the fourth bit from the
right).

### Bitwise `xor`

The bitwise `exclusive or`, or "`xor`," operator (`^`) takes two bit
patterns, and produces a new pattern that has a zero in all places where
the two bit patterns have the same bit, and a 1 in all places where the
two bit patterns have different bits. For instance, if the input
patterns are the number 11 ($00001011$) and the number 6 ($00000110$),
then the bitwise `xor` operator produces the pattern $00001101$, which
is the number 13.

```python
print( 11 ^ 6 )
```

The bitwise `xor` operator provides an easy way to encrypt numbers. Take
a bit pattern, and call it the "mask." Apply the mask to a number using
the `xor`. This gives a new number, which is the encrypted number.
Somebody who does not know the mask, can't tell what the original number
was. However, someone who does know the mask, can easily get the
original number back, by applying the mask once more. Try this.

### Precedence of bitwise operators

*Warning*: the precedence of bitwise operators is *not* that they are
handled before other operators. Make sure that you use parentheses to
order the operators when you use bitwise operators in a calculation. For
instance, you might think that `1<<1 + 2<<1` is the same as `1*2 + 2*2`,
but in actuality it is evaluated as `(1<<(1+2))<<1`, or `1*8*2`.

```python
print( 1<<1 + 2<<1 )
print( (1<<1) + (2<<1) )
```
