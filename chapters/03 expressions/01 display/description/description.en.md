When you write an expression in the Python shell, and you run it, the
result of the expression is shown below it. For instance, if you type
the following command in the shell and press `Enter`, you see the result
$$12$$.

```python
5 + 7
```

However, as I showed in Exercise
<a href="#python.shell" data-reference-type="ref" data-reference="python.shell">[python.shell]</a>,
a program that contains the statement `5 + 7` will not produce a result
in the shell. Instead, you have to explicitly display everything that
you want to see, even if it is on the last line of the program.

So, even though this chapter is about expressions, the first thing I
need to explain is not an expression, but a function, that allows you to
display results. The function that does that is `print`. I already
showed the `print` function in Chapters
<a href="#ch:introduction" data-reference-type="ref" data-reference="ch:introduction">2</a>
and
<a href="#ch:usingpython" data-reference-type="ref" data-reference="ch:usingpython">3</a>.

The `print` function is used as follows: you write the word `print`,
followed by an opening parenthesis, followed by whatever you want to
display, followed by a closing parenthesis. For example (and I showed
this one before):

```python
print( "Hello, world!" )
```

If you run this code (by saving it into a Python file and running it in
IDLE), you will see that it displays the text "Hello, world!" in the
shell.

By the way, when referring to a function by name in a text, authors of
texts about programming often put an opening and closing parenthesis
after the name of the function, to indicate that it is a function name.
From now on, I will follow this convention. Moreover, instead of
referring to a "function," authors sometimes call it a "statement" or a
"command." However, these terms are usually used to refer to anything
that Python can execute, not just functions. I.e., an expression can
also be called a "command."

You can display multiple things with one `print()` function by putting
everything that you want to display between the parentheses with commas
in between. The `print()` function will then display all of the items,
with one space in between each pair or them. For example:

```python
print( "I", "own", "two", "apples", "and", "one", "banana" )
```

Note that the spaces in this statement are all superfluous. The
statement:

```python
print("I","own","two","apples","and","one","banana")
```

is equivalent to the previous one. You can add such spaces for
readability. You can even put spaces between the word `print` and the
opening parenthesis, but by convention, for functions (and `print()` is
a function), the opening parenthesis is placed against the function
name.

Note that you can not only use `print()` to display texts, but also to
display numbers. You can even mix them up, as the following code shows.

```python
print( "I", "own", 2, "apples", "and", 1, "banana" )
```

Display some texts of your liking using a Python program. But take note
that if you want to display text strings, you have to enclose them in
double quotes – or single quotes, those work too.
