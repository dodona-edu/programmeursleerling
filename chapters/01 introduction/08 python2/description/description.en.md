Different versions of Python exist. At the moment of creating this book,
the most popular versions are Python 2 and Python 3. Python 3 is, as can
be expected, an update of Python 2. Python 2 programs are,
unfortunately, not completely compatible with Python 3. Since a lot of
Python 2 code is still in use, Python 2 is still an active language, and
still being maintained.

The reason why Python 3 was created is to resolve a number of
inconsistencies and idiosyncrasies in the Python 2 language. For people
new to programming, this is a big plus, because there are less "weird"
language elements they need to learn and understand if they choose
Python 3 instead of Python 2.

To give an example, when you calculate $$7/4$$ in Python 2, the answer is
$$1$$, and not $$1.75$$ as you might expect. The reason is that both $$7$$ and
$$4$$ are whole numbers ("integers"), and therefore the result of their
division is a whole number. If you want to make sure that the result is
$$1.75$$, you must make at least one of the numbers involved a
floating-point number. Therefore, $$7.0/4$$ gives the result $$1.75$$. This
is how almost all computer languages do calculations. Naturally, for
people who are not familiar with programming computers, this is
counter-intuitive. Python 3 has resolved this issue, and automatically
does the floating-point conversion when a floating-point result would be
expected, i.e., in Python 3, $$7/4$$ gives the result $$1.75$$. Many Python
2 programs, however, are written with the assumption that
integer-division rounds down, which means that, when you run them as
Python 3 programs, they no longer give the desired results. Thus, Python
2 and Python 3 are not compatible.

Since Python 3 is more intuitive than Python 2, and since nowadays most
Python programs and modules have been converted to Python 3, this book
is written for Python 3. If you ever have to revert back to Python 2, it
is not hard to make the change. An overview of the differences between
Python 2 and Python 3 is given in Appendix
<a href="#ch:python2" data-reference-type="ref" data-reference="ch:python2">30</a>
(which is not a complete overview, but contains all the differences that
I am aware of). If you are only using Python 3, you can ignore this
appendix. However, considering how often I see the question "What
exactly are the differences between Python 2 and Python 3?," and how
hard it seems to be to find an answer to that question, I thought it
prudent to add it.
