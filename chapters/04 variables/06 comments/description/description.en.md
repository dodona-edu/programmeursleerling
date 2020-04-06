Since the code that you have to write has now increased to more than
five lines or so, it has become sufficiently complex to warrant
discussing the use of comments. Comments are texts in code that Python
ignores, but that explain parts of the code. Comments are not only
useful to other people which might need to use or change your code, but
also to yourself, as you may need to change your own code some time
after you wrote it and you might not remember exactly what you did.

There are two main ways to include comments in Python code. The first is
to use a hash mark (\#), which turns everything to the right of the hash
mark on the line into commentary (of course, this is only the case if
the hash mark is not part of a string). The second is to use triple
double-quotes or triple single-quotes to indicate the start and end of
some commentary, which may be spread over multiple lines. In this case,
the starting triple quotes should always be at the start of a line, and
you cannot use this way of commenting in an indented code block. The
reason is that you are basically placing a multi-line string in your
code (more on this in Chapter
<a href="#ch:strings" data-reference-type="ref" data-reference="ch:strings">11</a>).

Learn more about comments by studying the code below.

```python
# comment: insert your code here.
# BTW: Have you noticed that everything right of the hash mark 
print( "Something..." ) # is ignored by your python interpreter?
print( "and something else.." ) # Use this to comment your code!
"""Another way of commenting on your code is via triple quotes 
-- these can be distributed over multiple """ # lines
'''which can also be done with single quotes''' # but be careful 
# with there being quotes IN your comments when you use this 
# multi-line method
print( "Done." )
```
