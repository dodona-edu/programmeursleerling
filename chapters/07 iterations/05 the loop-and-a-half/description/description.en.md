Suppose you want to ask the user for two numbers in a loop. For every
two numbers that the user enters, you want to show their multiplication.
You allow the user to stop the program when he enters zero for any of
the numbers. For some reason, if the numbers are dividers of each other,
that is an error and the program also stops, but with an error message.
Finally, you will not process numbers higher than 1000 or smaller than
zero, but that is not an error; you just want to allow the user to enter
new numbers. How do you program that? Here is a first attempt:

```python
from pcinput import getInteger

x = 3
y = 7

while (x != 0) and (y != 0) and (x%y != 0) and (y%x != 0):
    x = getInteger( "Enter number 1: " )
    y = getInteger( "Enter number 2: " )
    if (x > 1000) or (y > 1000) or (x < 0) or (y < 0):
        print( "Numbers should both be between 0 and 1000" )
        continue
    print( "Multiplication of", x, "and", y, "gives", x * y )
    
if x == 0 or y == 0:
    print( "Goodbye!" )
else:
    print( "Error: the numbers cannot be dividers" )
```

Study this code and make a list of everything that you feel is bad about
it. Once you have done that, continue reading and compare your notes to
the list below. If you noted things that are bad about it that are not
on the list below, email the author of the book.

There are many things bad about this code. Here is a list:

-   To ensure that the loop is run at least once, `x` and `y` must be
    initialized. Why did I choose 3 and 7 for that? That was arbitrary,
    but I had to pick two numbers that are not dividers of each other.
    Otherwise the loop would not have been entered. On the whole, having
    to give variables some arbitrary starting values just to make sure
    that they exist is not nice, as their initial values are
    meaningless. You want to avoid that.

-   When you enter something that should end the loop (e.g., zero for
    `x`), the multiplication will still take place before the loop ends.
    That was not supposed to happen.

-   If you enter 0 for `x`, the code will still ask for a value for `y`,
    even if it does not need it anymore.

-   The boolean expression next to the `while` is rather complex. In
    this code it is still readable, but you can imagine what happens
    when you have many more requirements.

-   The error message for the dividers is not next to the actual test
    where you decide to leave the loop (i.e., the boolean expression
    next to the `while`).

The solution to some of these issues that certain programmers prefer, is
to initialize `x` and `y` with values that you read from the input. This
solves the arbitrary initialization, and also gets around the problem
that you print the result of the multiplication even when the loop was
already supposed to end. If you do this, however, in the loop you have
to move the asking for input to the end of the loop, and if you ever
have a `continue` in the loop, you also have to copy it there. The code
becomes something like this:

```python
from pcinput import getInteger

x = getInteger( "Enter number 1: " )
y = getInteger( "Enter number 2: " )

while (x != 0) and (y != 0) and (x%y != 0) and (y%x != 0):
    if (x > 1000) or (y > 1000) or (x < 0) or (y < 0):
        print( "Numbers should both be between 0 and 1000" )
        x = getInteger( "Enter number 1: " )
        y = getInteger( "Enter number 2: " )
        continue
    print( "Multiplication of", x, "and", y, "gives", x * y )
    x = getInteger( "Enter number 1: " )
    y = getInteger( "Enter number 2: " )

if x == 0 or y == 0:
    print( "Goodbye!" )
else:
    print( "Error: the numbers cannot be dividers" )
```

So this code removes two of the issues, but it adds a new one, which
makes the code a lot worse. The list of issues now is:

-   The statements that ask for input for each of the variables occur no
    less than three times in the code.

-   If you enter 0 for `x`, the code will still ask for a value for `y`.

-   The boolean expression next to the `while` is rather complex.

-   The error message for the dividers is not next to the actual test
    where you decide to leave the loop.

The trick to get around these issues is to control the loop solely
through `continue`s and `break`s (and perhaps the occasional `exit()`
when errors occur, though later in the course you will learn to use the
much "cleaner" `return` for that). I.e., you do the loop "always," but
decide to leave the loop or redo the loop when certain events occur
which you notice inside the loop. Doing the loop "always" you can
effectuate with the statement `while True` (as this simply means: the
test that decides whether or not you have to do the loop again, always
results in `True`).

```python
from pcinput import getInteger
from sys import exit

while True:
    x = getInteger( "Enter number 1: " )
    if x == 0:
        break
    y = getInteger( "Enter number 2: " )
    if y == 0:
        break
    if (x < 0 or x > 1000) or (y < 0 or y > 1000):
        print( "The numbers should be between 0 and 1000" )
        continue
    if x%y == 0 or y%x == 0:
        print( "Error: the numbers cannot be dividers" )
        exit()
    print( "Multiplication of", x, "and", y, "gives", x * y )

print( "Goodbye!" )
```

This code gets around almost all the problems. It asks for the input for
`x` and `y` only once. There is no arbitrary initialization for `x` and
`y`. The loop stops as soon as you enter zero for one of the numbers. It
prints error messages at the moment that the errors are noted. There is
no complex boolean expression needed with lots of `and`s and `or`s.

The only issue that is still remaining is that when the user enters a
value outside the range 0 to 1000 for `x`, he still gets to enter `y`
before the program says that he has to enter the numbers again. That is
best solved by writing your own functions, which follows in the next
chapter. (If you really want to solve it now, you can do that with a
nested loop, but I wouldn't bother.)

The code is slightly longer than the first version, but length is no
issue, and the code is a lot more readable.

A loop like this one, that uses `while True`, is sometimes called a
"loop-and-a-half." It is a common approach to writing loops for which
you cannot predict when they will end.

The user must enter a positive integer. You use the `getInteger()`
function from `pcinput` for that. This function also allows entering
negative numbers. If the user enters a negative number, you want to
print a message and ask him again, until he entered a positive number.
Once a positive number is entered, you print that number and the program
ends. Such a problem is typically solved using a loop-and-a-half, as you
cannot predict how often the user will enter a negative number before he
gets wise. Write such a loop-and-a-half (you will need exactly one
`break`, and you need at most one `continue`). Print the final number
that the user entered after you have exited the loop. The reason to do
it afterwards is that the loop is just there to control the entering of
the input, not the processing of the resulting variable.

I have noted in the past that many students find the use of `while True`
confusing. They see it often in example code, but do not really grasp
what the point of it is. And then they start inserting `while True` in
their code whenever they do not know exactly what they need to do. If
you have troubles understanding the loop-and-a-half, study this section
again, until you do.
