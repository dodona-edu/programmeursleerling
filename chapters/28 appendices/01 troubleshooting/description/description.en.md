### When I run code I get an ImportError

Check the name of the file that your code tries to import. If it is
supposed to be one of the standard Python libraries, you probably made a
spelling mistake in the name. Either that, or you added `.py` to the
name – you should not do that. If the error concerns `pcinput` or
`pcmaze`, then probably you either did not build these files (check
Appendix
<a href="#ch:pcinput" data-reference-type="ref" data-reference="ch:pcinput">31</a>
or
<a href="#ch:pcmaze" data-reference-type="ref" data-reference="ch:pcmaze">32</a>
to solve the problem), or you placed them in a location that Python has
no access to. In the last case, make sure you copy them to the same
place as where you keep your Python programs.

### I get a FileNotFoundError: [Errno 2]

You try to open a file that Python cannot find. You might have forgotten
to include the complete pathname in the file name, or you think the file
is located in the current directory while actually it is not. Or maybe
your code tries to use one of the standard test files that I use for the
book, and you do not have those yet. If that is the case, check Appendix
<a href="#ch:testtextfiles" data-reference-type="ref" data-reference="ch:testtextfiles">33</a>
to learn how to make them.

### I get a SyntaxError but I have no idea what I did wrong

When one or more syntax errors are reported, you should try to solve the
one reported first. Further errors are often caused by the first one.
The line of code where Python discovered the error is reported with the
error. Check that line. Also check the line above it: it might very well
happen that you made an error in a line of code, but Python only notices
it when it processes the next line. Syntax highlighting may also give an
indication of where you made your mistake. Common syntax errors that
beginning programmers make are forgetting to include a colon (`:`) at
the end of an `if`, `while`, or `for` statement, misspelling the name of
variables that they created, or making errors in indentation.

### I get a SyntaxError that reports a "Non-UTF-8 code"

You have used a character in your program that Python cannot process.
For instance, you might have placed your own name in the code (maybe
even only in a comment), and your name is spelled with a special
character that is not directly found on the keyboard. Stick to
characters that are found on the US keyboard. It is not that you cannot
include special characters in your code, but the rules for doing that
are explained in later chapters in this book.

### I get a curious error even when running the example code

Make sure that you use Python version 3.4 or later. The code was written
with Python 3.4, and I have noticed that some code elements do not work
correctly with earlier versions of Python.

### When I run my program it doesn't do anything

Maybe you built an endless loop in your program, so the program is
actually working but never getting to the point where it produces
output. Check your loops. Sometimes it is helpful to include a `print()`
statement at the start of your program, just to see that the program
actually has started. `print()` statements in the code might also help
to discover where it gets stuck.

### I defined a function (or class) in my program, but it seems Python cannot access it

Make sure that you spelled your call to the function (or class)
correctly. Remember that Python is case sensitive! If the spelling seems
to be correct, make sure that you have not created a variable with the
same name as the function (or class). If you did, this will definitely
destroy the possibilities of Python to access your function (or class).

### I have been staring at my program for hours and can't get it to work

Sometimes it is good to take a break. Put the program away, go home,
play some games, exercise, take a shower, anything. Get back to it
tomorrow. Ask any programmer: sometimes you get stuck and cannot resolve
a problem, for which the solution is immediately clear to you when you
come in the next day. What might also help is get someone else in and
explain your problem to them. Often, during such an explanation, you
suddenly see what you were doing wrong all this time. What you
definitely should *not* do, however, is continue writing your program
without resolving the problem. You will only create a bigger mess. A
much better idea would be to make a copy of your program and then
actually remove/simplify code until the program starts working. That at
least gives you an indication where you have to look for the error.
