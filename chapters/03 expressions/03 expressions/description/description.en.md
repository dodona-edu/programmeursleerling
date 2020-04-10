Finally, I can get to the topic of this chapter, which is "expressions."
An expression is a combination of one or more values (such as strings,
integers, or floats) using operators, which result in a new value. In
other words, you can think of expressions as calculations.

### Basic calculations

Basic calculations combine two values with one operator in between them.
Some straightforward operators are:

| operator | description |
|:--------:|:------------|
| `+` | addition |
| `-` | subtraction |
| `*` | multiplication |
| `/` | division |
| `//` | integer division |
| `**` | power |
| `%` | modulo |
{:class="table table-striped table-condensed" style="width:auto;margin-left:auto;margin-right:auto;"}

Here are some examples:

```python
print( 15+4 )
print( 15-4 )
print( 15*4 )
print( 15/4 )
print( 15//4 )
print( 15**4 )
print( 15%4 )
```

I assume you know what each of these operators entails, except perhaps
the integer division and modulo operators.

The integer division (also called "floor division") is simply a division
that rounds down to a whole number. If you involve floats in the
calculation, the result will still be a float, but rounded down. If you
only involve integers in the calculation, the result will be an integer.

The modulo operator (%) takes the remainder of a division. For example:
If I divide 14 by 5, the result is 2.8, right? This means I can subtract
5 twice from 14, and still have a positive result, but if I subtract it
a third time, the result will become negative. So, after subtracting 5
twice from 14 I have a remainder that is less than 5. This remainder is
what the modulo operator produces.

In very simplistic terms: if I have 14 cookies which I have to divide
over 5 children, each child gets 2 cookies. And I still have 4 cookies
left, because there are more children than I have cookies at that point.
Thus, dividing 14 by 5 as an integer division is 2 (cookies per child),
while 14 modulo 5 is the remainder 4 (cookies I have left in my hand).

On a side note, I wish to point out that the code shown above consists
of multiple lines. Each line is said to be a "statement," and it
consists of one command that Python executes (in the code above, a
`print()` function on every line). Most programming languages make it
mandatory to end each statement with a special character, usually a
semi-colon ($$;$$). Python does not require a semi-colon after each
statement, but each statement must (in general) be on its own line. In
principle, you are allowed to place multiple Python statements on one
line, but then you should put semi-colons between the statements.
However, it is Python practice and convention not to do that, as it
makes code ugly, hard to read, and difficult to maintain. So, please
stick to the convention and give each statement its own line.

### More complex calculations

You are allowed to combine operators into bigger calculations, just as
you can do on the more advanced calculators. To help you out, you are
also allowed to used parentheses in your calculations, and you can even
nest these parentheses. Python will process the operators in the order
prescribed by mathematicians, often referred to as PEMDAS (Parentheses,
Exponents, Multiplication and Division, Addition and Subtraction).

Check out the calculation below, and try to predict what it will result
in before you copy it to the Python shell and run the code.

```python
print( 5*2-3+4/2 )
```

There are a couple of things to note about this calculation.

First, the end result is a float (even though it has no decimals, or, if
you will, only zero as a decimal). The reason is that a division is part
of the calculation, and for Python that means that it should turn this
into a floating-point calculation.

Second, just as explained above, spaces are ignored by Python, so the
code above is the same as:

```python
print( 5 * 2 - 3 + 4 / 2 )
```

It is even the same as:

```python
print( 5*2 - 3+4    / 2 )
```

I have been in long discussions with people who keep arguing that the
code above should result in $$6.5$$ or $$1.5$$, because *clearly* you have
to calculate the $$5*2$$ and the $$3+4$$ before you do the subtraction and
division. That is hogwash. It does not matter how close you place
operands together, spaces are ignored. If you really want to calculate
the $$3+4$$ first, you have to put it between parentheses. You can then
still use spaces to improve readability, but they mean nothing to
Python.

```python
print( (5*2) - (3+4)/2 )
print( ((5*2)-(3+4)) / 2 )
```

Now it is time to write your first program. Write a program that
displays the number of seconds in a week. You should, of course, not
grab your calculator or smartphone to do the calculation and then just
print the resulting number, but you should do the calculation in Python
code. Since this program needs only one line of code, you could just
write it in the Python shell, though you are encouraged to create a
program file and use that.

### String expressions

Some of the operators given above can also be used for strings, though
not all of them.

In particular, you can use the addition operator ($$+$$) to concatenate
two strings, and you can use the multiplication operator ($$*$$) with a
number and a string to create a string that contains a repetition of the
original string. Check it out:

```python
print( "hello"+"world" )
print( 3*"hello" )
print( "goodbye"*3 )
```

You cannot add a number to a string, or multiply two strings. Such use
of the operators is undefined, and will give error messages. None of the
other operators listed for numbers will work on strings either.

### Type casting

Sometimes you need to change the data type of a value into a different
data type. You can do that using type casting functions.

I will discuss functions in a lot more detail in a later chapter, but
for now you just need to know that a function has a name, and may have
parameters (values) between parentheses after the name. It will do
something with the parameters, and then may give back a result. For
instance, the `print()` function displays the parameter values that are
given to it between the parentheses, and gives nothing in return.

The type casting functions take the parameter value between the
parentheses and give back a value that is the (almost) the same as the
parameter value, but of a different data type. The three main type
casting functions are the following:

-   `int()` will return the value between the parentheses as an integer
    (rounding down if necessary)

-   `float()` will return the value between the parentheses as a float
    (adding .0 if necessary)

-   `str()` will return the value between the parentheses as a string

See the difference between the following two lines of code:

```python
print( 15/4 )
print( int( 15/4 ) )
```

Or the following two lines of code:

```python
print( 15+4 )
print( float( 15+4 ) )
```

I stated that you cannot use the addition operator to concatenate a
number to a string. However, if you need to do something like that, you
can work around the issue by using string type casting:

```python
print( "I own " + str( 15 ) + " apples." )
```
