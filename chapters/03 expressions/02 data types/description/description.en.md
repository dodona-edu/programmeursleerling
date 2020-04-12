Before I can get to expressions, there is one more topic that requires
some discussion, and that is data types. Specifically, there are three
different data types that you need to be aware of at this time: strings,
integers, and floats.

### Strings

A string is a text, consisting of zero or more characters. In Python, a
string is enclosed by either double quotes, or single quotes. In
principle, it does not matter which of the two you use, i.e., `"orange"`
is equivalent to `'orange'`. However, if you have a text which contains
a single quote, if you want to avoid problems you will have to enclose
it in double quotes, i.e., `"I can't stand it"` is a legal string, while
`'I can't stand it'` is not. Vice versa for double quotes in a string,
of course.

What if a string contains both double quotes and single quotes? You can
solve that issue by putting a backslash (`\`) in front of the single or
double quote that is part of the string to tell Python to treat that
single or double quote as a character of the string rather than
something that ends the string, i.e., `'I can\'t stand it'` is a legal
string. You can see that when you try to print it:

```python
print( 'I can\'t stand it' )
```

But what if I want to put an actual backslash in a string, and that
backslash is, by chance, in front of a single or double quote? Well, I
can do the same thing for a backslash, namely put a backslash in front
of a backslash to make it a literal backslash, rather than a backslash
that changes the interpretation of the character that comes after it.
For an example, check out what the next bit of code displays (you can
type it into the Python shell).

```python
print( 'I can\\\'t stand it' )
```

If this all is a bit confusing, forget about these details for now, as I
will come back to them in a later chapter. For now, just remember that a
string is a text, enclosed by either single or double quotes. A string
might be of any length, including zero characters long.

Be careful that you only use "straight" single or double quotes in your
Python programs, and not "rounded" ones. Word processors are in the
habit of changing your straight quotes into rounded quotes, and Python
does not recognize those. Text editors will not do that, but should you,
for some reason, copy code to and from a word processor, your quotes
might get changed. Watch out for that.

### Integers

Integers are whole numbers, which can be positive or negative (or zero).
There is a certain maximum size that integers can become, which depends
on the kind of computer and operating system you are running. For most
purposes, however, you will not run into those boundaries. Python is not
like those calculators with a 10-digit display that cannot use numbers
higher than 10 billion.

There are different ways of writing integers that result in the same
value. `1` is the same as `+1` (there are other ways than these to write
the value `1`, but these follow in a later chapter). So both
`print( 1 )` and `print( +1 )` produce the same outcome. This is
different for strings, of course. The string `"1"` is not the same as
the string `"+1"`.

When you use integers in Python, you cannot write them with "thousands
separators" (commas in English) to make them more readable. I.e., the
number one billion should be written as `1000000000` rather than
`1,000,000,000`.

Check out the following code and think about what it will display when
you run it. Then copy it to the Python shell and run it.

```python
print( 1,000,000,000 )
```

If your prediction of what this code would do was not correct, find out
why it produces this result.

### Floats

Floats, or "floating-point numbers," are numbers with decimals. For
instance, `3.14159265` is a float. Note that you have to use a period as
the decimal separator. Many countries use a comma as the decimal
separator, but Python uses the convention of English-speaking countries
and uses the period.

If there is an integer that for some reason you want to use as a float,
you can do so by adding `.0` to it. I.e., `13` is an integer, while
`13.0` is a float. Still, they represent the same value, and if you use
Python to compare them (which I will get to in a short while), Python
will tell you that they are the same value.

Just like with integers, there are certain maximum boundaries for
floats, and there is also a maximum precision. You are unlikely to ever
reach those maximum boundaries, as Python will switch over to scientific
notation when the numbers get very big, but if you use Python to do very
precise calculations, you might run into problems with precision. That
is unlikely to happen for most applications, but if you are a physicist
whose calculations involve huge numbers of particles on the molecular or
quantum level, it is something to be aware of.

Note that due to the way that Python stores floats, certain numbers
cannot be expressed exactly. For instance, the statement
`print( (431 / 100) * 100 )` prints as answer 430.99999999999994, and
not 431 as you might expect. If you know that the outcome of a
floating-point calculation must be an integer, then you best make sure
that you round the outcome to the nearest whole number. You can use the
`round()` function for that, which will be explained in Chapter
<a href="#ch:simplefunctions" data-reference-type="ref" data-reference="ch:simplefunctions">6</a>.
