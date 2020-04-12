At this point, I introduce some basic functions that you can use in your
Python programs.

### Type casting

I already introduced the type casting functions, but now I have
explained more details of functions, I can give a complete description.

-   `float()` has one parameter and returns a floating-point
    representation of the value of that parameter. If the parameter
    holds an integer, it returns the same value as a float (if you print
    it, you will see `.0` added). If the parameter holds a float, it
    returns the same value. If the parameter holds a string which can be
    interpreted as an integer or a float, it returns that interpretation
    as a float; otherwise it will give a runtime error.

-   `int()` has one parameter and returns an integer representation of
    the value of that parameter. If the parameter holds an integer, it
    returns the same integer. If the parameter holds a float, it returns
    the integer part of the float, i.e., the float value rounded down.
    If the parameter holds a string, and the string contains only
    digits, optionally with a preceding minus-sign, it returns the
    integer represented by those digits; otherwise it will give a
    runtime error.

-   `str()` has one parameter and returns a string representation of the
    value of that parameter.

What will happen if you run the following code? If you do not know, try
it and find out.

```python
print( 10 * int( "100,000,000" ) )
```

The code above gives a runtime error. Fix it by removing a few
characters.

### Calculations

Basic Python functions also have limited support for calculations.

-   `abs()` has one numerical parameter (an integer or a float). If the
    value is positive, it will return the value. If the value is
    negative, it will return the value multiplied by -1.

-   `max()` has two or more numerical parameters, and returns the
    largest.

-   `min()` has two or more numerical parameters, and returns the
    smallest.

-   `pow()` has two numerical parameters, and returns the first to the
    power of the second. Optionally, it has a third numerical parameter.
    If that third parameter is supplied, it will return the value modulo
    that third parameter.

-   `round()` has a numerical parameter and rounds it, mathematically,
    to a whole number. It has an optional second parameter. The second
    parameter must be an integer, and if it is provided, the function
    will round the first parameter to the number of decimals specified
    by the second parameter.

Examine the code below and try to determine what it displays. Then run
the code and see if you are correct.

```python
x = -2
y = 3
z = 1.27

print( abs( x ) )
print( max( x, y, z ) )
print( min( x, y, z ) )
print( pow( x, y ) )
print( round( z, 1 ) )
```

### `len()`

`len()` is a basic function that gets one parameter, and it returns the
length of that parameter. For now, the only data type which you will use
`len()` for is the string. `len()` returns the length of the string,
i.e., the number of characters.

What does the code below print? Run it and check if you are correct.

```python
print( len( 'can' ) )
print( len( 'cannot' ) )
print( len( "" ) )  # "" is an empty string
```

And what about the code below? Think carefully, then check the result.

```python
print( len( 'can\'t' ) )
```

### `input()`

You will often want the user of a program to supply some data. You can
ask the user to supply a string value by using the `input()` function.
The function has one parameter, which is a string. This string is the
so-called "prompt." When `input()` is called, the prompt is displayed on
the screen and the user gets to enter something. The user may type
anything they want, including nothing, and then press `Enter` to stop
entering input. The return value of the function is a string which
contains what the user entered, excluding that final press of the
`Enter` key.

It depends on the environment in which you use Python how exactly the
user gets asked to enter input. Sometimes a box is displayed in which
you can type something. If you run Python from the command prompt, it is
done as a command line. In different editors, it is done differently;
for instance, there are editors that show a pop-up box.

Here is an example:

```python
text = input( "Please enter some text: " )
print( "You entered:", text )
```

Be aware that `input()` always returns a string. Check the following
code:

```python
number = input( "Please enter a number: " )
print( "Your number squared is", number * number )
```

Regardless of what you entered, this code gives a runtime error, because
since the `input()` function returns a string, number is a string, and
you are not allowed to multiply two strings. You may resolve this by
using a type casting function to turn the string result of `input()`
into a numerical value, for instance:

```python
number = input( "Please enter a number: " )
number = float( number )
print( "Your number squared is", number * number )
```

