To complete this chapter, I want to discuss a few strategies on loop
design, and, in general, the design of algorithms.

### When to use a loop

If you roll five 6-sided dice, how big is the probability that you roll
five sixes? The answer is $$1/(6^5)$$, but suppose that you did not know
that, and wanted to use a simulation to estimate the probability. You
can imitate the rolling of a die using `randint()`, and so you can
imitate the rolling of five dice this way. You can check whether they
all show a 6. You can do that a large number of times, and then divide
the number of times that you rolled five sixes by the number of times
that you rolled five dice, to get an estimate. When I put this problem
to students (in a slightly more complicated form, so that the answer
cannot easily be calculated), I often get code that looks like this:

```python
from random import randint

TESTS = 10000

success = 0
for i in range( TESTS ):
    d1 = randint( 1, 6 )
    d2 = randint( 1, 6 )
    d3 = randint( 1, 6 )
    d4 = randint( 1, 6 )
    d5 = randint( 1, 6 )
    if d1 == 6 and d2 == 6 and d3 == 6 and d4 == 6 and d5 == 6:
        success += 1

print( "Chance at five sixes is", success / TESTS )
```

(You would need a bigger number of tests to get a more accurate
estimate, but I did not want this code to run too long.)

When I see code like this, I ask: "What if I had asked you to roll one
hundred dice? Would you really repeat that die rolling line 100 times?"
Whenever you see lines of code repeated with just a slight change
between them (or when you are copying/pasting within a block of code),
you should start thinking about loops. You can roll five dice by
stating:

```python
from random import randint

for i in range( 5 ):
    die = randint( 1, 6 )
```

"But," you might argue: "I need the value of all the five dice to see if
they are all sixes! Every time you cycle through the loop, you lose the
value of the previous roll!"

True enough, but the line that checks all the dice by using five boolean
expressions concatenated with `and`s is particularly ugly too. Can't you
streamline this? Is there no way that you can draw some conclusion upon
the rolling of one die?

By thinking a bit about it, you might come to the following conclusion:
as soon as you roll a die that is not a six, you already have failed on
your try, and you can skip to the next try. There are many ways to
effectuate this, but here is a brief one using a `break` and an `else`:

```python
from random import randint

TESTS = 10000

success = 0
for i in range( TESTS ):
    for j in range( 5 ):
        if randint( 1, 6 ) != 6:
            break
    else:
        success += 1

print( "Chance at five sixes is", success / TESTS )
```

You might think this is difficult to come up with, but there are other
ways too. You can, for instance, add up the values of the rolls and test
if the total is 30 after the inner loop. Or you can keep track of how
many dice were rolled to a value of 6 and check if that is 5 after the
inner loop. Or you can set a boolean variable to `True` before the inner
loop, then set it to `False` as soon as you roll something that is not 6
in the inner loop, and then test the variable after the inner loop.

The point is that the arbitrary long repetition of pieces of code can
probably be replaced by a loop.

### Processing data items one by one

Usually, when a loop is applied, you are working through a long series
of data items. Each cycle through the loop will process one of those
data items. You then often need to remember something about the data
items that you have processed so far, for which you need extra
variables. You have to be smart in thinking about such variables.

Take the following example: I will provide you with ten numbers, and I
need you to create a program that tells me which is the largest, which
is the smallest, and how many are divisible by 3. You might say: "It is
easy to determine the largest and the smallest; I just use the `max()`
and `min()` functions (introduced in Chapter
<a href="#ch:simplefunctions" data-reference-type="ref" data-reference="ch:simplefunctions">6</a>).
Divisible by 3 is a bit tricky, I have to think about that." But `max()`
and `min()` require you to keep all the numbers in memory. That's fine
for 10 numbers, but what about one hundred? Or a million?

Since you will have to process all the numbers, you have to think about
a loop, and in particular, a loop wherein you have only one of the
numbers available each cycle through the loop (but you will see them all
before the loop ends). You must now think about variables that you can
use to remember something each cycle through the loop, that allows you
to determine, at the end, which number was the largest, which the
smallest, and how many are divisible by 3. Which variables do you need?

The answer, which comes easy to anyone who has been doing some
programming, is that you need to remember, each cycle through the loop,
which is the largest number *until now*, which is the smallest number
*until now*, and how many numbers are divisible by 3 *until now*. That
means that every cycle through the loop you compare the new number with
the variables in which you retain the largest and smallest, and replace
them with the new number if that is appropriate. You also check if the
new number is divisible by three, and if so, increase the variable that
you use to keep track of that.

You will have to find good initial values for the three variables. The
divisible-by-3 variable can start at zero, but the largest and smallest
need an appropriate value. The best solution in this case is to fill
them with the first number, as that number is both the largest and the
smallest at that point.

I give this problem as an exercise below. Use the algorithm described
here to solve it.

### Start with the smallest unit and build outward

Suppose that I give you the following assignment: Of all the books on
all the shelves in the library, count the number of words and report the
average number of words for the books. If you ask a human to perform
this task, he or she will probably think: "I go to the library, get the
first book from the first shelf, count the words, write that number
down, then take the second book and do the same thing, etcetera. When I
finished the first shelf, I go to the second shelf and treat that one in
the same way, until I have done all the books on all the shelves in the
library. Then I add up the counts and divide by the number of books."
For humans this approach works, but when you need to tell a computer how
to do this, the task seems hard.

To solve this problem, I should start with the smallest unit that I need
to work with. In this case, the smallest unit is a "book." It is not
"word," because I don't need to do anything with a "word"; what I need
to do is count the words in a book. In pseudocode,[^4] that would be
something like:

```python
wordcount = 0
for word in book:
    wordcount += 1
```

When I code something like this, I can already test it. Once I am
satisfied that I can count the words in a book, I can move up to the
next smallest unit, which is the shelf. How do I process all the books
on a shelf? In pseudocode, it is something like:

```python
for book in shelf:
    process_book()
```

But what does `process_book()` do? It counts the words. I already wrote
pseudocode for that, which I simply need to insert in place of the
statement `process_book()`. This then becomes:

```python
for book in shelf:
    wordcount = 0
    for word in book:
        wordcount += 1
```

When I test this, I run into a problem. I find that I am counting the
words per book, but I am not doing anything with those word counts. I
just overwrite them. To get the average, I first need a count of all the
words in all the books. This means I have to initialize `wordcount` only
once.

```python
wordcount = 0
for book in shelf:
    for word in book:
        wordcount += 1
```

To calculate the average, I need to also count the books. Again, I only
need to initialize the `bookcount` once, at the start, and I have to
increase the `bookcount` every time I have processed one book. At the
end, I can then print the average.

```python
wordcount = 0
bookcount = 0
for book in shelf:
    for word in book:
        wordcount += 1
    bookcount += 1
print( wordcount / bookcount )
```

Finally, I can go up to the highest level: the library as a whole. I
know how to process one shelf, now I need to process all the shelves. I
should, of course, remember that the initialization of wordcount and
bookcount only should be done once, and the printing of the average too.
With that in mind, it is easy to extend the pseudocode to encompass the
library as a whole:

```python
wordcount = 0
bookcount = 0
for shelf in library:
    for book in shelf:
        for word in book:
            wordcount += 1
    bookcount += 1
print( wordcount / bookcount )
```

As you can see, I built a triple-nested loop, working from the inner
loop outward. To learn how to deal with nested loops, this is usually
the best approach.

[^4]: Pseudocode isn't real code, but it looks like code that more or
    less explains how an algorithm works. As such, it should be easy to
    implement it in various programming languages.
