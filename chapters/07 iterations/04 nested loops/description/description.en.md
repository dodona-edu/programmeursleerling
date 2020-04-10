You can put a loop inside another loop.

That is a simple statement, but it is one of the hardest concepts for
students to wrap their minds around.

Let's first look at an example of a double-nested loop, i.e., a loop
which contains one other loop. Usually programmers talk about an "outer
loop" and an "inner loop." The inner loop is part of the code block for
the outer loop.

```python
for i in range( 3 ):
    print( "Entering the outer loop for i =", i )
    for j in range( 3 ):
        print( "    Entering the inner loop for j =", j )
        print( "    (i,j) = ({},{})".format( i, j ) )
        print( "    Leaving the inner loop for j =", j )
    print( "Leaving the outer loop for i =", i )
```

Study this code and its output until you fully understand it!

The code first gives `i` the value 0, and then lets `j` take on the
values 0, 1, and 2. It then gives `i` the value 1, and then lets `j`
take on the values 0, 1, and 2. Finally, it gives `i` the value 2, and
then lets `j` take on the values 0, 1, and 2. So this code runs through
all possible pairs of `(i,j)` with `i` and `j` being 0, 1, or 2.

Notice how variables for the outer loop are also accessible by the inner
loop. `i` exists in both the outer and the inner loop.

Suppose that you want to print all pairs `(i,j)` where `i` and `j` can
take on the values 0 to 3, but `j` must be higher than `i`. Code that
does that is:

```python
for i in range( 4 ):
    for j in range( i+1, 4 ):
        print( "({},{})".format( i, j ) )
```

See how I cleverly use `i` to set the range for `j`?

Write code that prints all pairs `(i,j)` where `i` and `j` can take on
the values 0 to 3, but they cannot be equal.

You can, of course, also nest `while` loops, or mix nesting `for` loops
with `while` loops.

You should be aware that when you use a `break` or `continue` in an
inner loop, it will only break out of the inner loop or continue with
the inner loop, respectively. There is no command that you can give in
an inner loop that breaks out of both the inner and outer loop
immediately.[^3]

Once you understand double-nested loops, it should come as no surpise
that you can also triple-nest loops, quadruple-nest loops, or go even
deeper. However, in practice I have seldom seen a nesting deeper than
triple-nested.

```python
for i in range( 3 ):
    for j in range( 3 ):
        for k in range( 3 ):
            print( "({},{},{})".format( i, j, k ) )
```

[^3]: Unless you use them in a function, then you can exit the function
    at any time and so interrupt both the inner and the outer loop. But
    that will follow in Chapter
    <a href="#ch:functions" data-reference-type="ref" data-reference="ch:functions">9</a>.