As long as the user enters a value that can be turned into a number,
this code runs as intended. However, if the user enters something that
cannot be turned into a number, you again get a runtime error. There are
ways to resolve this issue, but I have not discussed the means to do
that yet, and it will take a while before I do that. However, below I
will introduce a way for you to ask the user for numbers without the
code crashing if the user is trying to be a wise-ass and enters
something else.

Write some code that asks the user for two numbers, then shows the
result when you add them, and when you multiply them.

### `print()`

The function `print()` takes zero or more parameters, displays them (if
there are multiple, with a separating space in between each pair of
them), and then "goes to the next line" (i.e., if you use two `print()`
statements, the second one will display its parameters below what the
first one displays).

If `print()` is called without parameters, the function simply will "go
to the next line." This way, you can display empty lines.

You can supply `print()` with anything as a parameter, and it will do
its best to print it. For now, you will only print the basic data types.

`print()` can get two special parameters, called `sep` and `end`.

`sep` indicates what should be printed between each of the parameters,
and by default is a space. You can use `sep` to turn the separating
space into anything else, including an empty string.

`end` indicates what `print()` should put after all the parameters have
been displayed, and by default is a "newline." You can use end to change
what `print()` does after displaying the parameters, for instance, you
can ensure that `print()` does not "go to the next line."

To use `sep` and `end`, you include parameters `sep=<string>` and/or
`end=<string>` (note: when in a code description you see something
between `<` and `>`, that usually means that you are not supposed to type
that literally, but that you have to replace it with something of the
type listed, e.g., `<string>` means that you have to type a string in
that place). For example:

```python
print( "X", "X", "X", sep="x" )
print( "X", end="" )
print( "Y", end="" )
print( "Z" )
```

When you run this code, you see two lines on the output. The first
contains "XxXxX," because the first line of code said that three times
the letter "X" should be displayed, with a lower case "x" as separator
between each pair. The second line contains "XYZ," because even though
there are three `print()` statements which together created this line,
the code says that Python should not go to the next line at the end of
the first two.

### `format()`

`format()` represents a rather complex functionality that is employed in
a particular way. It allows you to create a formatted string, i.e., a
string in which certain values appear in a specific format. To give an
example, suppose I want to display a calculated float:

```python
print( 7/11 )
```

Now I ask you to display that float with only three decimals. Until now,
you would use the `round()` function (introduced above), or something
like:

```python
print( round( 7/11, 3 ) )
```

