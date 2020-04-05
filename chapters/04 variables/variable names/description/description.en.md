So far, I have only used variables called `x`, `y`, and `z` (and one
erroneous `days_in_a_year`). However, you are free to choose the names
of your variables as you like them, provided that you follow a few
simple rules, namely:

-   A variable name must consist of only letters, digits, and/or
    underscores (`_`)

-   A variable name must start with a letter or an underscore

-   A variable name should not be a reserved word

"Reserved words" (or "keywords") are:

    False      class      finally    is         return
    None       continue   for        lambda     try
    True       def        from       nonlocal   while
    and        del        global     not        with
    as         elif       if         or         yield
    assert     else       import     pass
    break      except     in         raise

You can use capitals and lower case letters in variable names, but you
should realize that variable names are case sensitive, i.e., the
variable `world` is not the same as the variable `World`.

### Conventions

Programmers follow many conventions when choosing variable names. The
major ones are the following:

-   Programmers *never* choose variable names that are also the names of
    functions (whether they are functions provided by Python or
    functions they wrote themselves). Doing so will cause the
    corresponding function to be no longer accessible by the code, and
    may then lead to rather eccentric errors.

-   Programmers try to choose variable names that are in some way
    meaningful to the code. For instance, a variable that stores the
    number of seconds in a week, might have the name `secs_per_week`,
    but not the name `i_hate_my_job`. It would be even worse to name a
    variable that contains the numbers of seconds in a week
    `secs_per_month`.

-   An exception to choosing meaningful variable names is choosing names
    for "throw-away" variables, i.e., variables that you only use in a
    very small section of the code and that are no longer needed
    afterwards, and that have no good meaning by themselves. Programmers
    usually choose a single-letter name for such variables. For
    instance, if a variable is needed to quickly count to 100, after
    which it is not needed anymore, programmers often choose the letter
    `i` or `j` for such a variable.

-   To avoid confusion with capitals and lower case letters, programmers
    tend to use only lower case letters in variable names.

-   If a variable name is chosen that consists of multiple words,
    programmers put one underscore between each of the words.

-   Programmers never choose variable names that start with an
    underscore. Such variable names are considered reserved for the
    authors of the Python interpreter.

You should try to stick to these conventions for your own code. In
particular the convention of choosing meaningful variable names is
important to follow, because meaningful variable names make code
readable and maintainable. Look, for instance, at the following code:

```python
a = 3.14159265
b = 7.5
c = 8.25
d = a * b * b * c / 3
print( d )
```

Do you understand what this code does? You probably see that a seems to
be an approximation of $$\pi$$, but what is `d` supposed to be?

I can tell you that this code calculates the volume of a cone. You
probably would not have guessed that, but that is what it does. Now I
ask you to change the code to calculate the volume of a cone that is 4
meters high. What change will you make? If height is part of the
calculation, it is probably `b` or `c`. But which is it? Maybe if you
know a bit of maths and you look at the calculation of `d`, you realize
that `b` is squared in this calculation, which seems to refer to the
base of the cone, which is a circle. So it is probably `c`. But you
cannot be sure.

Now look at the following, equivalent code:

```python
pi = 3.14159265
radius = 7.5
height = 8.25
volume_of_cone = pi * radius * radius * height / 3
print( volume_of_cone )
```

This is much more readable, right? If I asked you to look at this code
and tell me what it does, and make the requested change, I don’t expect
you to hesitate in answering.

Such code with meaningful variable names tends to become
"self-documenting"; you do not need to add any comments to make the user
understand what it does and how it does it. Still, in the code above a
line of comment that says:  

```python
# calculation of volume of a cone with radius 7.5 and height 8.25
```
  
would not be misplaced.

### Practicing with variable names

{:class="callout callout-info"}
> #### Exercise
> In the code block below, the value 1 is assigned to a number of (potential) variable names. Some of these are legal, others are not. Identify the illegal variable names, and explain why they are illegal.
> ```python
> classification = 1   # 1
> Classification = 1   # 2
> cl@ssification = 1   # 3
> class1f1cat10n = 1   # 4
> 1classification = 1  # 5
> _classification = 1  # 6
> class = 1            # 7
> Class = 1            # 8
>  ```

{:class="callout callout-info"}
> #### Answer
> The third, fifth, and seventh assignments are illegal. The third because it does not consist of only letters, digits, and underscores. The fifth because it starts with a digit. The seventh because it is a reserved word (fortunately, syntax hightlighting makes it stand out). While the others are legal, according to convention the sixth should be avoided because it starts with an underscore, and the second and eighth too, as they contain capitals. The eighth is the worst in this respect, as it also looks like a reserved word.

### Constants

Many programming languages offer the ability to create "constants,"
which are values assigned to a variable which can no longer be changed
after the value has been first assigned. It is convention in most such
languages that the name of a constant is written in all capitals.
Constants can be useful to make code more readable. For instance, to
calculate the total of a bill of €24.95 with a 15% service charge,
you can use:

```python
total = 24.95
final_total = int( 100 * total * 1.15 ) / 100
print( final_total )
```

However, it is more readable to write:

```python
SERVICE_CHARGE = 1.15
CENTS = 100

total = 24.95
final_total = int( CENTS * total * SERVICE_CHARGE ) / CENTS
print( final_total )
```

Not only is it more readable, but it also makes the code easier to
change should the service charge be calculated differently in the
future. Especially if the service charge occurs in the code multiple
times, if it is defined just once as a constant at the top of the code,
it can be easily found and changed. When they are numerical, special
values such as the service charge are often called "magic numbers,"
i.e., their particular value has a special meaning, which is unclear if
you just see the number, so you are better off using a meaningful name
instead of the number.

While constants are very useful for coding purposes, Python does not
support them (which is a pity), i.e., in the code above `SERVICE_CHARGE`
is a regular variable and can be changed anywhere in the code. Still, it
is convention that any variable that is written in all capitals is
supposed to be a constant and should not be changed in the code, after
it got its initial value at the top of the code.

You are encouraged to use such "all capitals variable names" whenever
magic numbers occur in your code.
