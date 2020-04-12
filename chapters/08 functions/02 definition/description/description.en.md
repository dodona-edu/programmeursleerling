Chapter
<a href="#ch:simplefunctions" data-reference-type="ref" data-reference="ch:simplefunctions">6</a>
described how each function has a name, may have some parameters, and
may have a return value. When you create your own functions, you need to
define each of these. To create a function, you use the following
syntax:

```python
def <function_name>( <parameter_list> ):
    <statements>
```

The function name must meet the same requirements that variable names
must meet, i.e., only letters, digits, and underscores, and it cannot
start with a digit. The parameter list consists of zero or more variable
names, with commas in between. The code block below the function
definition must be indented.

Finally, be aware that Python must have "seen" your function definition
before it sees the call to it in your code. Therefore it is convention
to place all function definitions at the top of a program, right under
the `import` statements.

### How Python deals with functions

To be able to create functions, you have to know how Python deals with
functions. Look at the small Python program below. It defines one
function, called `goodbyeWorld()`. That function has no parameters. The
code block for the function prints the line "Goodbye, world!"

The rest of the program is not part of a function. We often call the
parts of a program that are not inside a function the "main" program.
The main program prints the line "Hello, world!," and then calls the
function `goodbyeWorld()`.

```python
def goodbyeWorld():
    print( "Goodbye, world!" )

print( "Hello, world!" )
goodbyeWorld()
```

When you run this program, you see that it first prints "Hello, world!,"
and then "Goodbye, world!" This happens even though Python processes
code top-down, so that it sees the line `print( "Goodbye, world!" )`
before it sees the line `print( "Hello, world!" )`. This is because
Python does not actually run the code inside functions, at least, not
until the moment that the function gets called. Python does not even
look at the code in functions. It just notices the function name,
registers that the function is defined so that it can be used, and then
continues, searching for the main program to run.

### Parameters and arguments

Examine the code below. It defines a function `hello()` with one
parameter, which is called `name`. The function uses the variable `name`
in the code block. There is no explicit assignment of the variable name,
it exists because it is a parameter of the function.

When a function is called, you must provide a value for every
(mandatory) parameter that is defined for the function. Such a value is
called an "argument." Therefore, to call the function `hello()`, you
must provide an argument for the parameter `name`. You place this
argument between the parentheses of the function call. Note that in your
main program you do not need to know that this parameter is called
`name`. What it is called is unimportant. The only thing you need to
know is that there is a parameter that needs a value, and preferably
what kind of value the function is expecting (i.e., what the author of
the function expects you to provide).

```python
def hello( name ):
    print( "Hello, {}!".format( name ) )

hello( "Adrian" )
hello( "Binky" )
hello( "Caroline" )
hello( "Dante" )
```

The parameters of a function are no more and no less than variables that
you can use in the function, and that get their value from outside the
function (namely by a function call). The parameters are "local" to the
function, i.e., they are not accessible outside the code block of the
function, nor do they influence any variable values outside the
function. More on that later.

Functions can have multiple parameters. For example, the following
function multiplies two parameters and prints the result:

```python
def multiply( x, y ):
    result = x * y
    print( result )

multiply( 2020, 5278238 )
multiply( 2, 3 )
```

### Parameter types

In many programming languages, you specify what the data types of the
parameters of the functions that you create are. This allows the
language to check whether calls to the functions are made with correct
arguments. In Python, you do not specify data types. This means that,
for example, the `multiply()` function in the code block above can be
called with string arguments. If you do so, you will generate a runtime
error (as you cannot multiply two strings).

If you want to write a "safe" function, you can check the type of
arguments that the function is provided with, using the `isinstance()`
function. `isinstance()` gets a value or a variable as first parameter,
and a type as second parameter. It returns `True` if the value or
variable is of the specified type, and `False` otherwise. For example:

```python
a = "Hello"
if isinstance( a, int ):
    print( "integer" )
elif isinstance( a, float ):
    print( "float" )
elif isinstance( a, str ):
    print( "string" )
else:
    print( "other" )
```

Of course, should you decide to do such type checking in a function, you
must decide what you will do if the user provides the wrong type. The
regular way to handle this is by "raising an exception." This will be
discussed in Chapter
<a href="#ch:exceptions" data-reference-type="ref" data-reference="ch:exceptions">18</a>.
For now, you may assume that the functions that you write are called
with parameters of the correct types. As long as you write functions for
your own use, you can always guarantee that.

### Default parameter values

It is possible to provide default values for some of the parameters. You
do this by placing an assignment operator and value next to the
parameter name, as if it is a regular assignment. When calling the
function, you can specify all parameters, or just some of them. In
principle the values get passed to the function’s parameters from left
to right; if you pass fewer values than there are parameters, as long as
default values for the remaining parameters are given, the function call
gets executed without runtime errors.

