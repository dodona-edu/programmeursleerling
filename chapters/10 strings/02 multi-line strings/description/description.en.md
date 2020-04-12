Strings in Python may span across multiple lines. This can be useful
when you have a very long string, or when you want to format the output
of the string in a certain way. Multi-line strings can be achieved in
two ways:

-   With single or double quotes, and an indication that the remainder
    of the string continues on the next line with a backslash.

-   With triple single or double quotes.

I first demonstrate how this works when you use the regular string
enclosure with one double or single quote at each end of the string:

```python
long = "I'm fed up with being treated like sheep. What's the \
point of going abroad if you're just another tourist carted \
around in buses surrounded by sweaty mindless oafs from \
Kettering and Coventry in their cloth caps and their cardigans \
and their transistor radios and their Sunday Mirrors, \
complaining about the tea - 'Oh they don't make it properly \
here, do they, not like at home' - and stopping at Majorcan \
bodegas selling fish and chips and Watney's Red Barrel and \
calamaris and two veg and sitting in their cotton frocks \
squirting Timothy White's suncream all over their puffy raw \
swollen purulent flesh 'cos they 'overdid it on the first day.'"
print( long )
```

As you can see when you run the code, Python interprets this example as
a single line of text. The backslash (`\`) can actually be included
after any Python statement to indicate that it continues on the next
line, and it can be quite useful for that, for instance when you write
long calculations.

The recommended way to write multi-line strings in Python is, however,
to use triple double or single quotes. I indicated earlier that you can
use those to write multi-line comments. Such comments are basically
large strings in the middle of your Python program, which do nothing as
they are not assigned to a variable.

Here is an example of a long string with triple double quotes:

```python
long = """And being herded into endless Hotel Miramars and 
Bellevueses and Continentales with their modern international
luxury roomettes and draught Red Barrel and swimming pools full
of fat German businessmen pretending they're acrobats forming 
pyramids and frightening the children and barging into queues 
and if you're not at your table spot on seven you miss the bowl 
of Campbell's Cream of Mushroom soup, the first item on the menu 
of International Cuisine, and every Thursday night the hotel has 
a bloody cabaret in the bar, featuring a tiny emaciated dago with
nine-inch hips and some bloated fat tart with her hair brylcreemed 
down and a big arse presenting Flamenco for Foreigners."""
print( long )
```

Note that in the first example the string was interpreted as a
continuous series of characters, while in the second example the lines
are all printed as different lines. The reason is that in the second
example an invisible character is included at the end of each line which
indicates that Python should move to the next line before continuing.
This is a so-called "newline" character, and you can actually insert it
explicitly into a string, using the code `"\n"`. This code should not be
read as a backslash and the `"n"`, but as a single newline character. By
using it, you can ensure that you print the output on multiple lines,
even if you use the backslash to indicate the continuation of the
string, as was done in the first example:

```python
long = "And then some adenoidal typists from Birmingham with\n\
flabby white legs and diarrhoea trying to pick up hairy bandy-\n\
legged wop waiters called Manuel and once a week there's an\n\
excursion to the local Roman Ruins to buy cherryade and melted\n\
ice cream and bleeding Watney's Red Barrel and one evening you\n\
visit the so called typical restaurant with local colour and\n\
atmosphere and you sit next to a party from Rhyl who keep\n\
singing 'Torremolinos, torremolinos' and complaining about the\n\
food - 'It's so greasy here, isn't it?' - and you get cornered\n\
by some drunken greengrocer from Luton with an Instamatic\n\
camera and Dr. Scholl sandals and last Tuesday's Daily Express\n\
and he drones on and on and on about how Mr. Smith should be\n\
running this country and how many languages Enoch Powell can\n\
speak and then he throws up over the Cuba Libres."
print( long )
```

If you do not want automatic newline characters in a multi-line string,
you have to use the backslash at the end of the line. Otherwise, the
second approach is the easiest to read.
