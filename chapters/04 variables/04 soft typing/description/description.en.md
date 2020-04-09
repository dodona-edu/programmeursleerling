All variables have a data type. In many programming languages, the type
of a variable is given when the variable is first created. For instance,
in C++, when you create a variable you declare the type in front of it,
like so:

```python
int secs_per_week = 7 * 24 * 60 * 60;
```

This is called "hard typing," and it has the advantage that if you
create a variable that you intend to be of a certain type, but then
assign it a value of a different type, the program can announce that you
made a mistake. This avoids some annoying and confusing errors that
might occur.

In Python, you do not "declare" the type of a variable, but a variable
still has a type, namely the type of the value that was assigned to it.
This entails that if you assign a new value to a variable, its type
might change. This is called "soft typing." (Note: I am personally of
the opinion that Python would be an even better language to teach people
programming if it had hard typing instead of soft typing, and I am not
alone in that opinion, but Guido van Rossum, the original creator of
Python, disagrees.)

The types that you have seen until now are integer, float, and string.
You can use the function `type()` to see what the type of a variable is.

```python
a = 3
print( type( a ) )
a = 3.0
print( type( a ) )
a = "3.0"
print( type( a ) )
```

Since variables have a type, the effect of operators might change
depending on the types of the variables involved. For instance, in the
following code, the addition operator ($$+$$) is used twice, but its
effect changes due to the types of the variables involved.

```python
a = 1
b = 4
c = "1"
d = "4"
print( a + b )
print( c + d )
```

Since `a` and `b` are both numbers, for `a + b` the addition operator is
a numerical addition. Since `c` and `d` are both strings, the addition
operator for `c + d` is the string concatenation.

In the code above, what would happen if you try to print `a + c`? If you
do not know, try it.

What does the code given below display? First think about it, then run
the code, and make sure that you understand what happens.

```python
name = "John Cleese"
print( "name" )
```

Change the code above so that it displays the name of a famous member of
Monty Python.
