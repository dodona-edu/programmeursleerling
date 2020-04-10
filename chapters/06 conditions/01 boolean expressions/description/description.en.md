A conditional statement, often called an "if"-statement, consists of a
test and one or more actions. The test is a so-called "boolean
expression." The actions are executed when the test evaluates to True.
For instance, an app on a smartphone might give a warning if the battery
level is lower than 5%. This means that the app needs to check if a
certain variable `battery_level` is lower than the value $$5$$, i.e., if
`battery_level < 5` evaluates to `True`. If the variable `battery_level`
holds the value $$17$$, then `battery_level < 5` evaluates to `False`.

### Booleans

`True` and `False` are so-called "boolean values" that are predefined in
Python. `True` and `False` are actually the *only* boolean values, and
anything that is not `False`, is `True`.

You might wonder what the data type of `True` and `False` is. The answer
is that they are of the type `bool`. However, in Python every value can
be interpreted as a boolean value, regardless of its data type. I.e.,
when you test a condition, and your test is of a value that is not
`True` or `False`, it will still be interpreted as either `True` or
`False`.

The following values are interpreted as `False`:

-   The special value `False`

-   The special value `None` (which you encountered in Chapter
    <a href="#ch:simplefunctions" data-reference-type="ref" data-reference="ch:simplefunctions">6</a>)

-   Every numerical value that is zero, e.g., 0 and 0.0

-   Every empty sequence, e.g., an empty string (`""`)

-   Every empty "mapping," e.g., an empty dictionary (dictionaries
    follow in Chapter
    <a href="#ch:dictionaries" data-reference-type="ref" data-reference="ch:dictionaries">14</a>)

-   Any function or method call that returns one of these listed values
    (this includes functions that return nothing)

Every other value is interpreted as `True`.

Any expression that is evaluated as `True` or `False` is called a
"boolean expression."

### Comparisons

The most common boolean expressions are comparisons. A comparison
consists of two values, and a comparison operator in between. Comparison
operators are:

| operator | description |
|:--------:|-------------|
|        `<`  |    less than |
|        `<=` |  less than or equal to |
|        `==`  | equal to |
|        `>=` |  equal to or greater than |
|        `>`  |  greater than |
|        `!=` |  not equal |
{:class="table table-striped table-condensed" style="width:auto;margin-left:auto;margin-right:auto;"}

A common mistake is to use a single $$=$$ as a comparison operator, as the
single $$=$$ is the assignment operator. In general, Python will produce a
syntax or runtime error if you try to use a single $$=$$ to make a
comparison.

You can use the comparison operators to compare both numbers and
strings. Comparison for strings is an alphabetical comparison, whereby
all capitals come before all lower case letters (and digits come before
both of them). More on this will follow in Chapter
<a href="#ch:strings" data-reference-type="ref" data-reference="ch:strings">11</a>.

Here are some examples of the results of comparisons:

```python
print( "1.", 2 < 5 )
print( "2.", 2 <= 5 )
print( "3.", 3 > 3 )
print( "4.", 3 >= 3 )
print( "5.", 3 == 3.0 )
print( "6.", 3 == "3" )
print( "7.", "syntax" == "syntax" )
print( "8.", "syntax" == "semantics" )
print( "9.", "syntax" == " syntax" )
print( "10.", "Python" != "rubbish" )
print( "11.", "Python" > "Perl" )
print( "12.", "banana" < "orange" )
print( "13.", "banana" < "Orange" )
```

Make sure that you run these evaluations, check their outcome, and
understand them!

Do you understand why `3 < 13` is `True`, but `"3" < "13"` is `False`?
Think about it!

You can assign the outcome of a boolean expression to a variable if you
like:

```python
greater = 5 > 2
print( greater )
greater = 5 < 2
print( greater )
print( type( greater ) )
```

Write some code that allows you to test if $$1/2$$ is greater than, equal
to, or less than $$0.5$$. Do the same for $$1/3$$ and $$0.33$$. Then do the
same for $$(1/3)*3$$ and $$1$$.

Comparisons of data types that cannot be compared, in general lead to
runtime errors.

```python
# This code gives a runtime error.
print( 3 < "3" )
```

### `in` operator

Python has a special operator called the "membership test operator,"
which is usually abbreviated to the "in operator" as it is written as
`in`. The `in` operator tests if the value to the left side of the
operator is found in a "collection" to the right side of the operator.

At this time, I have discussed only one "collection," which is the
string. A string is a collection of characters. You can test if a
particular character or a sequence of characters is part of the string
using the `in` operator. The opposite of the `in` operator is the
`not in` operator, which gives `True` when `in` gives `False`, and which
gives `False` when `in` gives `True`. For example:

```python
print( "y" in "Python" )
print( "x" in "Python" )
print( "p" in "Python" )
print( "th" in "Python" )
print( "to" in "Python" )
print( "y" not in "Python" )
```

Again, make sure that you understand these evaluations!

Write some code that allows you to test for each vowel whether it occurs
in your name. You may ignore capitals.

### Logical operators

Boolean expressions can be combined with logical operators. There are
three logical operators, `and`, `or`, and `not`.

`and` and `or` are placed between two boolean expressions. When `and` is
between two boolean expressions, the result is `True` if and only if
both expressions evaluate to `True`; otherwise it is `False`.

When `or` is between two boolean expressions, the result is `True` when
one or both of the expressions evaluate to `True`; it is only `False` if
both expressions evaluate to `False`.

`not` is placed in front of a boolean expression to switch it from
`True` to `False` or vice versa.

For example:

```python
t = True
f = False
print( t and t )
print( t and f )
print( f and t )
print( f and f )
print( t or t )
print( t or f )
print( f or t )
print( f or f )
print( not t )
print( not f )
```

You have to be careful with logical operators, because combinations of
`and`s and `or`s might lead to unexpected results. To ensure that they
are evaluated in the order that you intend, you can use parentheses. For
example, rather than writing `a and b or c` you should write
`(a and b) or c` or you should write `a and (b or c)` (depending on the
order in which you want to evaluate the logical operators), so that it
is immediately clear from your code which evaluation you want the code
to do. Even if you know the order in which the logical operators are
processed by Python, someone else who reads your code might not.

For the code below, give values `True` or `False` to each of the
variables `a`, `b`, and `c`, so that the two expressions evaluate to
different values.

```python
a = # True or False?
b = # True or False?
c = # True or False?

print( (a and b) or c )
print( a and (b or c) )
```

If all the logical operators in a boolean expression are `and`, or they
all are `or`, the use of parentheses is not needed, since there is only
one possible evaluation of the expression.

Boolean expressions are processed from left to right, and Python will
stop the processing of an expression when it already knows whether it
will end in `True` or `False`. Take, for instance, the following code:

```python
x = 1
y = 0
print( (x == 0) or (y == 0) or (x / y == 1) )
```

When you divide by zero, Python gives a runtime error, so the expression
`x / y == 1` crashes the program if `y` is zero. And `y` actually is
zero. However, when Python processed the whole boolean expression, at
the point where it tested `y == 0` it determined that the expression as
a whole is `True`, because if any of the expressions that are connected
by an `or` to the expression as a whole is `True`, then the whole
expression is `True`. So there was no need for Python to determine the
value of `x / y == 1`, and it did not even attempt to evaluate it. Of
course, the test `y == 0` must be to the left of `x / y == 1`, so that
Python will test `y == 0` first.

Note: While you can make truly complex boolean expressions using logical
operators, I recommend that you keep your expressions simple if
possible. Simple boolean expressions make code readable.
