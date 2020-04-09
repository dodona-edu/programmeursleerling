You might have noticed that in my example code I use white spaces a lot.
For instance, for parentheses attached to functions, I almost always
have a white space after the opening parenthesis and before the closing
parenthesis. In calculations, I often have white spaces around operators
if that makes the calculations better readable. I also often insert
empty lines in my code to make it more readable, and consistently use
four spaces as indentations.

Most of these things are just "style." The white spaces next to the
parentheses and around operators are not necessary, Python understands
the code just as well when they are gone. These four statements are all
equivalent:

```python
# All equivalent statements
print( 2 + 3 )
print(2+3)
print( 2+3)
print       (       2       +       3       )
```

Attaching the opening parenthesis to a function is something that almost
every programmer does, but for the rest, styles of placing white spaces
differ between programmers (my style of placing a space before the
closing parenthesis is rare). You can choose your own style in this
respect, you do not need to follow mine. But I recommend that you use
your chosen style consistently, which will make your code more readable
even for programmers who use a different style.

Note that in the code above there is a hash mark (\#) on the first line,
with a text after that which explains some details of the code. The line
with the hash mark is a comment line: whenever you put a hash mark in
your code (except when it is within a string, of course), everything to
the right of the hash mark for the remainder of the line is commentary,
which Python ignores. You can use comments to clarify your code, if such
clarification is needed. More details on providing comments to code I
will give in a later chapter.
