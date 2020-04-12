Python offers some basic functions, some of which are introduced above.
Besides those, Python offers a large assortment of so-called "modules,"
which contain many more useful functions. To use functions from a module
in your program, you have to import the module, by writing a line
`import <modulename>` at the top of your code. You can then use all the
functions in the module, though you have to precede the function calls
with the name of the module and a period, e.g., to call the `sqrt()`
function from the `math` module (which calculates the square root of a
number), you call `math.sqrt()` after importing `math`.

Alternatively, you can import only specific functions from a module, by
stating:

```python
from <modulename> import <function1>, <function2>, <function3>, …
```
  
The main advantage of importing specific functions from a module in this
way is that in your code, you no longer need to precede the call to a
function with the module name.

For example:

```python
import math

print( math.sqrt( 4 ) )
```

is equivalent to:

```python
from math import sqrt

print( sqrt( 4 ) )
```

If you want to rename something that you import from a module, you can
do so with the keyword `as`. This might be useful when you use multiple
modules that contain things with equal names.

```python
from math import sqrt as squareroot

print( squareroot( 4 ) )
```

I will now introduce some functions from two standard modules that are
often used, and some functions from a module which was developed for
this book (you will learn to develop your own modules later). There are
many more modules besides the ones introduced here, some of which will
come up later in the book, and others which you will have to look up by
yourself by the time you need them in practice. However, you may assume
that for any more-or-less general problem that you want to solve,
someone has made a module that makes solving that problem simple or even
trivial. So, in practice, do not start coding immediately, but first
investigate whether you can exploit someone else's efforts.

### `math`

The `math` module contains some useful mathematical functions. These
functions have usually been implemented in a very efficient way, and in
general they return a float. I will introduce only a few of these
functions here (if you want to learn more of them, look up the `math`
module in the Python reference):

-   `exp()` gets one numerical parameter and returns $$e$$ to the power of
    that parameter. If you do not remember $$e$$ from math class: $$e$$ is a
    special value that has many interesting properties, which have
    applications in physics, maths, and statistics.

-   `log()` gets one numerical parameter and returns the natural
    logarithm of that parameter. The natural logarithm is the value
    which, when e is raised to the power of that value, gives the
    requested parameter. Just like $$e$$, the natural logarithm has many
    applications in physics, maths, and statistics.

-   `log10()` gets one numerical parameter and returns the base-10
    logarithm of that parameter.

-   `sqrt()` gets one numerical parameter and returns the square root of
    that parameter.

For example:

```python
from math import exp, log

print( "The value of e is approximately", exp( 1 ) )
e_sqr = exp( 2 )
print( "e squared is", e_sqr )
print( "which means that log(", e_sqr, ") is", log( e_sqr ) )
```

### `random`

The `random` module contains functions that return pseudo-random
numbers. I say "pseudo-random" and not "random," because it is
impossible for digital computers to generate actual random numbers.
However, for all intents and purposes you may assume that the functions
in the `random` module cough up random values.

-   `random()` gets no parameters, and returns a random float in the
    range $$[0,1)$$, i.e., a range that includes 0.0, but excludes 1.0.

-   `randint()` gets two parameters, both integers, and the first should
    be smaller than or equal to the second. It returns a random integer
    in the range for which the two parameters are boundaries, e.g.,
    `randint(2,5)` returns 2, 3, 4, or 5, with an equal chance for each
    of them.

-   `seed()` initializes the random number generator of Python. If you
    want a sequence of random numbers that are always the same, start by
    calling `seed()` with a fixed value as parameter, for instance, 0.
    This can be useful for testing purposes. If you want to
    re-initialize the random number generator so that it starts behaving
    completely randomly again, call `seed()` without parameter.

For example:

```python
from random import random, randint, seed

seed()
print( "A random number between 1 and 10 is", randint( 1, 10 ) )
print( "Another is", randint( 1, 10 ) )
seed( 0 )
print( "3 random numbers are:", random(), random(), random() )
seed( 0 )
print( "The same 3 numbers are:", random(), random(), random() )
```

### `pcinput`

`pcinput` is a module I wrote for this book. You can find it in Appendix
<a href="#ch:pcinput" data-reference-type="ref" data-reference="ch:pcinput">31</a>,
and can easily recreate it (or simply download it from
<http://www.spronck.net/pythonbook>{:target="_blank"}). It contains four functions which
are helpful for getting particular kinds of input from the user in a
safe way. The functions are the following:

-   `getInteger()` gets one string parameter, the prompt, and asks the
    user to supply an integer using that prompt. If the user enters
    something that is not an integer, the user is asked to enter a new
    input. The function will continue asking the user for inputs until a
    legal integer is entered, and then it will return that value, as an
    integer.

-   `getFloat()` gets one string parameter, the prompt, and asks the
    user to supply a float using that prompt. If the user enters
    something that is not a float or an integer, the user is asked to
    enter a new input. The function will continue asking the user for
    inputs until a legal float or integer is entered, and then it will
    return that value, as a float.

-   `getString()` gets one string parameter, the prompt, and asks the
    user to supply a string using that prompt. Any value that the user
    enters is accepted. The function will return the string that was
    entered, with leading and trailing spaces removed.

-   `getLetter()` gets one string parameter, the prompt, and asks the
    user to supply a letter using that prompt. The user's input must be
    a single letter, in the range A to Z. Both capitals and lower case
    letters are accepted. The function returns the letter entered,
    converted to a capital.

These functions allow you to write code that asks the user for inputs of
a specific data type, and guarantee that the input will indeed be of
that data type, i.e., the code does not crash if the user enters
something that is unacceptable. The functions are not very nicely
designed, as they display messages in English when the user enters
something that is wrong (so the functions are less useful if your code
is meant to support a different language). But for the purpose of
learning Python, they work fine.

Create or download the `pcinput` module, make sure that it is located in
the folder where you write your Python code, then create a file with the
code below in it. Run it, try to enter something else than an integer,
and see what happens.

```python
from pcinput import getInteger

num1 = getInteger( "Please enter an integer: " )
num2 = getInteger( "Please enter another integer: " )

print( "The sum of", num1, "and", num2, "is", num1 + num2 )
```

Ask the user to supply a string. Then use that string as a prompt to ask
for a float.

{:class="callout callout-info"}
> #### Note
> I do not explain here how the functions of `pcinput` work, as they are implemented using concepts that are discussed much later in the book. You will learn, in time, how to develop such functions yourself. For now, do not worry about how they work, but just use them. This is the attitude that you should have towards most standard functions: as long as you know what they do, which parameters they need, and what they return, you do not need to spend time considering how they work.
