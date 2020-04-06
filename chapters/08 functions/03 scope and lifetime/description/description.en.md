Scope refers to visibility. In particular, when discussing the scope of
a variable, it refers to the places in a program where a variable is
visible and can be changed. Lifetime refers to how long a variable
exists in memory. Lifetime is closely related to scope, which is why I
discuss them in one section.

### Scope of variables

In general, the scope of a variable is at least the code block in which
it is created, and all the code blocks that are nested within that code
block at a deeper indent level. The follow code demonstrates how the
scope of variables is defined for Python:

```python
hello = "Hi!"
bye = "Goodbye!"

for i in range( 3 ):
    for j in range( 2 ):
        afternoon = "Good afternoon"
        print( bye )
    print( j )
    print( hello )
    print( afternoon )

print( i )
print( j )
print( afternoon )
```

The variables `hello` and `bye` are created at the top level of the
program, which means their scope is the whole program. The variables
`i`, `j`, and `afternoon` are defined in code blocks which are at a
deeper indent level. In most programming languages, that would mean that
their scope would be restricted to those deeper levels, but Python is
friendly in this respect and makes their scope extend beyond the loop
that they are in. So all these variables are visible in the program
after they have been defined.

How does this work with functions?

```python
dozen = 12

def dimeAdozen():
    print( "There are", dozen/dime, "dimes in a dozen" )

dime = 10
dimeAdozen()
print( "dime =", dime, "and dozen =", dozen )
```

Again, we see that both `dozen` and `dime` are visible within the
function `dimeAdozen()`. They can be seen by the function because they
have been defined before the function is called, and since the code
block of the function is at a deeper indent level, it can see these
variables.

However, now look at the following code, which contains a small change
from the code above:

```python
dozen = 12

def dimeAdozen():
    dozen = 13
    print( "There are", dozen/dime, "dimes in a dozen" )

dime = 10
dimeAdozen()
print( "dime =", dime, "and dozen =", dozen )
```

Run this code, then examine it and its output closely, and compare it
with the code and the output of the code block above it. The variable
`dozen` seems to get a new value in the function `dimeAdozen()`, which
leads to the function claiming that there are now 1.3 dimes in a dozen.
However, when the value of `dozen` is printed in the main program, its
value is shown to be still 12, and not 13.

The reason is that the variable `dozen` in the function is a different
one than the variable `dozen` in the main program. By assigning a value
to a variable in a function, a new, "local" variable is created. And
this variable is used for the remainder of the function. The original
variable `dozen` still exists, but is invisible to the function once it
has created its own `dozen`.

The lifetime of the variable `dozen` in the function is the period for
which the code block of the function is executed. As soon as the
function ends (for instance, because of a `return` or because the last
line was executed), the local variables of the function are destroyed.
They are no longer in the computer’s memory, and can no longer be
accessed.

```python
apple = "apple"
banana = "banana"
cherry = "cherry"
durian = "durian"

def printfruits_1():
    print( apple, banana )

def printfruits_2( apple ):
    banana = cherry
    print( apple, banana )

def printfruits_3( apple, banana ):
    cherry = "mango"
    banana = cherry
    print( apple, banana )

printfruits_1()
printfruits_2( cherry )
printfruits_3( cherry, durian )

print( "apple =", apple )
print( "banana =", banana )
print( "cherry =", cherry )
print( "durian =", durian )
```

Run this code and study it closely.

The three functions `printfruits_1()`, `printfruits_2()`, and
`printfruits_3()` print the variables `apple` and `banana`.

In `printfruits_1()` these are the two variables `apple` and `banana`
that are defined outside the function, as the function itself does not
try to define these variables.

In `printfruits_2()`, `apple` is the parameter of the function, which
means it is a variable local to the function that gets its value from
outside the function. The value it gets is the value of the variable
`cherry` (because `cherry` is provided as the argument when the function
is called), which is the word "cherry." `banana` is a variable that gets
its value in the function. This is a new, local variable `banana`, which
has nothing to do with the variable `banana` in the main program. It
gets the value of `cherry`, which is not locally known to the function,
so it uses the variable `cherry` from the main program for that.
Therefore, the local variable `banana` gets the value "cherry," and this
is the value that is printed.

In `printfruits_3()`, `apple` and `banana` are both parameters, so they
are both variables that are local to the function and that get their
initial value from the call to the function. The function then creates a
local variable `cherry`, which is independent from the variable `cherry`
from the main program. It then assigns the value of `cherry`, which is
`"mango"`, to the local variable `banana`. All these changes are
therefore made to local variables, and have no influence on the values
of variables from the main program.

When after the function calls the values of the variables from the main
program are printed, you see that they still have the values that were
originally assigned to them, regardless of whether they were used as
arguments to the function calls, or whether variables in the functions
with the same names got different values assigned. As soon as a variable
in a function gets assigned a value, if that variable was not yet
created in the function and was not a parameter of the function, a new,
local variable is created and used in the function. Such a new, local
variable is completely independent from any variable which exists
outside the function. Its lifetime is the period for which the function
is executed. Parameters can also be considered local variables of a
function.

This is a very powerful feature of functions: they do not have to take
into account variables that exist outside the function, as any variable
that they create is local to the function.

### Global variables

I showed above that variables that are created outside a function are
visible in the function, unless a new variable with the same name is
created in the function. Variables from the main program are called
"global" variables, as they are visible anywhere in the program, as
opposed to "local" variables that are only visible in a function.

It is good practice to make functions independent from the main program,
i.e., to not let them access any of the global variables. If you do need
to communicate values from outside a function to the function, then do
so by means of parameters. An exception can be made for variables that
are used as constants (see Chapter
<a href="#ch:variables" data-reference-type="ref" data-reference="ch:variables">5</a>).
If you do let a function access a constant, then make sure it is clear
to anyone who inspects the function that you are referring to a
constant, i.e., that the name of the constant is written in all
capitals.

You might wonder if it isn’t possible to change the values of global
variables in a function. This is, in fact, possible, but you have to
make clear that you explicitly want the global variable to be affected
by using the keyword `global`. The statement `global <variable>`
indicates that the particular variable mentioned is actually referring
to the global variable of this name. For example:

```python
fruit = "apple"

def changeFruit():
    global fruit
    fruit = "banana"

print( fruit )
changeFruit()
print( fruit )
```

While it is possible to affect global variables in functions, this is
not recommended as it makes the function dependent on the main program
(and thus no longer a "pure" function). Basically, it makes the function
have side effects, and (all together now:) *a function should not have
any side effects*.

It is also never necessary to include global variables in a function. If
you want to allow a function to affect a global variable, then let the
function return a value that can be assigned to the global variable.
Leave it to the main program to decide whether or not to overwrite the
value of one of its own variables. The only reason I mention it here is
that I sometimes see students reverting to the keyword `global` because
they have insufficient understanding of `return` statements. Denying the
existence of `global` is not effective, I rather admit that it exists
and warn students against using it.