This works. However, when I put more requirements on it (for instance,
"also reserve 10 positions for it, and left align the outcome in that
reserved space"), it may become convoluted. Using the `format()`
function, you can display the requested value in a much easier and more
readable way:

```python
print( "{:.3f}".format( 7/11 ) )
```

`format()` is a function that "works" on a string. Up until this point,
I have only used functions that get parameters. However, there are
functions that work only on a particular data type, and are defined in
such a way that a variable (or value) of that data type has to be placed
in front of the function call, with a period in between. The reason why
this is, has to do with something called "object orientation," which I
will discuss in Chapters
<a href="#ch:objectorientation" data-reference-type="ref" data-reference="ch:objectorientation">21</a>
to
<a href="#ch:iteratorsandgenerators" data-reference-type="ref" data-reference="ch:iteratorsandgenerators">24</a>.
For now, just know that such functions are called "methods," and to call
them, you have to place the variable (or value) of the right data type
in front of them, with a period in between. The variable (or value) that
is used in this way is also accessible to the method, just like its
parameters are.

So, the `format()` method (let's refer to it by its correct name, it is
not a function but a method) is called as follows: `<string>.format()`.
It will return a new string, which is a formatted version of the string
for which it is called. It can take any number of parameters, and in the
process of formatting, will insert these parameter values in particular
places in the resulting string.

The places where `format()` inserts the parameter values in the string
are indicated in the string by opening and closing curly brackets (`{`
and `}`). If you only use `{}` to refer to the parameters, it will
process the string from left to right, and process the parameters from
left to right, inserting them in the order that they are given. For
example:

```python
print( "The first 3 numbers are {}, {} and {}.".format( 
    "one", "two", "three" ) )
```

If you want to process them in a different order, you can indicate the
order by putting a number between the curly brackets. The first
parameter has number 0, the second has number 1, the third has number 2,
etcetera (if you find numbering starting with zero strange, then know
that this is very common in programming languages and you will see this
many more times). For example:

```python
print( "Backwards they are {2}, {1} and {0}.".format( 
    "one", "two", "three" ) )
```

`format()` can deal with parameters of any type, as long as they have a
suitable string representation. For instance, it can deal with integers
and floats, and you can mix those up with strings as you like:

```python
print( "The first 3 numbers are {}, {} and {}.".format( 
    "one", 2, 3.0 ) )
```

If you want to format the parameters in a more specific way, there are
possibilities to do that, if you put a colon (:) in between the curly
brackets, after the order number if you have one, and place some
formatting instructions to the right of the colon. There are many
possibilities for formatting instructions, and I will introduce only a
few.

First I discuss some formatting instructions for string parameters. If
you want to reserve a certain number of places for a string parameter,
then you can indicate that with an integer to the right side of the
colon. This is called the "precision." The following code uses a
precision of 7.

```python
print( "The first 3 numbers are {:7}, {:7} and {:7}.".format( 
    "one", "two", "three" ) )
```

If you do not reserve sufficient space for a parameter with the
precision, `format()` will take as much space as it needs. So you cannot
use the precision to, for instance, break off a string prematurely.

```python
print( "The first 3 numbers are {:4}, {:4} and {:4}.".format( 
    "one", "two", "three" ) )
```

If you use precision, you can align the parameter to the left, center,
or right. You do that by placing an alignment character between the
colon and the precision. Alignment characters are `<` for align left,
`^` for align center, and `>` for align right.

```python
print( "The first 3 numbers are {:>7}, {:^7} and {:<7}.".format( 
    "one", "two", "three" ) )
```

Now I will discuss some number formatting instructions. If you want a
number to be interpreted as an integer, you place a "d" to the right
side of the colon. If instead you want it to be interpreted as a float,
you place an "f." If you want to display an integer as a float,
`format()` will do the necessary conversions for you. If you want to
display a float as an integer, `format()` will cause a runtime error.

```python
print( "{} divided by {} is {}".format( 1, 2, 1/2 ) )
print( "{:d} divided by {:d} is {:f}".format( 1, 2, 1/2 ) )
print( "{:f} divided by {:f} is {:f}".format( 1, 2, 1/2 ) )
```

Just as with strings, you can use precision and alignment with numbers.
You use the same instruction characters, and place them between the
colon and the `d` or `f`. And just as with strings, if the precision
does not provide enough places, `format()` will take extra places as
needed. Note that a preceding minus-sign and the decimal period each
also take a place.

```python
print( "{:5d} divided by {:5d} is {:5f}".format( 1, 2, 1/2 ) )
print( "{:<5f} divided by {:^5f} is {:>5f}".format( 1, 2, 1/2 ) )
```

Finally, and perhaps most useful, you can indicate how many decimals you
want a floating point number to be displayed with, by placing a period
and an integer to the left of the `f`. `format()` will round the
parameter to the requested number of decimals. Note that you can
indicate zero decimals using `.0`, which will display floats as
integers.

```python
print( "{:.2f} divided by {:.2f} is {:.2f}".format( 1, 2, 1/2 ) )
```

The combination of precision, alignment, and decimals, allows you to
create nice, table-like displays.

```python
s = "{:>5d} times {:>5.2f} is {:>5.2f}"
print( s.format( 1, 3.75, 1 * 3.75 ) )
print( s.format( 2, 3.75, 2 * 3.75 ) )
print( s.format( 3, 3.75, 3 * 3.75 ) )
print( s.format( 4, 3.75, 4 * 3.75 ) )
print( s.format( 5, 3.75, 5 * 3.75 ) )
```