If you define a function with default values for some of the parameters,
but not all, it is common to place the ones for which you give a default
value to the right of the ones for which you do not.

If you want to override the default value for a specific parameter, and
you know its name but not its place in the order of the parameters, or
you simply want to leave the other parameters at their default value,
you can actually in the function call give a value to a *specific*
parameter by name, using an assignment between the parentheses, i.e.,
`<function>( <parametername>=<value> )`.

The following code gives examples of these possibilities:

```python
def multiply_xyz( x, y=1, z=7 ):
    print( x * y * z )
    
multiply_xyz( 2, 2, 2 ) # x=2, y=2, z=2
multiply_xyz( 2, 5 )    # x=2, y=5, z=7
multiply_xyz( 2, z=5 )  # x=2, y=1, z=5
```

### `return`

Parameters can be used to communicate information from outside a
function to the code block of the function. Often, you also want a
function to communicate information to the rest of the program outside
the function. The keyword `return` accomplishes this.

When you use the command `return` in a function, that ends the
processing of the function, and Python will continue with the code that
comes after the call to the function. You can put one or more values or
variables after the `return` statement. These values are communicated to
the program outside the function. If you want to use them outside the
function, you can put them into a variable when you assign the call to
the function to that variable.

For instance, suppose a function is called using a statement
`<variable> = <function>()`. The function makes a calculation and stores
it as `<result>`. `return <result>` then ends the function, and the
value stored in `<result>` "comes out of" the function. Due to the way
`<function>()` was called, this value ends up in `<variable>`.

If this sounds a bit convoluted, it will probably become clear after
studying the following example:

```python
from math import sqrt

def pythagoras( a, b ):
    return sqrt( a*a + b*b )

c = pythagoras( 3, 4 )
print( c )
```

The function `pythagoras()` calculates the value of the square root of
the sum of the squares of its two parameters. Then it returns that
value, using the `return` statement. The main program "captures" the
value by assigning it to variable `c`, then prints the contents of `c`.

Note that the `return` statement in the example above has a complete
calculation with it. That calculation is done in the function, which
leads to a value. It is the result of the calculation, i.e., the value,
which is returned to the main program.

Now suppose that you want to only do this calculation for positive
numbers (which would not be strange, as the function clearly is meant to
calculate the length of the diagonal side of a right triangle, and who
ever heard of a triangle with sides of length zero or less). Examine
this code:

```python
from math import sqrt

def pythagoras( a, b ):
    if a <= 0 or b <= 0:
        return
    return sqrt( a*a + b*b )

print( pythagoras( 3, 4 ) )
print( pythagoras( -3, 4 ) )
```

At first glance this code might seem fine: as it has nothing to
calculate for negative numbers, it just returns no value. However, when
you run this program you find it prints the special value `None`. I
discussed this special value in Chapter
<a href="#ch:simplefunctions" data-reference-type="ref" data-reference="ch:simplefunctions">6</a>.
The main program expected the function `pythagoras()` to return a
number, so `pythagoras()` is failing its duties by returning nothing in
certain circumstances. You should always be very clear about what data
type your function returns, and ensure that in each and every
circumstance the function actually returns a value of that type. By the
way, the following code is equivalent to the code above (and has the
same mistake):

```python
from math import sqrt

def pythagoras( a, b ):
    if a > 0 and b > 0:
        return sqrt( a*a + b*b )

print( pythagoras( 3, 4 ) )
print( pythagoras( -3, 4 ) )
```

In this code, you do not see the `return` without a value explicitly,
but it is there nonetheless. If Python reaches the end of a function
code block without having found a `return`, it will return from the
function without a value.

If you wonder what you should return in circumstances that you do not
have a good return value for: that depends on the application. For
instance, for the `pythagoras()` function, you could decide that it will
return $$-1$$ whenever it gets provided with arguments that it cannot
process. As long as you communicate that to the user of a function, the
user can ensure that the main program handles such exceptional cases in
the spirit of the program as a whole. For instance:

```python
from math import sqrt
from pcinput import getInteger

def pythagoras( a, b ):
    if a <= 0 or b <= 0:
        return -1
    return sqrt( a*a + b*b )

num1 = getInteger( "Give side 1: " )
num2 = getInteger( "Give side 2: " )
num3 = pythagoras( num1, num2 )
if num3 < 0:
    print( "The numbers you provided cannot be used." )
else:
    print( "The diagonal side's length is", num3 )
```

Note that every line of code in the function that occurs immediately
after a `return` at the same level of indentation will always be
ignored. E.g., in the function:

```python
from math import sqrt

def pythagoras( a, b ):
    if a <= 0 or b <= 0:
        return -1
        print( "This line will never be printed" )
    return sqrt( a*a + b*b )
```

the line below `return -1` clearly states how useless it is.

### Difference between `return` and `print`

