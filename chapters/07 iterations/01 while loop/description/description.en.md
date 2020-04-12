Suppose you have to ask the user for five numbers, then add them up, and
show the total. With the material from the previous chapters, you would
program that as follows:

```python
from pcinput import getInteger

num1 = getInteger( "Number 1: " )
num2 = getInteger( "Number 2: " )
num3 = getInteger( "Number 3: " )
num4 = getInteger( "Number 4: " )
num5 = getInteger( "Number 5: " )

print( "Total is", num1 + num2 + num3 + num4 + num5 )
```

But what if I want you to ask the user for 500 numbers? Are you going to
create a block of code of more than 500 lines long? Surely there must be
an easier way to do this?

Of course there is. You can use a loop to do this.

The first loop I am going to present to you is the `while` loop. A
`while` statement is quite similar to an `if` statement. The syntax is:

```python
while <boolean expression>:
    <statements>
```

Just like an `if` statement, the `while` statement tests a boolean
expression, and if the expression evaluates to `True`, it executes the
code block below it. However, contrary to the `if` statement, once the
code block has finished, the code "loops" back to the boolean expression
to test it again. If it still evaluates to `True`, the code block below
it gets executed once more. And after it has finished, it loops back
again, and again, and again…

Note: if the boolean expression immediately evaluates to `False`, then
the code block below the `while` is skipped completely, just like with
an `if` statement.

![loop](media/Loop.png "loop"){:width="70%"}

### `while` loop, first example

Let's take a simple example: printing the numbers 1 to 5. With a `while`
loop, that can be done as follows:

```python
num = 1
while num <= 5:
    print( num )
    num += 1
print( "Done" )
```

This code is also expressed by the flow chart in Figure
<a href="#f:chart4" data-reference-type="ref" data-reference="f:chart4">8.1</a>.

![while](media/Chart4en.png "while"){:width="60%" data-caption="Flow chart expressing a `while` loop."}

It is crucial that you understand this code, so let's discuss it step by
step.

The first line initializes a variable `num`. This is the variable that
the code will print, so it is initialized to 1, as 1 is the first value
that must be printed.

Then the `while` loop starts. The boolean expression says `num <= 5`.
Since `num` is 1, and 1 is actually smaller than (or equal to) 5, the
boolean expression evaluates to `True`. Therefore, the code block below
the `while` gets executed.

The first line of the code block below the `while` prints the value of
`num`, which is 1. The second line adds 1 to the value of `num`, which
makes `num` hold the value 2. Then the code loops back to the boolean
expression (i.e., the last line of the code, the printing of "Done," is
not executed as it is not part of the loop and the loop has not finished
yet).

Since `num` is 2, the boolean expression still evaluates to `True`. The
code block gets executed once more. 2 is displayed, `num` gets the value
3, and the code loops back to the boolean expression.

Since `num` is 3, the boolean expression still evaluates to `True`. The
code block gets executed once more. 3 is displayed, `num` gets the value
4, and the code loops back to the boolean expression.

Since `num` is 4, the boolean expression still evaluates to `True`. The
code block gets executed once more. 4 is displayed, `num` gets the value
5, and the code loops back to the boolean expression.

Since `num` is 5, the boolean expression still evaluates to `True`
(because `5 <= 5`). The code block gets executed once more. 5 is
displayed, `num` gets the value 6, and the code loops back to the
boolean expression.

Since `num` is 6, the boolean expression now evaluates to `False`
(because 6 is bigger than 5). Therefore, the code block gets skipped,
and the code continues with the first line below the code block, which
is the last line of the code. The word "Done" is printed, and the code
ends.

Change the code above so that it prints the numbers 1, 3, 5, 7, and 9.

### `while` loop, second example

If you understand the first example, you probably also understand how to
ask the user for five numbers and print the total. This is implemented
as follows:

```python
from pcinput import getInteger

total = 0
count = 0
while count < 5:
    total += getInteger( "Please give a number: " )
    count += 1

print( "Total is", total )
```

Study this code closely. There are two variables used. `total` is used
to add up the five numbers that the user enters. It is started at zero,
as at the start of the code the user has not yet entered any numbers, so
the total is still zero. `count` is used to count how often the code has
gone through the loop. Since the loop must be done five times, `count`
is started at 0 and the boolean expression tests if `count` smaller is
than 5. Since in the loop `count` gets increased by 1 at the end of
every cycle through the loop, the loop gets processed five times before
the boolean expression `False` is.

You may wonder why `count` is started at 0 and the boolean expression
checks if `count < 5`. Why not start `count` at 1 and check if
`count <= 5`? The reason is convention: programmers are used to start
indices at 0, and if they count, they count "up to but not including."
When you continue with programming, you will find that most code sticks
to this convention. Most standard programming constructs that use
indices or count things apply this convention too. My advice is
therefore that you get used to it, as it makes code easier to read.

