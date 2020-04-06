Typically, when things go wrong in a program, the reason is that
variables are holding values that you did not expect them to have when
writing the code. A good way of "debugging" your code (i.e., finding out
where problems are and fixing them) is printing the variable names and
values in appropriate places. For instance, the following code gives an
error when you run it.

``` python
nr1 = 5
nr2 = 4
nr3 = 5
print( nr3 / (nr1 % nr2) )
nr1 = nr1 + 1
print( nr3 / (nr1 % nr2) )
nr1 = nr1 + 1
print( nr3 / (nr1 % nr2) )
nr1 = nr1 + 1
print( nr3 / (nr1 % nr2) )
```

In this case you might see what the problem is, but suppose you do not,
how are you going to find out what is wrong? You see that the error
occurs on line 10 of the code (the last line), which means that
everything is still running okay at line 9. If you insert a new line of
code between line 9 and line 10 that prints the values of `nr1`, `nr2`,
`nr3` and perhaps also `nr1 % nr2`, you probably quickly determine what
the problem is. Adding print statements does not actually change
anything about the variables, so print statements are safe to add. A
nice fix for the problem (i.e., something else than just removing the
offending line) will be introduced in a later chapter.

Add the line suggested above, printing the variables right before the
error occurs, to the erroneous code.