I noticed in the past that many students struggle with the difference
between a function returning a value and a function printing a value.
Compare the following two pieces of code:

```python
def print3():
   print( 3 )
print3()
```

and:

```python
def return3():
   return 3
print( return3() )
```

Both the function `print3()` and `return3()` are called in their
respective codes, and result in the printing of the value 3. The
difference is that the printing of this value in the case of `print3()`
happens in the function, while the function returns nothing, while in
the case of `return3()` the function only returns the value 3, which is
then printed in the main program. For the user the result of these codes
looks the same: both display the number 3. But for the programmer the
two functions involved are quite different.

The function `print3()` can only be used for one purpose, namely to
display the number 3. The function `return3()`, however, can be used
wherever I need the number 3, regardless whether I need to display it,
use it in a calculation, or assign it to a variable. For instance, the
following code raises 2 to the power of 3 and prints the result:

```python
def return3():
   return 3
x = 2 ** return3()
print( x )
```

On the other hand, the following code leads to a runtime error when
executed:

```python
def print3():
    print( 3 )
x = 2 ** print3() # Erroneous code!
print( x )
```

The reason is that while `print3()` displays the value of 3 on the
screen (you even see it above the runtime error when you run the code),
it does not produce the actual value 3 in such a way that the
calculation can use it. The function `print3()` actually returns the
special value `None`, which cannot be used in a calculation.

So, if you want to create a function that produces a value that can be
used in other parts of the program, then the function must return that
value. If you want to create a function that just displays something on
the screen, you can use a print statement in the function to do that,
but the function does not need to return anything.

### Welcome to the machine

If you still have troubles imagining how functions work, think of them
like this:

A function is like a big machine, for instance, a machine that makes
pancakes. It has some input hoppers at the top, which are labeled
"milk," "eggs," and "flour." Those are the input parameters. You can
decide what pancakes you want by putting the right stuff in the hoppers;
for instance, if you want whole-grain pancakes, you put whole-grain
flour into the "flour" hopper. Of course, you can be certain that things
will go dramatically wrong if you put eggs into the "milk" hopper – or
you try to put a cat into the "flour" hopper.

Anyway, once the hoppers are loaded the machine starts huffing and
puffing. You patiently wait next to the output hopper which, surprise
surprise, is labeled "return." And after a short while, a pancake slides
out. The pancake is the return value that the machine produced.

The machine also has a display. Maybe after you put something
inappropriate into the "flour" hopper, the display says: "Cat stuck in
the machine, please reset." The display is where everything that you
"print" in the machine appears.

Now, you understand that it is useless if, after loading the right
ingredients into the input hopper, the machine just displays "Pancake is
ready!" You want the actual pancake. That’s why the machine must
"return" it via its output hopper, from which you can take it and
"assign" it to your lunch plate. Just printing that the pancake exists
is not sufficient.

By the way, one of the nice things about the pancake making machine is
that even if you do not know how pancakes are made, you can still get
pancakes as long as you manage to supply the right ingredients. That’s
also what is so nice about functions: they may do complex things for you
without you needing to know how they accomplish them.

![machine](media/Machine.png "machine"){:width="70%"}

### Multiple return values

In your functions, you are not limited to returning just one value. You
can return multiple values by putting commas in between. If you want to
use these values in the program after the call to the function, you have
to assign them to multiple variables. You put them to the left of the
assignment, also with commas in between. This is easiest to illustrate
with and example:

```python
import datetime

def addDays( year, month, day, dayincrement ):
    startdate = datetime.datetime( year, month, day )
    enddate = startdate + datetime.timedelta( days=dayincrement )
    return enddate.year, enddate.month, enddate.day

y, m, d = addDays( 2015, 11, 13, 55 )
print( "{}/{}/{}".format( y, m, d ) )
```

The function `addDays()` gets four arguments, namely integers indicating
a year, a month, and a day, and a number of days that you want to add to
that date. It returns three values, namely a new year, month, and day.
These are in this code captured in the main program in three variables,
namely `y`, `m`, and `d`.

When you look at the code above, you might be mystified how exactly
`addDays()` is doing its job. As I said, it’s a nice thing about
functions that as long as the function works and you know what arguments
it wants and what it returns, you can use the function without any
knowledge of its internal process. So you can just ignore the code for
`addDays()` (note: the contents of `addDays()` use the `datetime`
module, which is discussed in Chapter
<a href="#ch:varioususefulmodules" data-reference-type="ref" data-reference="ch:varioususefulmodules">28</a>).

### Calling functions from functions

Functions are allowed to call other functions, as long as those other
functions are known to the calling function. For instance, the following
code shows how the function `euclideanDistance()` uses the function
`pythagoras()` to calculate the distance between two points in
2-dimensional space.

