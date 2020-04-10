An alternative way of implementing loops is by using a `for` loop. `for`
loops tends to be easier and safer to use than `while` loops, but cannot
be applied to all iteration problems. `while` loops are more general. In
other words, everything that a `for` loop can do, a `while` loop can do
too, but not the other way around.

The syntax of a `for` loop is as follows:

```python
for <variable> in <collection>:
    <statements>
```

A `for` loop gets presented with a collection of items, and it will
process these items, in order, one by one. Every cycle through the loop
will put one item in the variable given next to the `for`, and can then
be used in the code block under the `for`. The variable does not need to
exist before the `for` loop is encountered. If it does, it gets
overwritten. It is a real variable, by the way, in the sense that it
still exists after the loop has finished. It will contain the last value
that it got assigned during the processing of the loop.

At this point you might wonder what a "collection" is. There are many
different kinds of collections in Python, and in this section I will
introduce a few. In later chapters collections will be discussed in more
detail.

### `for` loop with strings

The only collection introduced until now is the string. A string is a
collection of characters, e.g., the string `"banana"` is a collection of
the characters `"b", "a", "n", "a", "n"`, and `"a"`, in that specific
order. The following code loops through each of these letters:

```python
for letter in "banana":
    print( letter )
print( "Done" )
```

While this code is fairly trivial, let's go through it step by step (I
did not make a flow chart, as that is not easy for `for` loops).

When the `for` loop is encountered, Python takes the collection (i.e.,
the string `"banana"`) and turns it into an "iterable." What that is
exactly I will get to in Chapter
<a href="#ch:iteratorsandgenerators" data-reference-type="ref" data-reference="ch:iteratorsandgenerators">24</a>,
but for now assume that it is a list of all the letters in the string,
in the order that they appear in the string. Python then takes the first
of those letters, and puts it in the variable `letter`. It then executes
the code block below the `for`.

The code block contains only one statement, which is the printing of
`letter`. So the program prints "b," and then loops back to the `for`.
Python then takes the next letter, which is an "a," and it executes the
code block with `letter` being `"a"`. It then repeats this process for
each of the remaining letters. Once all the letters have been used, the
`for` loop ends, and Python executes the last line of the code, which is
the printing of the word "Done."

To be absolutely clear: In a `for` loop you do not have to write code
that explicitly increases some kind of variable that then grabs the next
letter, or something like that. The `for` statement handles that
automatically: every time it is looped back to, it takes the next item
from the collection.

### `for` loop using a variable as collection

In the code above, the literal string `"banana"` was used as the
collection, but it could also be a variable that contains a string. For
instance, the following code runs similar to the previous code:

```python
fruit = "banana"
for letter in fruit:
    print( letter )
print( "Done" )
```

You might wonder if this isn't dangerous. What happens if the programmer
changes the contents of the variable `fruit` in the loop's code block?
You can try this out using the following code:

```python
fruit = "banana"
for letter in fruit:
    print( letter )
    if letter == "n":
        fruit = "orange"
print( "Done" )
```

As you can see when you run this code, changing the contents of the
variable `fruit` in the loop has no effect on the loop's processing. The
sequence of characters that the loop processes is only constituted once,
when the `for` loop is first entered. Changing the value of `fruit` into
`"orange"` while the loop is still processing the value `"banana"`, does
not stop it from continuing to process `"banana"`. This is a great
feature of `for` loops, because it means they are guaranteed to end. No
`for` loops are endless![^2]

Note that there is a conditional statement in the loop above. There is
nothing that stops you from putting conditions in the code block for a
loop. There is also nothing against putting loops in the code block for
a condition, or even putting loops inside loops (more on that last
option follows later in this chapter). Most readers probably are not
surprised to hear that, but for the few who are completely new to
programming: as long as you stick to the syntactic requirements, you can
use conditional statements and loops wherever you can write Python
statements.

### `for` loop using a range of numbers

Python offers a `range()` function that generates a collection of
sequential numbers, which is often used for `for` loops. The simplest
call to `range()` has one parameter, which is a number. It will generate
all integers, starting at zero, up to but not including the parameter.

```python
for x in range( 10 ):
    print( x )
```

`range()` can get multiple parameters. If you give two parameters, then
the first will be the starting number (default is zero), while the
second will be the "up to but not including" number. If you give three
parameters, the third will be a step size (default is 1). You can choose
a negative step size if you want to count down. With a negative step
size, make sure that the starting number is higher than the number that
you want to count up to (or down to, in this case).

```python
for x in range( 1, 11, 2 ):
    print( x )
```

Change the three parameters above to observe their effect, until you
fully understand the `range()` function.

Use the `for` loop and `range()` function to print multiples of 3,
starting at 21, counting down to 3, in just two lines of code.

### `for` loop with manual collections

If you want to use a `for` loop to cycle through items in a collection
that you create manually, you can do so by listing all your items
between parentheses. This defines a "tuple" for the items of your
collection. Tuples will be discussed in detail in Chapter
<a href="#ch:tuples" data-reference-type="ref" data-reference="ch:tuples">12</a>.

```python
for x in ( 10, 100, 1000, 10000 ):
    print( x )
```

Or:

```python
for x in ("apple", "pear", "orange", "banana", "mango", "cherry"):
    print( x )
```

Your collection can even consist of mixed types.

### Practice with `for` loops

To get strong grips on how to use `for` loops, do the following
exercises.

You already created code with a `while` loop that asked the user for
five numbers, and displayed their total. Create code for this task, but
now use a `for` loop.

Create a countdown function that starts at a certain count, and counts
down to zero. Instead of zero, print "Blast off!" Use a `for` loop.

I am not going to ask you to build a `for` loop that asks the user to
enter numbers until the user enters zero. Why not?

[^2]: Unfortunately, I will have to revise this statement in Chapter
    <a href="#ch:iteratorsandgenerators" data-reference-type="ref" data-reference="ch:iteratorsandgenerators">24</a>,
    but it requires knowledge of pretty advanced Python to create an
    endless `for` loop – for now, and in general practice, you may
    assume that `for` loops are guaranteed to end.
