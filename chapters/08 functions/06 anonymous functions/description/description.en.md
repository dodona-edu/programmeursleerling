The concept of "anonymous functions" should be considered optional
material: they are rarely used, and never needed. However, for
completeness I discuss them here.

Python allows a program to create a function that has no name. The
function can be assigned to a variable, and the variable can then be
used as if it is a function. To create an anonymous function, you use
the following syntax:

```python
lambda <parameters>: <statement>
```

`lambda` is a keyword. `<parameters>` is a sequence of parameter names,
separated by comma’s if there is more than one. `<statement>` is one
single statement. The anonymous function does not need the keyword
`return`, but the value of `<statement>` is used as return value.

For instance, the following code creates an anonymous function that
calculates the square of its parameter. The function gets assigned to a
variable `f`. `f` can then be called as a function, to calculate the
squares of numbers.

```python
f = lambda x: x*x
print( f(12) )
```

This code is exactly the same as the following code:

```python
def f( x ):
    return x*x
print( f(12) )
```

So, if anonymous functions are no different from regular functions, and
actually more limited as they can only use a single line of code, why
are they included in Python? Actually, there has been going on quite a
lot of debate amongst the people who create Python whether or not the
`lambda` keyword should remain. It is part of Python because it is also
part of other programming languages, in particular functional
programming languages such as Lisp and Haskell, which rely on the
concept of anonymous functions. But the `lambda` keyword in Python is
not as powerful as the `lambda` keyword in these other languages, and,
as we have seen, not really needed. A main reason that it is still part
of Python is backwards compatibility and the fact that there are many
Python users who like to use it.

Occasionally, anonymous functions have their uses, and can actually make
programs a bit more readable. I will show an example in Chapter
<a href="#ch:lists" data-reference-type="ref" data-reference="ch:lists">13</a>.
