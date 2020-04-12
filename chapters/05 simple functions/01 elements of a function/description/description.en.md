A function is a block of reusable code that performs some action. To get
a function to do its job, you "call" it, with some appropriate
parameters if the function requires them. The idea is that you do not
need to have knowledge about how a function performs its action. You
only need to know three things:

-   The name of the function

-   The parameters it needs (if any)

-   The return value of the function (if any)

These will now be discussed in turn.

### Function name

Each function has a name. Like a variable name, a function name may
consist of letters, digits, and underscores, and cannot start with a
digit. Almost all standard Python functions consist only of lower case
letters. Usually a function name expresses concisely what the function
does.

When referring to a function, it is convention to use the name, and put
an opening and closing parenthesis after the name, as functions are
always called in code with such parentheses.

### Parameters

Some functions are called with parameters ("arguments"), which may or
may not be mandatory. The parameters are placed between the parentheses
that follow the function name. If there are multiple parameters, you
place commas between them.

The parameters are the values that the user supplies to the function to
work with. For instance, the `int()` function must be called with one
parameter, which is the value that the function will try make an integer
representation of. The `print()` function may be called with any number
of parameters (even zero), which it will display, after which it will go
to a new line.

In general, a function cannot change parameters. For instance, look at
the following code:

```python
x = 1.56
print( int( x ) )
print( x )
```

As you can see when you run this code, the `int()` function has not
changed the actual value of `x`; it only told the `print()` function
what the integer value of `x` is. The reason is that, in general,
parameters are "passed by value." This means that the function does not
get access to the actual parameters, but it gets copies of the values of
the parameters. I say "in general" because not all data types are
"passed by value," but the ones I have discussed until now are. It will
be a while before you get to a chapter that introduces data types that
can be changed by functions when they are passed as parameters, and I
will make abundantly clear how that works when it comes up.

If a function gets multiple parameters, their order matters. For
instance, the function `pow()` gets two parameters, and raises the first
to the power of the second.

```python
base = 2
exponent = 3
print( pow( base, exponent ) )
```

The names of the variables that are used as parameters do not matter,
the first is raised to the power of the second. So the following example
will give a different outcome than the first, as the same variables are
given to the function in a different (rather confusing) order.

```python
base = 2
exponent = 3
print( pow( exponent, base ) ) # confusing use of variables 
```

What happens if you try to call a function with parameters that it
cannot work with? For instance, what happens if I call the `int()`
function with a string that does not contain an integer value, or the
`pow()` function with strings instead of numbers? In general, this will
lead to runtime errors in your code. For instance, both lines of the
code below give a runtime error.

    x = pow( 3, "2" )
    y = int( "two-and-a-half" )

### Return value

A function may or may not "return" a value. If a function returns a
value, that value can be used in your code. For instance, the function
`int()` returns an integer representation of the parameter it gets. You
can place this return value in a variable, using an assignment, or use
it in a different manner, for instance immediately print it. You can
even not do anything with it, though there is little reason to call the
function in that case.

```python
x = 2.1
y = '3'
z = int( x )
print( z )
print( int( y ) )
```

As you can see from the example above, you can even use function calls
as parameters for a function; e.g., the second call to the `print()`
function in the example gets as parameter a call to the function
`int()`. In this example, the call to the `int()` function is executed
before the `print()` function is called, as Python first calculates the
values for all the parameters before it makes a function call. So the
return value of `int()` is a parameter for `print()`.

Not all functions return a value. For instance, the `print()` function
does not. If you are not careful, this may lead to strange behavior of
your program. For instance, examine and run the following code:

```python
print( print( "Hello, world!" ) )
```

You can see that this code prints two lines, the first containing the
text "Hello, world!" and the second containing the word "None." What is
that "None" doing there? To find that out, let's examine how Python
evaluates this statement.

When Python first encounters this statement, it must evaluate
`print( <something> )`. Since `<something>` is an argument, it starts by
evaluating that. `<something>` is actually `print( <something_else> )`.
Since `<something_else>` is an argument, it now evaluates that.
`<something_else>` is the string `"Hello, world\`"!. This is not
something that needs to be evaluated, so it calls `print()` with this
string as argument, and "captures" the return value of `print()` because
it needs it as the evaluation of `<something>`.

Here is the crux: `print()` has no return value, so there is nothing
that Python can use for `<something>`. For situations such as this,
Python has a special value called `None`. So the first `print()` gets
called with `None` as argument, and this leads to Python displaying the
word "None."

`None` is a special value that indicates "no value at all." If you try
to print such a value, Python prints the word "None," but is not
actually printing a string that is `"None"`. It only indicates that
there was nothing to print. `None` is different from, for instance, an
empty string (`""`). An empty string is still a value, namely a string
of length zero. `None` is no string at all, no integer, no float,
nothing. So be careful when trying to use a function call as a
parameter; if the function does not actually return a value, weird
things may happen.

### A function is a black box

Let me stress once more that you may consider a function a "black box":
you do not need to know how the function works or how it is implemented.
The name, parameters, and return value are all you need to know. The
function might, internally, create variables and do calculations, but
they do not have an effect on the rest of your code.

…At least, if the function is implemented well. A function that has no
effect on your code is called a "pure function," and the functions that
I discuss here are all "pure functions." However, sometimes functions
are designed that actually do have an effect outside the function,
specifically, that the user may provide parameters to that undergo a
change. That may be fine, if it is intentional and well-documented. Such
functions are called "modifiers." Modifiers will come up in later
chapters.

For now, you can just assume that any function that you use, has no
effect on the rest of your code. So calling a function is safe.