```python
from math import sqrt

def pythagoras( a, b ):
    if a <= 0 or b <= 0:
        return -1
    return sqrt( a*a + b*b )

def euclideanDistance( x1, y1, x2, y2 ):
    return pythagoras( abs( x1 - x2 ), abs( y1 - y2 ) )

print( euclideanDistance( 1, 1, 4, 5 ) )
```

`euclideanDistance()` knows `pythagoras()`, because `pythagoras()` was
defined before `euclideanDistance()` is called.

If you want, you can put functions inside other functions, i.e., you can
"nest" functions. For instance, you can place `pythagoras()` in
`euclideanDistance()`. That means that `pythagoras()` can be called
inside `euclideanDistance()`, but not elsewhere in the program.

```python
from math import sqrt

def euclideanDistance( x1, y1, x2, y2 ):

    def pythagoras_inside( a, b ):
        if a <= 0 or b <= 0:
            return -1
        return sqrt( a*a + b*b )

    return pythagoras_inside( abs( x1 - x2 ), abs( y1 - y2 ) )

print( euclideanDistance( 1, 1, 4, 5 ) )
# print( pythagoras_inside( 3, 4 ) )
```

It is not very common that nested functions are used, but it is
possible.

Note: if you remove the hash mark before the last line of the code
above, it adds a call to `pythagoras_inside()`. This will cause a
runtime error, as `pythagoras_inside()` is only visible inside
`euclideanDistance()`.

Write a function called `printx()` that just prints the letter "x." Then
write a function called `multiplex()` which takes as argument an integer
and prints as many times the letter "x" as the integer indicates by
calling the function `printx()` that many times.

### Naming functions

Convention prescribes that you should not start a function name with an
underscore (such function names are reserved for the developers of
Python itself), and that you try to use only lower case letters. If the
function name consists of multiple words, you can either put underscores
between the words, or start every word except the first with a capital
(different programmers prefer different conventions in this respect, but
it does not matter much as you can always recognize a function by the
fact that it has parentheses after the name).

Certain function names are typical for particular functionalities.

A function that tests if a certain item has a certain property, which
then returns either `True` or `False` depending on whether the property
holds, commonly has a name that starts with the word `is`, which is then
followed by the name of the property, starting with a capital. For
instance, a function that tests if a number is even, would be called
`isEven()`.

Write the function `isEven()`.

Write the function `isOdd()`, which determines whether a number is odd,
by calling the function `isEven()` and inverting its result.

Note: if you want to use a function like `isEven()` in a conditional
statement, for instance, because you want to execute an action only for
numbers that are even, you do not need to write
`if isEven( num ) == True:`. You can simply write `if isEven( num ):`,
because the function already returns `True` or `False`. Using an
is-function in such a way makes a program more readable.

A function that gets the value of a certain property and returns it,
commonly starts with the word `get`, which is then followed by the name
of the property, starting with a capital. For instance, a functions that
gets the fractional part of a float (i.e., the decimals) would be called
`getFraction()`.

Write the function getFraction().

The opposite of a get function is a function that gives a property a
certain value. Such a function commonly starts with `set`, and for the
rest is similar to a `get` function. I cannot give an example as at this
point I have not yet explained how you can use a function to give
something a value, as functions cannot change the values of their
parameters (at least, for the data types that we have used until now).
This will follow in a later chapter.

If you stick to such naming conventions, it will make your code more
readable.

### Commenting functions

In all the chapters until now, you have seen very little commenting of
code. While books and courses on programming often encourage students to
write comments in code, I myself am of the opinion that code should be
"self-documenting," i.e., that you can easily derive from code what it
does simply by reading it. You can accomplish that often by choosing
strong names for variables and functions, judiciously using white spaces
and empty lines, good indenting (which Python enforces), and not using
any convoluted trickery just because it makes the code a little bit
faster or to show off how smart you are.[^5]

So while I see comments as an extra that you should use when you feel
you need to explain something particular about your code, my opinion on
comments for functions is different. The idea behind a function is that
the user of the function does not need to look at the function’s code to
use it. Therefore, what the function does and how it works, should be
explained in comments at the top of the function, above the function
name.

In the comments for a function, you explain three things:

-   What the function does

-   What arguments the function needs/accepts, including data types

-   What the function returns, including data types

If a function has any side effects, i.e., things it affects in the main
program, then this should be carefully documented in the comments too. I
do not put that in the list above, because a function *should not have
any side effects*.

Note: For the answers to the exercises in this chapter I have added
comments to the functions in a form that I find acceptable. In follow-up
chapters I often will not do that as I discuss the functions in text
anyway, or I want you to study the contents of the function. However, I
always write comments for functions that I write in code that I use for
other purposes.

[^5]: A little anecdote on the side here: I once heard someone extol the
    intellect of a certain programmer by saying "when I see his code, I
    don't understand any of it!" When someone would say that about my
    code, I would feel deeply ashamed.