Note: The variable `count` is what programmers call a "throw-away
variable." Its only purpose is to count how often the loop has been
cycled through, and it has no real meaning before the loop, in the loop,
or after the loop has ended. Programmers often choose a single-character
variable name for such a variable, usually `i` or `j`. In this example I
chose the name `count` because it is illustrative of what the variable
does for the code, but a single-character name for this variable would
have been acceptable.

Change the code block above so that it not only prints the total, but
also the average of the five numbers.

The first code block of this chapter also asks the user for five
numbers, and prints the total. However, that code block uses "Enter
number `x`: " as a prompt, whereby `x` is a digit. Can you change the
code block above so that it also uses such a changing prompt to ask for
each number?

### Putting the `while` loop under user control

Suppose that, in the second example, you do not want the user to be
restricted to entering exactly five numbers. You want the user to enter
as many numbers as he wants, including none. This means that you cannot
predict how many iterations through the `while` loop are needed.
Instead, it is the user who controls when the loop ends. You therefore
have to give the user the means to indicate that the loop should end.

The code block below shows how to use a `while` loop to allow the user
to enter numbers as long as he wants, until he enters a zero. Once a
zero is entered, the total is printed, and the program ends.

```python
from pcinput import getInteger
    
num = -1
total = 0
while num != 0:
    num = getInteger( "Enter a number: " )
    total += num
print( "Total is", total )
```

This code works, but there are (at least) two ugly things about it.
First, `num` is initialized to -1. The -1 is meaningless, I just needed
an initialization that would ensure that the `while` loop would be
entered at least once. Second, when the user enters zero, `total` still
gets increased by `num`. Since `num` is zero at that point, it does not
matter for the total, but if I wanted the user to end the program by
typing something else (for instance, a negative number), then `total`
would now hold the wrong value.

Because of these ugly elements, some programmers prefer to write this
code as follows:

```python
from pcinput import getInteger
    
num = getInteger( "Enter a number: " )
total = 0
while num != 0:
    total += num
    num = getInteger( "Enter a number: " )
print( "Total is", total )
```

This solves the ugly parts from the previous code, but introduces
something new that is ugly, namely the repetition of the `getInteger()`
function. How this can be solved follows at the end of this chapter. For
now, make sure that you understand how `while` loops work.

Create a loop that lets the user enter some numbers until he enters
zero, and then prints their total and their average. Make sure you test
the loop with no numbers entered, and with several copies of the same
number entered.

### Endless loops

The code below is supposed to start at number 1, and add up numbers,
until it encounters a number that, when squared, is divisible by 1000.
The code contains an error, though. See if you can spot it (without
running the code!).

```python
number = 1
total = 0
while (number * number) % 1000 != 0:
    total += number
print( "Total is", total )
```

The heading of this subsection gave away the answer, of course: this
code contains a loop that never terminates. If you run it, it looks like
the program "hangs," i.e., sits there and does nothing. It is not doing
nothing, it is actually highly active, but it is in a never-ending
addition. `number` starts at 1, and is never increased in the loop, so
the boolean expression will always be `True`. This is called an "endless
loop," and it is the single one great danger in using `while` loops.

If you run this code in IDLE, you can stop it by pressing `Ctrl-C`.
Other editors may have menu options to interrupt code execution. In
user-unfriendly environments, you may actually have to "kill" the
process that runs the code using a system command.

Since every programmer writes endless loops by accident now and again,
it is good practice when you program a loop to immediately add a
statement to the loop that makes a change that is tested in the boolean
expression, so that you do not forget about it. I.e., if you write
`while i < 10:`, immediately add a line `i += 1` below it, and then
start adding the rest of your code in between.

Fix the code above so that it no longer is an endless loop.

### `while` loop practice exercises

You should now practice a bit with simple `while` loops.

Write countdown code. It starts with a given number (e.g., 10), and
counts down to zero, printing each number it encounters (10, 9, 8, …).
It does not print 0, instead it prints "Blast off!"

The factorial of a positive integer is that integer, multiplied by all
positive integers that are lower (excluding zero). You write the
factorial as the number with an exclamation mark after it. E.g., the
factorial of 5 is $$5! = 5 * 4 * 3 * 2 * 1 = 120$$. Write some code that
calculates the factorial of a number. Do not test your program with
numbers that are too high, as factorials grow exponentially (testing it
up to 10! is more than enough). Hint: to do this with a `while` loop,
you need two variables: one variable which at the end of the loop must
contain the answer, and one variable that contains the current factor.
In the loop, you multiply the answer with the current factor, before
subtracting 1 from the factor. Choose the right initializations of these
variables before the loop.
