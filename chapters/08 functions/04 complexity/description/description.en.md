Suppose that Python would not have built-in `max()` and `min()`
function, and neither do you have knowledge of (or are allowed to) use
anything of the chapters after this one. You get the following
assignment:

Write a program that processes two groups of three numbers (you can
write the program for fixed numbers, but later on you will add that the
user enters these numbers). It adds up the lowest numbers of each of the
groups, the middle numbers of each of the groups, and the highest
numbers of each of the groups. It then prints these three results.

How do you do this? You can start with something like:

```python
# First initialize variables in group 1 (num11, num12, num13)
# and in group 2 (num21, num22, num23) to some values.

smallest1 = 0
smallest2 = 0
medium1 = 0
medium2 = 0
largest1 = 0
largest2 = 0

if num11 < num12:
    if num11 < num13:
        smallest1 = num11
    else:
        smallest1 = num13
elif num12 < num13:
    smallest1 = num12
else:
    smallest1 = num13

# Test:
print( smallest1 )

# This works to get the smallest from group 1.
# Now do the same for the smallest from group 2.
# Then do something similar for the largest of group 1 and 2.
# Then invent something for taking the middle one.
# Finally, do all the additions and print the results...
```

You can imagine that with this approach, with nested `if` statements
that get repeated six times with different assignments in the branches,
this becomes a huge, unreadable, unmanageable program of which it is
hard to see whether it is correct or not. You have to approach the
problem in a smarter way.

Suppose that you have a function that determines the smallest of three
numbers, a function that determines the middle one of three numbers, and
a function that determines the largest one of three numbers. Then the
program is pretty simple to write! It will be something like:

```python
num11, num12, num13 = 436, 178, 992
num21, num22, num23 = 880, 543, 101

def smallest( n1, n2, n3 ):
    return n1 # just return something for now

def middle( n1, n2, n3 ):
    return n1 # just return something for now

def largest( n1, n2, n3 ):
    return n1 # just return something for now

print( "sum of smallest =", smallest( num11, num12, num13 ) + 
    smallest( num21, num22, num23 ) )
print( "sum of middle =", middle( num11, num12, num13 ) + 
    middle( num21, num22, num23 ) )
print( "sum of largest =", largest( num11, num12, num13 ) + 
    largest( num21, num22, num23 ) )
```

{:class="callout callout-info"}
> #### Note
> In the code above, to reduce the size, I used a "multiple assignment" to give the variables `num`$$xx$$ their values. You can have multiple variables at the right of the assignment operator, and an equal number of values to the left, and the first value will then go to the first variable, the second value to the second variable, etcetera. I will discuss this in more depth in Chapter <a href="#ch:tuples" data-reference-type="ref" data-reference="ch:tuples">12</a>.

The program above readable, understandable, and can already be tested.
True, the functions `smallest()`, `middle()`, and `largest()` do not
return the correct values yet. While writing the program above, you
might not even have an idea on how to write them. But you probably feel
that they could be written, and you know that you can produce code for
them later, and step by step.

So how do you do `smallest()`? Well, as I showed above, doing this with
nested `if` statements becomes a bit convoluted and unreadable (really,
don’t look at how I did it and try to write this yourself; it is pretty
hard to keep the three variables in your head while writing such a
nested `if`). Can this be approached in a more readable way?

Is it hard to determine the smallest of two numbers? No, that is really
easy:

```python
def smallest_of_two( n1, n2 ):
    if n1 < n2:
        return n1
    return n2
```

By nesting such a function, you can make a `smallest()` function that
determines the smallest of three numbers. The same can be done for
`largest()`. So the program now becomes:

```python
num11, num12, num13 = 436, 178, 992
num21, num22, num23 = 880, 543, 101

def smallest_of_two( n1, n2 ):
    if n1 < n2:
        return n1
    return n2

def largest_of_two( n1, n2 ):
    if n1 > n2:
        return n1
    return n2

def smallest( n1, n2, n3 ):
    return smallest_of_two( smallest_of_two( n1, n2 ), n3 )

def middle( n1, n2, n3 ):
    return n1 # just return something for now

def largest( n1, n2, n3 ):
    return largest_of_two( largest_of_two( n1, n2 ), n3 )

print( "sum of smallest =", smallest( num11, num12, num13 ) + 
    smallest( num21, num22, num23 ) )
print( "sum of middle =", middle( num11, num12, num13 ) + 
    middle( num21, num22, num23 ) )
print( "sum of largest =", largest( num11, num12, num13 ) + 
    largest( num21, num22, num23 ) )
```

The program now works as far as smallest numbers and largest numbers are
concerned. To complete the code, a solution must be found for the
middle. What is the middle of three numbers? It is the number that
remains if the smallest and largest are taken out. Can this be
programmed? Here I propose a `remove_two_of_three()` function. The
function first removes the smallest from three numbers, then removes the
largest of the remaining two, which is the same as the largest of the
original three. So, for an easy implementation of
`remove_two_of_three()`, I also implement functions
`remove_one_of_three()` and `remove_one_of_two()`.

```python
num11, num12, num13 = 436, 178, 992
num21, num22, num23 = 880, 543, 101

def smallest_of_two( n1, n2 ):
    if n1 < n2:
        return n1
    return n2

def largest_of_two( n1, n2 ):
    if n1 > n2:
        return n1
    return n2

def remove_one_of_three( n1, n2, n3, remove ):
    if n1 == remove:
        return n2, n3
    elif n2 == remove:
        return n1, n3
    return n1, n2

def remove_one_of_two( n1, n2, remove ):
    if n1 == remove:
        return n2
    return n1

def remove_two_of_three( n1, n2, n3, remove1, remove2 ):
    num1, num2 = remove_one_of_three( n1, n2, n3, remove1 )
    return remove_one_of_two( num1, num2, remove2 )

def smallest( n1, n2, n3 ):
    return smallest_of_two( smallest_of_two( n1, n2 ), n3 )

def middle( n1, n2, n3 ):
    return remove_two_of_three( n1, n2, n3, 
        smallest( n1, n2, n3 ), largest( n1, n2, n3 ) )

def largest( n1, n2, n3 ):
    return largest_of_two( largest_of_two( n1, n2 ), n3 )

print( "sum of smallest =", smallest( num11, num12, num13 ) + 
    smallest( num21, num22, num23 ) )
print( "sum of middle =", middle( num11, num12, num13 ) + 
    middle( num21, num22, num23 ) )
print( "sum of largest =", largest( num11, num12, num13 ) + 
    largest( num21, num22, num23 ) )
```

The program is now finished and it works. It is fairly long, but all the
functions are easy to understand, and it is also easy to understand why
the program works. It is still shorter than the original attempt, with
at least six nested `if` statements, would have been, and it is a lot
more readable.

It might be that there are different approaches for this program. With
some inventiveness, you might come up with smarter ways to determine
smallest, middle, and largest (I am not completely satisfied with my
approach for the middle). But the program works, and is understandable,
and that is the most important.

You can criticize the approach that I take in this program. For
instance, calculation of the smallest of the same three numbers takes
place twice: once to determine the smallest, and once to determine the
middle. The same holds for the largest. Can this be optimized, so that
such a determination takes place only once? Of course it can, for
instance by the introduction of two extra variables that keep track of
the smallest and largest numbers. But why would I? That would not make
the program more readable, and while it would make the program a bit
faster, I am talking nanoseconds here. For a program like this, speed is
unimportant and completely subject to readability. Let me stress again
that while learning programming, solving a problem correctly comes
first, immediately followed by solving a problem in a readable and
maintainable way. Efficiency comes much later.

What you should learn from this, is that when a program consists of a
series of problems that you find hard to solve, you should try to split
it into sub-problems or sub-goals, and solve these independently. You
can often already introduce functions for sub-problems when you set up
the program, and then for the time being fill these function templates
with something simple, like returning a constant. You can then at least
test the program. Later on, you can start filling in all the function
templates that you created.
