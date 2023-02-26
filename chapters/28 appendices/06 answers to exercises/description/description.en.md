This appendix provides answers to most of the exercises. They are also
available in file format from <http://www.spronck.net/pythonbook>{:target="_blank"}.

Note that it is useless to look up answers to exercises if you have not
spent a significant amount of time trying to solve the exercises. You
can only learn programming by doing. Only use the answers to compare
them with your own, completed solutions, or as a final resort should you
have no idea how to solve a problem. However, if you cannot solve a
problem, it is usually better to return to an earlier part of the book
that contains information that you evidently did not understand or
forgot about.

Note that very often, the answers given here are only one of many
possible ways to solve a problem. If you have found a different way to
solve a problem, that might be just fine, though make sure you test your
answer extensively to ensure that it is correct.

Moreover, while the answers given here are usually efficient, efficiency
is not the first goal when writing code. You should first make sure that
your code solves the problem at hand, before you look into making the
code more efficient. Readability and maintainability are far more
important than efficiency.

### Chapter 2

#### Answer 1.1

A straightforward sorting procedure that first identifies the highest
card, then the next highest card, then the lowest-but-one, and then the
lowest card, needs six comparisons. You could perform it, for instance,
as follows:

Number the cards from 1 to 4, left to right. The number is tied to the
spot where the card is, i.e., when you switch two cards, they exchange
numbers. Compare cards 1 and 2, and switch them if 1 is higher than 2.
Compare cards 2 and 3, and switch them if 2 is higher than 3. Compare
cards 3 and 4, and switch them if 3 is higher than 4. Now the highest
card will be the number 4. Then, compare cards 1 and 2 again, and switch
them if 1 is higher than 2. Compare cards 2 and 3 again, and switch them
if 2 is higher than 3. Now the next-highest card is number 3. Finally,
compare cards 1 and 2 and switch them if 1 is higher than 2. You have
now sorted the four cards, with six comparisons.

To do it with less comparisons, you need a procedure that is a bit more
complex. Start again by numbering the cards from 1 to 4. Compare cards 1
and 2, and switch them if 1 is higher than 2. Compare cards 3 and 4, and
switch them if 3 is higher than 4. Compare cards 1 and 3. If 1 is higher
than 3, you switch card 1 and 3, and also card 2 and 4. The lowest card
is now in spot 1, and you also know that card 3 is lower than card 4.
Now compare cards 2 and 3. If 2 is lower than 3, you are done, needing
only four comparisons. If 2 is higher than 3, you switch 2 and 3. You
now still have to compare cards 3 and 4, and switch them if 3 is higher
than 4, but then you are done, needing only five comparisons. So you can
do the sorting with a guaranteed maximum of five comparisons.

You might think that you can be smart and, after comparing 1 and 2 and
maybe switching them, and comparing 3 and 4 and maybe switching them, to
compare 2 and 3, because if at that point 2 is smaller than 3, you only
need three comparisons. However, should at that point 2 be higher than
3, if you are unlucky you will need six comparisons in total.

For those new to programming, the more efficient procedure which only
needs five comparisons is quite hard to design, so do not get
discouraged if you cannot come up with it. It is more important that you
solve a task, than that you solve it in the most efficient manner.

#### Answer 1.2

You should draw four boxes on a piece of paper, number them, and put
each of the cards in one of the boxes. Tell the person who is following
the instructions that "compare the card in box $$x$$ with the card in box
$$y$$" means that they should ask the processor to take up those cards,
look at them, put them back in the same spots where they were taken
from, and then indicate which of the two is the higher card. Then you
can give them instructions for the simple, six-comparisons procedure
outlined above:

1.  Compare the card in box 1 with the card in box 2. If the card in box
    1 is higher than the card in box 2, switch these two cards.

2.  Compare the card in box 2 with the card in box 3. If the card in box
    2 is higher than the card in box 3, switch these two cards.

3.  Compare the card in box 3 with the card in box 4. If the card in box
    3 is higher than the card in box 4, switch these two cards.

4.  Compare the card in box 1 with the card in box 2. If the card in box
    1 is higher than the card in box 2, switch these two cards.

5.  Compare the card in box 2 with the card in box 3. If the card in box
    2 is higher than the card in box 3, switch these two cards.

6.  Compare the card in box 1 with the card in box 2. If the card in box
    1 is higher than the card in box 2, switch these two cards.

Using the idea of drawing boxes that you have numbered to refer to the
cards put in those boxes is similar to using variables in a computer
program. Variables will be explained in one of the early chapters.
Trying to write instructions for the more efficient procedure outlined
above is harder, because you need nested conditions and an early escape.

### Chapter 3

#### Answer 2.1

You now have Python running on your computer. Congratulations!

#### Answer 2.2

You will see nothing in the shell (apart from a display of the word
`RESTART` that you always see when running a program). $$7/4$$ is a legal
Python statement, so the program will not give an error. The program
just calculates $$7/4$$, but does not display the result using a print
statement, so the program does not show $$1.75$$. The shell, however,
displays the result of running the program. But since a program has no
result by itself, there is nothing for the shell to display either. So
you see nothing.

### Chapter 4

#### Answer 3.1

```python
print( 60 * (0.6 * 24.95 + 0.75) + (3 - 0.75) )
```

#### Answer 3.2

Each of the lines should be either `print( "A message" )` or
`print( 'A message' )`. The error in the first line is that it ends in a
period. That period should be removed. The error in the second line is
that it contains something that is supposed to be a string, but starts
with a double quote while it ends with a single quote. Either the double
quote should become a single quote, or the single quote should become a
double quote. The third line is actually syntactically correct, but
probably it was meant to be `print( 'A message' )`, so the `f"` should
be removed.

#### Answer 3.3

```python
print( 1/0 )
```

#### Answer 3.4

The problem is that there is one closing parenthesis missing in the
first line of code. I actually deleted the closing parenthesis that
should be right of the $$6$$, but you cannot know that; you can only count
the parentheses in the first statement and see that there is one less
closing parenthesis than there are opening parentheses.

The confusing part of this error message is that it says that the error
is in the second line of code. The second line of the code, however, is
fine. The reason is that since Python has not seen the last required
closing parenthesis on the first line, it starts looking for it on the
second line. And while doing that, it notices that something is going
wrong, and it reports the error. Basically, while trying to process the
second line, Python finds that it cannot do that, so it indicates that
there is an error with the second line.

You will occasionally encounter this in your own code: an error is
reported for a certain line of code, but the error is actually made in
one of the previous lines. Such errors often encompass the absence of a
required parenthesis or single or double quote. Keep this in mind.

#### Answer 3.5

```python
print( str( (14 + 535) % 24 ) + ".00" )
```

### Chapter 5

#### Answer 4.1

```python
# This program calculates the average of three variables,
# var1, var2, and var3
var1 = 12.83
var2 = 99.99
var3 = 0.12
average = (var1 + var2 + var3) / 3 # Calculate the average
print( average ) # May look a bit ugly, but we might make this
# look a bit better when we have learned about formatting
```

#### Answer 4.2

```python
pi = 3.14159
radius = 12
print( "The surface area of a circle with radius",
    radius, "is", pi * radius * radius )
```

#### Answer 4.3

```python
CENTS_IN_DOLLAR = 100
CENTS_IN_QUARTER = 25
CENTS_IN_DIME = 10
CENTS_IN_NICKEL = 5

amount = 1156
cents = amount

dollars = int( cents / CENTS_IN_DOLLAR )
cents -= dollars * CENTS_IN_DOLLAR
quarters = int( cents / CENTS_IN_QUARTER )
cents -= quarters * CENTS_IN_QUARTER
dimes = int( cents / CENTS_IN_DIME )
cents -= dimes * CENTS_IN_DIME
nickels = int( cents / CENTS_IN_NICKEL )
cents -= nickels * CENTS_IN_NICKEL
cents = int( cents )

print( amount / CENTS_IN_DOLLAR, "consists of:" )
print( "Dollars:", dollars )
print( "Quarters:", quarters )
print( "Dimes:", dimes )
print( "Nickels:", nickels )
print( "Pennies:", cents )
```

#### Answer 4.4

```python
a = 17
b = 23
print( "a =", a, "and b =", b )
a += b
b = a - b
a -= b
print( "a =", a, "and b =", b )
```

### Chapter 6

#### Answer 5.1

```python
s = input( "Enter a string: " )
print( "You entered", len( s ), "characters" )
```

#### Answer 5.2

```python
from pcinput import getFloat
from math import sqrt

side1 = getFloat( "Please enter the length of the first side: " )
side2 = getFloat( "Please enter the length of the second side: ")
side3 = sqrt( side1 * side1 + side2 * side2 )
print( "The length of the diagonal is {:.3f}.".format( side3 ) )
```

#### Answer 5.3

```python
from pcinput import getFloat

num1 = getFloat( "Please enter number 1: " )
num2 = getFloat( "Please enter number 2: " )
num3 = getFloat( "Please enter number 3: " )

print( "The largest is", max( num1, num2, num3 ) )
print( "The smallest is", min( num1, num2, num3 ) )
print( "The average is", round( (num1 + num2 + num3)/3, 2 ) )
```

#### Answer 5.4

```python
from math import exp

s = "e to the power of {:2d} is {:>9.5f}"
print( s.format( -1, exp( -1 ) ) )
print( s.format( 0, exp( 0 ) ) )
print( s.format( 1, exp( 1 ) ) )
print( s.format( 2, exp( 2 ) ) )
print( s.format( 3, exp( 3 ) ) )
```

#### Answer 5.5

```python
from random import random

print( "A random integer between 1 and 10 is",
    1 + int( random() * 10 ) )
```

### Chapter 7

#### Answer 6.1

```python
from pcinput import getFloat

grade = getFloat( "Please enter a grade: " )
check = int( grade * 10 )
if grade < 0 or grade > 10:
    print( "Grades have to be in the range 0 to 10." )
elif check%5 != 0 or check != grade*10:
    print( "Grades should be rounded to the nearest half point.")
elif grade >= 8.5:
    print( "Grade A" )
elif grade >= 7.5:
    print( "Grade B" )
elif grade >= 6.5:
    print( "Grade C" )
elif grade >= 5.5:
    print( "Grade D" )
else:
    print( "Grade F" )
```

#### Answer 6.2

The grade will always be "D" or "F," as the tests are placed in the
incorrect order. E.g., if score is 85, then it is not only greater than
80.0, but also greater than 60.0, so that the grade becomes "D."

#### Answer 6.3

```python
from pcinput import getString

s = getString( "Please enter a string: " )
count = 0
if ("a" in s) or ("A" in s):
    count += 1
if ("e" in s) or ("E" in s):
    count += 1
if ("i" in s) or ("I" in s):
    count += 1
if ("o" in s) or ("O" in s):
    count += 1
if ("u" in s) or ("U" in s):
    count += 1

if count == 0:
    print( "There are no vowels in the string." )
elif count == 1:
    print( "There is only one different vowel in the string." )
else:
    print( "There are", count, "different vowels in the string.")
```

#### Answer 6.4

```python
from pcinput import getFloat
from math import sqrt

a = getFloat( "A: " )
b = getFloat( "B: " )
c = getFloat( "C: " )

if a == 0:
    if b == 0:
        print( "There is not even an unknown in this equation!" )
    else:
        print( "There is one solution, namely", -c/b )
else:
    discriminant = b*b - 4*a*c
    if discriminant < 0:
        print( "There are no solutions" )
    elif discriminant == 0:
        print( "There is one solution, namely", -b/(2*a) )
    else:
        print( "There are two solutions, namely",
                (-b+sqrt(discriminant))/(2*a), "and",
                (-b-sqrt(discriminant))/(2*a) )
```

### Chapter 8

#### Answer 7.1

```python
from pcinput import getInteger

num = getInteger( "Give a number: " )
i = 1
while i <= 10:
    print( i, "*", num, "=", i*num )
    i += 1
```

#### Answer 7.2

```python
from pcinput import getInteger

num = getInteger( "Give a number: " )
for i in range( 1, 11 ):
    print( i, "*", num, "=", i*num )
```

#### Answer 7.3

```python
from pcinput import getInteger

TOTAL = 10
largest = 0
smallest = 0
div3 = 0

for i in range( TOTAL ):
    num = getInteger( "Please enter number "+str( i+1 )+": " )
    if num%3 == 0:
        div3 += 1
    if i == 0:
        smallest = num
        largest = num
        continue
    if num < smallest:
        smallest = num
    if num > largest:
        largest = num

print( "Smallest is", smallest )
print( "Largest is", largest )
print( "Dividable by 3 is", div3 )
```

#### Answer 7.4

```python
bottles = 10
s = "s"

while bottles != "no":
    print( "{0} bottle{1} of beer on the wall, "\
        "{0} bottle{1} of beer.".format( bottles, s ) )
    bottles -= 1
    if bottles == 1:
        s = ""
    elif bottles == 0:
        s = "s"
        bottles = "no"
    print( "Take one down, pass it around, {} bottle{} "\
        "of beer on the wall.".format( bottles, s ) )
```

The backslash (`\`) at the end of two of the strings in this code
concatenates the string on the next line to the string after which the
backslash is found. I use that feature here to make the code fit in the
box. Use of the backslash to allow code to span multiple lines is
discussed in Chapter
11.
You do not need it at this time: you can just put the whole `print()`
statement on one long line.

#### Answer 7.5

```python
num1 = 0
num2 = 1
print( 1, end=" " )

while True:
    num3 = num1 + num2
    if num3 > 1000:
        break
    print( num3, end=" " )
    num1 = num2
    num2 = num3
```

#### Answer 7.6

```python
from pcinput import getString

word1 = getString( "Give word 1: " )
word2 = getString( "Give word 2: " )
common = ""
for letter in word1:
    if (letter in word2) and (letter not in common):
        common += letter
if common == "":
    print( "The words share no characters." )
else:
    print( "The words have the following in common:", common )
```

#### Answer 7.7

```python
from random import random

DARTS = 100000
hits = 0
for i in range( DARTS ):
    x = random()
    y = random()
    if x*x + y*y < 1:
        hits += 1

print( "A reasonable approximation of pi is", 4 * hits / DARTS )
```

#### Answer 7.8

```python
from random import randint
from pcinput import getInteger

answer = randint( 1, 1000 )
count = 0

while True:
    guess = getInteger( "What is your guess? " )
    if guess < 1 or guess > 1000:
        print( "Your guess should be between 1 and 1000" )
        continue
    count += 1
    if guess < answer:
        print( "Higher" )
    elif guess > answer:
        print( "Lower" )
    else:
        print( "You guessed it!" )
        break

if count == 1:
    print( "You needed only one guess. Lucky bastard." )
else:
    print( "You needed", count, "guesses." )
```

#### Answer 7.9

```python
from pcinput import getLetter
from sys import exit

count = 0
lowest = 0
highest = 1001
print( "Take a number in mind between 1 and 1000." )

while True:
    guess = int( (lowest + highest) / 2 )
    count += 1
    prompt = "I guess "+str( guess )+". Is your number"+\
        " (L)ower or (H)igher, or is this (C)orrect? "
    response = getLetter( prompt )
    if response == "C":
        break
    elif response == "L":
        highest = guess
    elif response =="H":
        lowest = guess
    else:
        print( "Please enter H, L, or C." )
        continue
    if lowest >= highest-1:
        print( "You must have made a mistake,",
            "because you said that the answer is higher than",
            lowest, "but also lower than", highest )
        print( "I quit this game" )
        exit()

if count == 1:
    print( "I needed only one guess! I must be a mind reader." )
else:
    print( "I needed", count, "guesses." )
```

#### Answer 7.10

```python
from pcinput import getInteger

num = getInteger( "Please enter a number: " )
if num < 2:
    print( num, "is not prime" )
else:
    i = 2
    while i*i <= num:
        if num%i == 0:
            print( num, "is not prime" )
            break
        i += 1
    else:
        print( num, "is prime" )
```

There is a small trick in this code to speed up the calculation
enormously. The code only tests dividers up to the square root of `num`
(i.e., it tests up to the point that `i*i > num`). The reason that it
does this, is that if there is a number bigger than the square root of
`num` that divides it, there must necessarily also be one smaller than
that square root. For instance, if the number is 21, the square root is
between 4 and 5. So the algorithm only tests numbers up to 4. There is a
divider for 21 higher than 4, namely 7. But that means there must also
be one lower than (or equal to) 4, and indeed, there is one, namely 3.
This is a gigantic speedup compared to testing all numbers up to `num`;
for instance, if `num` is somewhere in the neighborhood of 1 million,
and is prime, you would need to test about 1 million numbers if you test
all of them up to `num`, while this particular algorithm would only test
about one thousand.

If you found this trick, great! If not, don't worry: as long as your
code works, you are doing just fine. The hard part is getting the code
to work in the first place. As long as you accomplish that, you are well
under way to becoming a great programmer.

One final note on this code: you should test it extensively! It is very
easy to go wrong on particular numbers. In this case, make sure you test
a negative number, zero, 1 (which all three should be reported as not
prime), 2 (which is the lowest prime number and the only even one), 3
(which is the lowest odd prime), several not-prime numbers, several
prime numbers, and numbers which are the square of a prime. Even better,
if you can write a for loop around your code that tests all numbers
between, for instance, -10 and 100, then you are really doing an
extensive test of your code.

#### Answer 7.11

```python
num = 9
print( ". |", end="" )
for i in range( 1, num+1 ):
    print( "{:>3}".format( i ), end="" )
print()
for i in range( 3*(num+1) ):
    print( "-", end="" )
print()
for i in range( 1, num+1 ):
    print( i, "|", end="" )
    for j in range( 1, num+1 ):
        print( "{:>3}".format( i*j ), end="" )
    print()
```

#### Answer 7.12

```python
for i in range( 1, 101 ):
    for j in range( 1, i ):
        for k in range( j, i ):
            if j*j + k*k == i:
                print( "{} = {}**2 + {}**2".format( i, j, k ) )
```

A more efficient version of this algorithm is:

```python
from math import sqrt

for i in range( 1, 101 ):
    for j in range( 1, int( sqrt( i ) )+1 ):
        for k in range( j, int( sqrt( i ) )+1 ):
            if j*j + k*k == i:
                print( "{} = {}**2 + {}**2".format( i, j, k ) )
```

#### Answer 7.13

```python
from random import randint

TRIALS = 10000
DICE = 5
success = 0

for i in range( TRIALS ):
    lastdie = 0
    for j in range( DICE ):
        roll = randint( 1, 6 )
        if roll < lastdie:
            break
        lastdie = roll
    else:
        success += 1

print( "The probability of an increasing sequence",
    "of five die rolls is {:.3f}".format( success/TRIALS ) )
```

#### Answer 7.14

```python
for A in range( 1, 10 ):
    for B in range( 10 ):
        if B == A:
            continue
        for C in range( 10 ):
            if C == A or C == B:
                continue
            for D in range( 1, 10 ):
                if D == A or D == B or D == C:
                    continue
                num1 = 1000*A + 100*B + 10*C + D
                num2 = 1000*D + 100*C + 10*B + A
                if num1 * 4 == num2:
                    print( "A={}, B={}, C={}, D={}".format(
                        A, B, C, D ) )
```

The program will generate all combinations of A, B, C, and D that solve
the puzzle. In this case there is only one, but the program continues
seeking for more solutions until it has tested all possibilities.
Fortunately, that process is very fast. If you want to stop the program
once it has found a solution, the best approach is to put most of it in
a function and return from that function as soon as a solution is found.
Creating your own functions is discussed in the next chapter.

#### Answer 7.15

```python
PIRATES = 5
coconuts = 0
while True:
    coconuts += 1
    pile = coconuts
    for i in range( PIRATES ):
        if pile % PIRATES != 1:
            break
        pile = (PIRATES-1) * int( (pile - 1) / PIRATES )
    if pile % PIRATES == 1:
        break
print( coconuts )
```

This solution start with zero coconuts and keeps adding coconuts to the
pile until the pile is of a size whereby it can let each pirate take his
share leaving one coconut, removing the share from the pile, and
removing the remaining coconut. Testing whether a single coconut remains
after division is done using the modulo operator. After all pirates took
their share, the problem is solved if there again would be one coconut
remaining when the pile is equally divided amongst the pirates.

Isn't it a bit surprising that you can solve a problem for which the
description is so long in so few lines of code?

#### Answer 7.16

First I give the solution that simulates each Triangle Crawler
separately. The advantage of coding it like this is that it is not hard
to accomplish. The disadvantage is that this code is rather slow. It
should be pretty easy to understand how this solution works:

```python
from random import randint

NUMCRAWLERS = 100000
totalage = NUMCRAWLERS # They all live at least one day

for i in range( NUMCRAWLERS ):
    if randint( 0, 2 ): # Don't die on first day
        totalage += 1
        while randint( 0, 1 ): # Don't die on following day
            totalage += 1

print( "{:.2f}".format( totalage / NUMCRAWLERS ) )
```

The second solution considers the population as one big whole, and
simply divides it up into chunks. The first day, it takes out a chunk
the size of a third of the population, adds to the total age the fact
that this chunk only lived for one day, and lets the rest remain. On the
second day, it takes out half the population, and adds to the total age
that those lived for two days. On the third day, it again takes out half
of the remainder, and adds up that those lived three days. This
continues until no Crawlers remain.

It should be noted that often there will be a Crawler remaining which
could not be divided (as a Crawler either survives or dies, but it
cannot be Schrödinger's Cat). Such a Crawler is assigned randomly to the
group that dies or the group that survives. You can see that this code
can deal with huge numbers of Triangle Crawlers without problems.

```python
from random import randint

NUMCRAWLERS = 1000000000
num = NUMCRAWLERS
die = int( num / 3 )
if NUMCRAWLERS % 3:
    if randint( 0, NUMCRAWLERS % 3 ): # Remaining on day 1
        die += 1
totalage = die # Day-1 deaths added to totalage
num -= die

age = 2
while num > 0:
    die = int( num / 2 )
    num -= die # Kill off half the population
    if die != num: # There is a single remaining
        if randint( 0, 1 ): # Decide on kill of single
            die, num = num, die # swap values
    totalage += die * age
    age += 1

print( "{:.2f}".format( totalage / NUMCRAWLERS ) )
```

Finally, I present a solution that I did not suggest, but that works
great. It is very brief, incredibly fast, and gives an almost exact
answer. It simply calculates

$$\frac{1}{3} + \frac{2}{3}(\frac{1}{2}(2 + \frac{1}{2}(3 + \frac{1}{2}(4 + \frac{1}{2}(5 + \hellip) ) ) ) )$$

for a limited number of terms, in this case 100, which is plenty to get
a highly accurate approximation. Of course, this a calculation rather
than a simulation, but it is the mathematical expression that you were
actually asked to solve.

```python
estimate = 1/3
remainder = 2/3
for days in range( 2, 101 ):
    remainder /= 2
    estimate += remainder * days
print( "{:.2f}".format( estimate ) )
```

By the way, the exact answer is $$2\frac{1}{3}$$ days; an approximation
should give 2.33 or 2.34.

### Chapter 9

#### Answer 8.1

```python
from pcinput import getInteger

# multiplicationtable gets an integer as parameter.
# It prints the multiplication table for that integer.
def multiplicationtable( n ):
    i = 1
    while i <= 10:
        print( i, "*", n, "=", i*n )
        i += 1

num = getInteger( "Give a number: " )
multiplicationtable( num )
```

#### Answer 8.2

```python
from pcinput import getString

# commoncharacters gets two strings as parameters.
# It returns the number of characters that they have in common.
def commoncharacters( w1, w2 ):
    common = ""
    for letter in w1:
        if (letter in w2) and (letter not in common):
            common += letter
    return len( common )

word1 = getString( "Give word 1: " )
word2 = getString( "Give word 2: " )

num = commoncharacters( word1, word2 )
if num <= 0:
    print( "The words share no characters." )
elif num == 1:
    print( "The words have one character in common" )
else:
    print( "The words have", num, "characters in common")
```

#### Answer 8.3

```python
# The function gregoryLeibnitz approximates pi using the Gregory-
# Leibnitz series. It gets one parameter, which is an integer
# that indicates how many terms are calculated. It returns the
# approximation as a float.
def gregoryLeibnitz( num ):
    appr = 0
    for i in range( num ):
        if i%2 == 0:
            appr += 1/(1 + i*2)
        else:
            appr -= 1/(1 + i*2)
    return 4*appr

print( gregoryLeibnitz( 50 ) )
```

#### Answer 8.4

```python
from pcinput import getFloat
from math import sqrt

# This function solves a quadratic equation.
# Its parameters are the numeric values for A, B, and C in the
# equation Ax**2 + Bx + C = 0. It returns three values: an int
# 0, 1, or 2, indicating the number of solutions, followed by two
# numbers which are the solutions. With no solutions, both
# solutions are set to zero. With one solution, it is returned as
# the first of the two, while the other is set to zero.
def quadraticFormula( a, b, c ):
    if a == 0:
        if b == 0:
            return 0, 0, 0
        return 1, -c/b, 0
    discriminant = b*b - 4*a*c
    if discriminant < 0:
        return 0, 0, 0
    elif discriminant == 0:
        return 1, -b/(2*a), 0
    else:
        return 2, (-b+sqrt(discriminant))/(2*a), \
            (-b-sqrt(discriminant))/(2*a)

num, sol1, sol2 = quadraticFormula( getFloat( "A: " ),
    getFloat( "B: " ), getFloat( "C: " ) )
if num == 0:
    print( "There are no solutions" )
elif num == 1:
    print( "There is one solution, namely:", sol1 )
else:
    print( "There are two solutions, namely:", sol1, "and", sol2)
```

#### Answer 8.5

```python
from pcinput import getInteger

def getNumber( prompt ):
    while True:
        num = getInteger( prompt )
        if num < 0 or num > 1000:
            print( "Please enter a number between 0 and 1000" )
            continue
        return num

def main():
    while True:
        x = getNumber( "Enter number 1: " )
        if x == 0:
            break
        y = getNumber( "Enter number 2: " )
        if y == 0:
            break
        if x%y == 0 or y%x == 0:
            print( "Error: the numbers cannot be dividers" )
            return
        print( "Multiplication of", x, "and", y, "gives", x * y )
    print( "Goodbye!" )

if __name__ == '__main__':
    main()
```

#### Answer 8.6

```python
# Calculates the factorial of parameter n, which must be an
# integer. Returns the value of the factorial as an integer.
def factorial( n ):
    value = 1
    for i in range( 2, n+1 ):
        value *= i
    return value

# Calculates n over k; parameters n and k are integers. Returns
# the value n over k as an integer (because it always must be
# an integer).
def binomialCoefficient( n, k ):
    if k > n:
        return 0
    return int( factorial( n ) /
        (factorial( k )*factorial( n - k )) )

def main():
    print( factorial( 5 ) )
    print( binomialCoefficient( 8, 3 ) )

if __name__ == '__main__':
    main()
```

#### Answer 8.7

The code tries to print the return value of the function
`area_of_triangle()`, but since this function has no return value, it
prints the word `None`. To display the output of a function, you can
either print the output in the function and then call it without using
the return value, or you let the function produce the output, return it,
and print the return value of the function in your main program. Not
both. In general it is preferable if functions do not do the printing
themselves, because it makes them more generally usable (for instance,
the function `area_of_triangle()`, if it just returns the area instead
of printing it, you can not only use the function to print the area, but
also use the area in calculations). If you do not understand the
explanation given here, revisit Chapter
6.

### Chapter 10

#### Answer 9.1

```python
def fib( n ):
    if n <= 2:
        return 1
    return fib( n-1 ) + fib( n-2 )

print( fib( 20 ) )
```

#### Answer 9.2

```python
def fib( n, depth ):
    indent = 6 * depth * " "
    print( "{}fib({})".format( indent, n ) )
    if n <= 2:
        print( "{}return {}".format( indent, 1 ) )
        return 1
    value = fib( n-1, depth+1 ) + fib( n-2, depth+1 )
    print( "{}return {}".format( indent, value ) )
    return value

print( fib( 5, 0 ) )
```

#### Answer 9.3

Since the Fibonacci sequence can just as easily be implemented as an
iterative function (you did this in the previous chapter), doing it as a
recursive function is not a good idea. The reasons are the same as for
the factorial, explained in the chapter. There is the additional reason
that the recursive definition basically calculates all terms of the
sequence multiple times, as you can see when you look at the output for
the second exercise, while calculating them just once suffices.

#### Answer 9.4

```python
def gcd( m, n ):
    if m % n == 0:
        return n
    return gcd( n, m%n )

print( gcd( 7*5*13, 2*3*7*11 ) )
```

Interestingly, while the definition of the algorithm distinguishes the
smallest and the largest number, you actually do not have to make that
distinction in your code. If you call the function with the two
exchanged, it just leads to one extra recursive call.

#### Answer 9.5

The problem in this code is that when I enter a string with two illegal
characters, then it will recursively call itself twice, namely once for
each of the letters. So, for instance, if the user enters `"route67"`,
it will first call itself recursively for the `"6"`. If the user then
enters a correct string, the function should end. Instead, it continues
checking the original input `"route67"`, finds the `"7"`, and calls
itself recursively again to ask for yet another string. I could explain
how you can solve this problem by fixing the code, but the real fix here
is that you should not write recursive functions that interact with the
user.

#### Answer 9.6

```python
SIZE = 4

def solve_hanoi( pole_from, pole_tmp, pole_to, size ):
    if size == 1:
        print( "Disc 1 from", pole_from, "to", pole_to )
        return 1
    moves = solve_hanoi( pole_from, pole_to, pole_tmp, size-1 )
    print( "Disc", size, "from", pole_from, "to", pole_to )
    moves += 1+solve_hanoi( pole_tmp, pole_from, pole_to, size-1)
    return moves

moves = solve_hanoi( 'A', 'B', 'C', SIZE )
print( moves, "moves needed" )
```

An iterative approach to solve this puzzle is the following. Repeat
these two steps until the problem is solved: (1) Move disc 1 to the next
pole; (2) Move a disc that is not disc 1 to another pole (there is
always exactly one disc for which you can do this). The only decision
that remains is whether you should move disc 1 "clockwise" or
"counter-clockwise." If the size of the biggest disc is even, go
clockwise (A to B, B to C, or C to A). Otherwise, go counter-clockwise
(A to C, C to B, or B to A). This solution is fast and avoids recursion,
which means that it works for bigger disc sizes than the recursive
solution tends to allow. However, it is more complex to implement as you
have to represent each pole as a list of discs (lists will be introduced
in Chapter
13),
and you have to find a way to check whether the game is solved (you can
just take the number of necessary moves, which is $$2^N-1$$).

### Chapter 11

#### Answer 10.1

```python
text = """And Saint Attila raised the hand grenade up on high,
saying, "O Lord, bless this thy hand grenade, that with it
thou mayst blow thine enemies to tiny bits, in thy mercy."
And the Lord did grin. And the people did feast upon the lambs,
and sloths, and carp, and anchovies, and orangutans, and
breakfast cereals, and fruit bats, and large chu..."""

counta, counte, counti, counto, countu = 0, 0, 0, 0, 0
for c in text:
    if c.upper() == "A":
        counta += 1
    elif c.upper() == "E":
        counte += 1
    elif c.upper() == "I":
        counti += 1
    elif c.upper() == "O":
        counto += 1
    elif c.upper() == "U":
        countu += 1

print( "Counts: a={}, e={}, i={}, o={}, u={}".format(
    counta, counte, counti, counto, countu ) )
```

#### Answer 10.2

```python
text = """And sending tinted postcards of places they don't
realise they haven't even visited to 'All at nu[m]ber 22, weather
w[on]derful, our room is marked with an 'X'. Wish you were here.
Food very greasy but we've found a charming li[t]tle local place
hidden awa[y ]in the back streets where they serve Watney's Red
Barrel and cheese and onion cris[p]s and the accordionist pla[y]s
"Maybe i[t]'s because I'm a Londoner"' and spending four days on
the tarmac at Luton airport on a five-day package tour wit[h]
n[o]thing to eat but dried Watney's sa[n]dwiches..."""

start = -1
while True:
    start = text.find( "[", start+1 )
    if start < 0:
        break
    finish = text.find( "]", start )
    if finish < 0:
        break
    print( text[start+1:finish], end="" )
    start = finish
print()
```

#### Answer 10.3

```python
ch = "A"
while ch <= "Z":
    print( ch, end=" " )
    ch = chr( ord( ch )+1 )
print()

for i in range( 26 ):
    rotr13 = (i + 13)%26
    ch = chr( ord( "A" ) + rotr13 )
    print( ch, end=" " )
```

#### Answer 10.4

```python
text = """How much wood would a woodchuck chuck
If a woodchuck could chuck wood?
He would chuck, he would, as much as he could,
And chuck as much as a woodchuck would
If a woodchuck could chuck wood."""

def clean( s ):
    news = ""
    s = s.lower()
    for c in s:
        if c >= "a" and c <= "z":
            news += c
        else:
            news += " "
    return news

count = 0
for word in clean( text ).split():
    if word == "wood":
        count += 1

print( "Number of times \"wood\" occurs in the text:", count )
```

Note that in the example text, the word "wood" never occurs with a
capital. For a solid test, you should insert "wood" written with one or
more capitals in the text somewhere.

#### Answer 10.5

```python
text = "Hello, world!"
newtext = ""

while len( text ) > 0:
    i = 0
    ch = text[i]
    j = 1
    while j < len( text ):
        if text[j] < ch:
            ch = text[j]
            i = j
        j += 1
    text = text[:i] + text[i+1:]
    newtext += ch

print( newtext )
```

#### Answer 10.6

```python
from sys import exit

sentence = "as it turned out our chance meeting with REverend \
aRTHUR BElling was was to change our whole way of life, and \
every sunday we'd hurry along to St lOONY up the Cream BUn \
and Jam..."

# Just check if there really is a sentence.
if len( sentence  ) <= 0:
    exit()

# Capitalize first letter
newsentence = sentence[0].upper() + sentence[1:]

wordlist = newsentence.split()
lastword = ""
newsentence = ""

for word in wordlist:

    # Correct double capitals
    if len( word ) > 2 and word[0] >= "A" and word[0] <= "Z" and\
        word[1] >= "A" and word[1] <= "Z" and word[2] >= "a" and\
        word[2] <= "z":
        word = word[0] + word[1].lower() + word[2:]

    # Capitalize days
    day = word.lower()
    if day == "sunday" or day == "monday" or day == "tuesday" or\
        day == "wednesday" or day == "thursday" or \
        day == "friday" or day == "saturday":
        word = day[0].upper() + day[1:]

    # Correct CAPS LOCK
    if word[0] >= "a" and word[0] <= "z":
        allcaps = True
        for c in word[1:]:
            if not (c >= "A" and c <= "Z"):
                allcaps = False
                break
        if allcaps:
            word = word[0].upper() + word[1:].lower()

    # Remove duplicates
    if word == lastword:
        continue

    newsentence += word + " "
    lastword = word

newsentence = newsentence.strip()
print( newsentence )
```

### Chapter 12

#### Answer 11.1

I created `display_complex()` to nicely format complex numbers (it will
not show a real part which is zero, or a 1 in front of the $$i$$, or clump
a plus and minus together). Creating such a function was not a
requirement.

```python
def add_complex( c1, c2 ):
    return (c1[0] + c2[0], c1[1] + c2[1])

def display_complex( c ):
    s = "("
    if c[1] == 0:
        return str( c[0] )
    elif c[0] != 0:
        s += str( c[0] )
        if c[1] > 0:
            s += "+"
    if c[1] != 1:
        if c[1] == -1:
            s += "-"
        else:
            s += str( c[1] )
    s += "i)"
    return s

num1 = (2,1)
num2 = (0,2)
print( display_complex( num1 ), "+", display_complex( num2 ),
    "=", display_complex( add_complex( num1, num2 ) ) )
```

#### Answer 11.2

I used a less nice version of `display_complex()` for this solution.

```python
def multiply_complex( c1, c2 ):
    return (c1[0]*c2[0] - c2[1]*c1[1], c1[0]*c2[1] + c1[1]*c2[0])

def display_complex( c ):
    return "({},{}i)".format( c[0], c[1] )

num1 = (2,1)
num2 = (0,2)
print( display_complex( num1 ), "*", display_complex( num2 ),
    "=", display_complex( multiply_complex( num1, num2 ) ) )
```

#### Answer 11.3

```python
inttuple = ( 1, 2, ( 3, 4 ), 5, ( ( 6, 7, 8, ( 9, 10 ), 11 ), 12,
    13 ), ( ( 14, 15, 16 ), ( 17, 18, 19, 20 ) ) )

def display_inttuple( it ):
    for element in it:
        if isinstance( element, int ):
            print( element, end=" ")
        else:
            display_inttuple( element )

display_inttuple( inttuple )
```

### Chapter 13

#### Answer 12.1

```python
from random import choice

answers = [ "It is certain", "It is decidedly so", "Without a \
doubt", "Yes, definitely", "You may rely on it", "As I see it, \
yes", "Most likely", "Outlook good", "Yes", "Signs point to yes",
"Reply hazy try again", "Ask again later", "Better not tell you \
now", "Cannot predict now", "Concentrate and ask again", "Don't \
count on it", "My reply is no", "My sources say no", "Outlook \
not so good", "Very doubtful" ]

input( "Ask the magic 8-ball your question: " )
print( "The magic 8-ball says:", choice( answers ) )
```

The `choice()` function from `random` selects a random item from a list.
You could also have used `randint()`, selecting an index from the range
0 to `len( answers )-1`.

#### Answer 12.2

```python
from random import randint

deck = []
for value in ("Ace", "2", "3", "4", "5", "6", "7", "8",
    "10", "Jack", "Queen", "King"):
    for suit in ("Hearts", "Spaces", "Clubs", "Diamonds"):
        deck.append( value + " of " + suit )

for i in range( len( deck ) ):
    j = randint( i, len( deck )-1 )
    deck[i], deck[j] = deck[j], deck[i]

for card in deck:
    print( card )
```

#### Answer 12.3

```python
fifo = []
while True:
    k = input( "> " )
    if k == "":
        break
    if k != "?":
        fifo.append( k )
    elif len( fifo ) > 0:
        print( fifo.pop(0) )
    else:
        print( "List is empty" )
```

#### Answer 12.4

```python
text = """Now, it's quite simple to defend yourself against a
man armed with a banana. First of all you force him to drop
the banana; then, second, you eat the banana, thus disarming
him. You have now rendered him helpless."""

def count_letter( x ):
    return x[0], -ord(x[1])

countlist = []
for i in range( 26 ):
    countlist.append( [0, chr(ord("a")+i)] )

for letter in text.lower():
    if letter >= "a" and letter <= "z":
        countlist[ord(letter)-ord("a")][0] += 1

countlist.sort( reverse=True, key=count_letter )

for count in countlist:
    print( "{:3}: {}".format( count[0],count[1] ) )
```

#### Answer 12.5

There are basically two general approaches to this program: either you
make a list of numbers, or you make a list of booleans and use the index
as numbers. In the solution below, I used the booleans method. I start
the list at zero, as that saves many subtractions while only adding one
useless boolean. The method is really fast because I can work with
indices.

```python
numbers = 101 * [True]
numbers[1] = False
for i in range( 1, len( numbers ) ):
    if not numbers[i]:
        continue
    print( i, end=" " )
    j = 2
    while j*i < len( numbers ):
        numbers[j*i] = False
        j += 1
```

In the code below, I use the alternative method. I use the `range()`
function to create the list. I actually remove items from the list when
I know that they are not prime, which reduces the number of list
manipulations needed when increasing numbers are removed.

```python
MAXNUM = 100
numbers = list( range(2,MAXNUM+1) )
i = 0
while i < len( numbers ):
    j = i+1
    while j < len( numbers ):
        if numbers[j]%numbers[i]:
            j += 1
        else:
            numbers.pop(j)
    i += 1
for i in numbers:
    print( i, end=" " )
```

#### Answer 12.6

```python
from pcinput import getInteger

EMPTY = "-"
PLAYERX = "X"
PLAYERO = "O"
MAXMOVE = 9

def display_board( b ):
    print( "  1 2 3" )
    for row in range( 3 ):
        print( row+1, end=" ")
        for col in range( 3 ):
            print( b[row][col], end=" " )
        print()

def opponent( p ):
    if p == PLAYERX:
        return PLAYERO
    return PLAYERX

def getRowCol( player, what ):
    while True:
        num = getInteger( "Player "+player+", which "+what+
            " do you play? " )
        if num < 1 or num > 3:
            print( "Please enter 1, 2, or 3" )
            continue
        return num

def winner( b ):
    for row in range( 3 ):
        if b[row][0] != EMPTY and b[row][0] == b[row][1] \
            and b[row][0] == b[row][2]:
            return True
    for col in range( 3 ):
        if b[0][col] != EMPTY and b[0][col] == b[1][col] \
            and b[0][col] == b[2][col]:
            return True
    if b[1][1] != EMPTY:
        if b[1][1] == b[0][0] and b[1][1] == b[2][2]:
            return True
        if b[1][1] == b[0][2] and b[1][1] == b[2][0]:
            return True
    return False

board = [[EMPTY,EMPTY,EMPTY],[EMPTY,EMPTY,EMPTY],
    [EMPTY,EMPTY,EMPTY]]
player = PLAYERX

display_board( board )
move = 0
while True:
    row = getRowCol( player, "row" )
    col = getRowCol( player, "column" )
    if board[row-1][col-1] != EMPTY:
        print( "There is already a piece at row", row,
            "and column", col )
        continue
    board[row-1][col-1] = player
    display_board( board )
    if winner( board ):
        print( "Player", player, "won!" )
        break
    move += 1
    if move == MAXMOVE:
        print( "It's a draw." )
        break
    player = opponent( player )
```

#### Answer 12.7

```python
from pcinput import getString
from random import randint

EMPTY = "."
BATTLESHIP = "X"
SHIPS = 3
WIDTH = 4
HEIGHT = 3

def displayBoard( b ):
    print( "  ", end="" )
    for col in range( WIDTH ):
        print( chr( ord("A")+col ), end=" " )
    print()
    for row in range( HEIGHT ):
        print( row+1, end=" ")
        for col in range( WIDTH ):
            print( b[row][col], end=" " )
        print()

def placeBattleships( b ):
    for i in range( SHIPS ):
        while True:
            x = randint( 0, WIDTH-1 )
            y = randint( 0, HEIGHT-1 )
            if b[y][x] == BATTLESHIP:
                continue
            if x > 0 and b[y][x-1] == BATTLESHIP:
                continue
            if x < WIDTH-1 and b[y][x+1] == BATTLESHIP:
                continue
            if y > 0 and b[y-1][x] == BATTLESHIP:
                continue
            if y < HEIGHT-1 and b[y+1][x] == BATTLESHIP:
                continue
            break
        b[y][x] = BATTLESHIP

def getTarget():
    while True:
        cell = getString( "Which cell do you target? " ).upper()
        if len( cell ) != 2:
            print( "Please enter a cell as XY,",
                "where X is a letter and Y a digit" )
            continue
        if cell[0] not in "ABCD":
            print( "The first character of the cell",
                "should be a letter in the range A-"+
                chr( ord("A")+WIDTH-1 ) )
            continue
        if cell[1] not in "123":
            print( "The second character of the cell should be",
                "a digit in the range 1-"+str( HEIGHT ) )
            continue
        return ord(cell[0])-ord("A"), ord(cell[1])-ord("1")

board = []
for i in range( HEIGHT ):
    row = WIDTH * [EMPTY]
    board.append( row )
placeBattleships( board )
displayBoard( board )

hits = 0
moves = 0
while hits < SHIPS:
    x, y = getTarget()
    if board[y][x] == BATTLESHIP:
        print( "You sunk my battleship!" )
        board[y][x] = EMPTY
        hits += 1
    else:
        print( "Miss!" )
    moves += 1

print( "You needed", moves, "moves to sink all battleships." )
```

#### Answer 12.8

```python
# Recursive function that determines if intlist, which is a list
# of integers, contains a subset that adds up to total. It
# returns the subset, or empty list if there is no such subset.
def subset_that_adds_up_to( intlist, total ):
    for num in intlist:
        if num == total:
            return [num]
        newlist = intlist[:]
        newlist.remove( num )
        retlist = subset_that_adds_up_to( newlist, total-num )
        if len( retlist ) > 0:
            retlist.insert( 0, num )
            return( retlist )
    return []

numlist = [ 3, 8, -1, 4, -5, 6 ]

solution = subset_that_adds_up_to( numlist, 0 )

if len( solution ) <= 0:
    print( "There is no subset which adds up to zero" )
else:
    for i in range( len( solution ) ):
        if solution[i] < 0 or i == 0:
            print( solution[i], end="" )
        else:
            print( "+{}".format( solution[i] ), end="" )
    print( "=0" )
```

The recursive function works as follows: It loops through all numbers on
`intlist`. If the current number is equal to `total`, it has found a
solution and returns a list which contains only that number. Otherwise,
it recursively calls itself with a copy of `intlist` from which the
current number is removed, for a total which is reduced by the current
number (e.g., if the current number is 3 and the total is 5, it removes
3 from the list and checks whether a total of 2 can be achieved with the
remaining list, because then 5 could be achieved by adding 3 to the
solution for the remaining list). If the recursive call returns a list
that is not empty, a solution is found, so the current number is
appended to the returned list, and the result is returned. Once all
numbers have been processed and no solution was found, an empty list is
returned.

Note: The solution to this problem tests all possible subsets until one
is found that solves the problem, or all of them have been tested. You
might wonder whether there are smarter solutions, considering the fact
that the number of subset rises exponentially with the size of the list.
The answer is that there might be solutions which improve upon this one
(for instance, I could take into account that if a number occurs
multiple times on the list that some subsets occur multiple times and
need only be tested once), but that for general lists of numbers, no
algorithm is known that avoids having to process each and every subset
if there is no solution. For those who know some complexity theory: the
subset sum problem is "NP-hard."

### Chapter 14

#### Answer 13.1

```python
text = """How much wood would a woodchuck chuck
If a woodchuck could chuck wood?
He would chuck, he would, as much as he could,
And chuck as much as a woodchuck would
If a woodchuck could chuck wood."""

def clean( s ):
    news = ""
    s = s.lower()
    for c in s:
        if c >= "a" and c <= "z":
            news += c
        else:
            news += " "
    return news

worddict = {}
for word in clean( text ).split():
    worddict[word] = worddict.get( word, 0 ) + 1

keylist = list( worddict.keys() )
keylist.sort()
for key in keylist:
    print( "{}: {}".format( key, worddict[key] ) )
```

#### Answer 13.2

```python
movies = {  "Monty Python and the Holy Grail":
            [ 9, 10, 9.5, 8.5, 3, 7.5,8 ],
            "Monty Python's Life of Brian":
            [ 10, 10, 0, 9, 1, 8, 7.5, 8, 6, 9 ],
            "Monty Python's Meaning of Life":
            [ 7, 6, 5 ],
            "And Now For Something Completely Different":
            [ 6, 5, 6, 6 ] }

keylist = list( movies.keys() )
keylist.sort()
for key in keylist:
    print( "{}: {}".format( key, round(
        sum( movies[key] )/len( movies[key] ), 1 ) ) )
```

#### Answer 13.3

Many answers are possible. Probably the simplest one is to use a
dictionary where the keys are tuples of writers' last and first names,
and the values are lists of all the books of a writer. A book is a tuple
consisting of title and location. To find all the books of a writer, use
the writer's last and first name to find a list of his books. To find
the location of a specific book of a writer, get the list of his books
and find the book on that list, then get the corresponding location. You
could choose to store the book list also as a dictionary with a book's
title as key, but writers usually do not write so many books that you
need to do that. Of course, using names as keys is not a great idea as
it is easy to make spelling mistakes, and book titles as keys would be
even less useful, but these were the only identifying elements I
described. I can't complain if you want to introduce easier and less
ambiguous keys in such a data structure (but in general, you should
divert to a database system to deal with libraries).

### Chapter 15

#### Answer 14.1

```python
allthings = {"Socrates", "Plato", "Eratosthenes", "Zeus", "Hera",
    "Athens", "Acropolis", "Cat", "Dog"}
men = {"Socrates", "Plato", "Eratosthenes"}
mortalthings = {"Socrates","Plato","Eratosthenes","Cat","Dog"}

print( men.issubset( mortalthings ) ) # (a)
print( "Socrates" in men ) # (b)
print( "Socrates" in mortalthings ) # (c)
print( len( mortalthings.difference( men ) ) > 0 ) # (d)
print( len( allthings.difference( mortalthings ) ) > 0 ) # (e)
```

#### Answer 14.2

```python
set3 = set( [3*x for x in range( 1, int( 1001/3 ) )] )
set7 = set( [7*x for x in range( 1, int( 1001/7 ) )] )
set11 = set( [11*x for x in range( 1, int( 1001/11 ) )] )

seta = set3 & set7 & set11
setb = (set3 & set7) - set11
setc = set( range( 1, 1001 ) ) - set3 - set7 - set11
```

### Chapter 16

#### Answer 15.1

```python
from os import listdir, getcwd

flist = listdir( "." )
for name in flist:
    print( getcwd() + "/" + name )
```

### Chapter 17

#### Answer 16.1

The code below is mostly a copy of some code you had to write in Chapter
14.
The only difference is that the text here is not provided as a string,
but read from a file.

```python
def clean( s ):
    news = ""
    s = s.lower()
    for c in s:
        if c >= "a" and c <= "z":
            news += c
        else:
            news += " "
    return news

fp = open( "pc_woodchuck.txt" )
text = fp.read()
fp.close()

wdict = {}
for word in clean( text ).split():
    wdict[word] = wdict.get( word, 0 ) + 1

keylist = list( wdict.keys() )
keylist.sort()
for key in keylist:
    print( "{}: {}".format( key, wdict[key] ) )
```

#### Answer 16.2

```python
def clean( s ):
    news = ""
    s = s.lower()
    for c in s:
        if c >= "a" and c <= "z":
            news += c
        else:
            news += " "
    return news

wdict = {}
fp = open( "pc_woodchuck.txt" )
while True:
    line = fp.readline()
    if line == "":
        break
    for word in clean( line ).split():
        wdict[word] = wdict.get( word, 0 ) + 1
fp.close()

keylist = list( wdict.keys() )
keylist.sort()
for key in keylist:
    print( "{}: {}".format( key, wdict[key] ) )
```

#### Answer 16.3

```python
from os.path import join
from os import getcwd

def removevowels( line ):
    newline = ""
    for c in line:
        if c not in "aeiouAEIOU":
            newline += c
    return newline

inputname = join( getcwd(), "pc_woodchuck.txt" )
outputname = join( getcwd(), "pc_woodchuck.tmp" )

fpi = open( inputname )
fpo = open( outputname, "w" )

countread = 0
countwritten = 0

while True:
    line = fpi.readline()
    if line == "":
        break
    countread += len( line )
    line = removevowels( line )
    fpo.write( line )
    countwritten += len( line )

fpo.close()
fpi.close()

print( "Characters read:", countread )
print( "Characters written:", countwritten )
```

#### Answer 16.4

The solution below makes use of sets: a set is created for each file,
which contains all the words from that file that have 2 letters or more.
You can change the length of the words searched for by changing
`WORDLEN`. To make the program flexible, it is not limited to just three
sets, but uses as many sets as there are names in the file list. At the
end, the program creates an intersection of all the sets to determine
the words that meet the requirements.

```python
from os.path import join
from os import getcwd

WORDLEN = 2

def clean( s ):
    news = ""
    s = s.lower()
    for c in s:
        if c >= "a" and c <= "z":
            news += c
        else:
            news += " "
    return news

files = ["pc_jabberwocky.txt","pc_rose.txt","pc_woodchuck.txt"]
setlist = []

for name in files:
    filename = join( getcwd(), name )
    wordset = set()
    setlist.append( wordset )
    fp = open( filename )
    while True:
        line = fp.readline()
        if line == "":
            break
        wordlist = clean( line ).split()
        for word in wordlist:
            if len( word ) >= WORDLEN:
                wordset.add( word )
    fp.close()

combination = setlist[0].copy()
i = 1
while i < len( setlist ):
    combination = combination & setlist[i]
    i += 1
for word in combination:
    print( word )
```

#### Answer 16.5

Again, in the solution below I chose to be flexible as far as the number
of files is concerned. The program is easier to write if you assume
there are three files, and no more. If you chose such a solution, that
is acceptable as long as the program does what it should do, as allowing
it to work with a variable number of files is more an exercise for the
chapter on iterations. However, by now you should be quite familiar with
iterations, so try to apply them whenever they provide a superior
solution.

```python
from os.path import join
from os import getcwd

files = ["pc_jabberwocky.txt","pc_rose.txt","pc_woodchuck.txt"]
letterlist = [ len( files )*[0] for i in range( 26 ) ]
totallist = len( files ) * [0]

# Process all the input files, read their contents line by line,
# make them lower case, and keep track of the letter counts in
# letterlist, while keeping track of total counts in totallist.
filecount = 0
for name in files:
    filename = join( getcwd(), name )
    fp = open( filename )
    while True:
        line = fp.readline()
        if line == "":
            break
        line = line.lower()
        for c in line:
            if c >= 'a' and c <= 'z':
                totallist[filecount] += 1
                letterlist[ord(c)-ord("a")][filecount] += 1
    fp.close()
    filecount += 1

# Write the counts in CSV format.
outfilename = join( getcwd(), "pc_writetest.csv" )
fp = open( outfilename, "w" )
for i in range( len( letterlist ) ):
    s = "\"{}\"".format( chr( ord("a")+i ) )
    for j in range( len( files ) ):
        s += ",{:.5f}".format( letterlist[i][j]/totallist[j] )
    fp.write( s+"\n" )
fp.close()

# Print the contents of the created output file as a check.
fp = open( outfilename )
print( fp.read() )
fp.close()
```

### Chapter 18

#### Answer 17.1

The code can generate a `ValueError` when you enter something that is
not an integer, an `IndexError` when you give an index outside the range
`{-5,4}`, a `ZeroDivisionError` when you enter index 2, and a
`TypeError` when you enter index 3. The code below does the most
straightforward handling, but you can also build a loop around the code
so that the user gets asked for new inputs until it works.

```python
numlist = [ 100, 101, 0, "103", 104 ]
try:
    i1 = int( input( "Give an index: " ) )
    print( "100 /", numlist[i1], "=", 100 / numlist[i1] )
except ValueError:
    print( "You did not enter an integer" )
except IndexError:
    print( "You should specify an index between -5 and 4" )
except ZeroDivisionError:
    print( "It looks like the list contains a zero" )
except TypeError:
    print( "it looks like there is a non-numeric item" )
except:
    print( "Something unexpected happened" )
    raise
```

### Chapter 19

#### Answer 18.1

For this program I created a copy of "pc_rose.txt" and called it
"pc_rose_copy.txt." To demonstrate what happens, I display the
contents of the file before and after the encryption process.

```python
FILENAME = "pc_rose_copy.txt"

def display_contents( filename ):
    fp = open( filename, "rb" )
    print( fp.read() )
    fp.close()

def encrypt( filename ):
    fp = open( filename, "r+b" )
    buffer = fp.read()
    fp.seek(0)
    for c in buffer:
        if c >= 128:
            fp.write( bytes( [c-128] ) )
        else:
            fp.write( bytes( [c+128] ) )
    fp.close()

display_contents( FILENAME )
encrypt( FILENAME )
display_contents( FILENAME )
```

#### Answer 18.2

```python
letters = "etaoinshrdlcum "
unencoded = "Hello, world!"

# Print the unencoded string, as a check.
print( unencoded, len( unencoded ) )

# Create a half-byte-list as a basis for the encoding.
halfbytelist = []
for c in unencoded:
    if c in letters:
        halfbytelist.append( letters.index( c )+1 )
    else:
        byte = ord( c )
        halfbytelist.extend( [0, int( byte/16 ), byte%16 ] )
if len( halfbytelist )%2 != 0:
    halfbytelist.append( 0 )

# Turn the half-byte-list into a byte-list.
bytelist = []
for i in range( 0, len( halfbytelist ), 2 ):
    bytelist.append( 16*halfbytelist[i] + halfbytelist[i+1] )

# Turn the byte-list into a byte string and print it, as a check.
encoded = bytes( bytelist )
print( encoded, len( encoded ) )
```

This solution needs 25 lines of code, of which 4 are comments, 4 are
empty lines, and 3 are only for testing purposes. So, basically, 14
lines of code suffices. That wasn't too bad, right?

#### Answer 18.3

```python
letters = "etaoinshrdlcum "
encoded = b'\x04\x81\xbb@,\xf0wI\xba\x02\x10'

# Print the encoded byte string, as a check.
print( encoded, len( encoded ) )

# Create a half-byte-list on the basis of the byte string.
halfbytelist = []
for c in encoded:
    halfbytelist.extend( [ int( c/16 ), c%16 ] )
if halfbytelist[-1] == 0:
    del halfbytelist[-1]

# Turn the half-byte-list into a string.
decoded = ""
while len( halfbytelist ) > 0:
    num = halfbytelist.pop(0)
    if num > 0:
        decoded += letters[num-1]
        continue
    num = 16*halfbytelist.pop(0) + halfbytelist.pop(0)
    decoded += chr( num )

# Print the string, as a check.
print( decoded, len( decoded ) )
```

#### Answer 18.4

This program looks like it is quite long, but it is straightforward.
`compress()` and `decompress()` were developed in the previous two
exercises (I changed them so that input and output are byte strings).
The rest of the program is mainly the handling of potential errors in
dealing with the files. You often see this in programs: the core
functionality needs a few lines, while handling of potential problems
takes three-quarters of the code.

```python
from pcinput import getString, getLetter
from os.path import exists, getsize

LETTERS = b"etaoinshrdlcum "

# Compress byte string unencoded, return the compressed version.
def compress( unencoded ):
    halfbytelist = []
    for c in unencoded:
        if c in LETTERS:
            halfbytelist.append( LETTERS.index( c )+1 )
        else:
            halfbytelist.extend( [0, int( c/16 ), c%16 ] )
    if len( halfbytelist )%2 != 0:
        halfbytelist.append( 0 )
    bytelist = []
    for i in range( 0, len( halfbytelist ), 2 ):
        bytelist.append( 16*halfbytelist[i] + halfbytelist[i+1] )
    return bytes( bytelist )

# Decompress byte string encoded, return decompressed version.
def decompress( encoded ):
    halfbytelist = []
    for c in encoded:
        halfbytelist.extend( [ int( c/16 ), c%16 ] )
    if halfbytelist[-1] == 0:
        del halfbytelist[-1]
    bytelist = []
    while len( halfbytelist ) > 0:
        num = halfbytelist.pop(0)
        if num > 0:
            bytelist.append( LETTERS[num-1] )
            continue
        num = 16*halfbytelist.pop(0) + halfbytelist.pop(0)
        bytelist.append( num )
    return bytes( bytelist )

# Ask for the input file and read its contents.
while True:
    filein = getString( "Which is the input file? " )
    if not exists( filein ):
        print( filein, "does not exist" )
        continue
    try:
        fp = open( filein, "rb" )
        buffer = fp.read()
        fp.close()
    except IOError as ex:
        print( filein, "cannot be processed, choose another" )
        print( "Error [{}]: {}".format( ex.args[0], ex.args[1] ))
        continue
    break

# Ask for the output file and create it.
while True:
    fileout = getString( "Which is the output file? " )
    if exists( fileout ):
        print( fileout, "already exists" )
        continue
    try:
        fp = open( fileout, "wb" )
    except IOError as ex:
        print( fileout, "cannot be created,",
            "choose another file name" )
        print( "Error [{}]: {}".format( ex.args[0], ex.args[1] ))
        continue
    break

# Ask whether the user wants to compress or decompress.
while True:
    dc = getLetter( "Choose (C)ompress or (D)ecompress? " )
    if dc != 'C' and dc != 'D':
        print( "Please choose C or D" )
        continue
    break

# Compress or decompress the buffer.
if dc == 'C':
    buffer = compress( buffer )
else:
    buffer = decompress( buffer )

# Store the (de)compressed buffer in the output file.
try:
    fp.write( buffer )
    fp.close()
except IOError as ex:
    print( "The writing process failed" )
    print( "Error [{}]: {}".format( ex.args[0], ex.args[1] ))

# Report the sizes of input and output.
print( getsize( filein ), "bytes read" )
print( getsize( fileout ), "bytes written" )
```

### Chapter 20

#### Answer 19.1

```python
s = "Hello, world!"
mask = (1<<5) | (1<<3) | (1<<1)    # 00101010

code = ""
for c in s:
    code += chr(ord(c)^mask)
print( code )

decode = ""
for c in code:
    decode += chr(ord(c)^mask)
print( decode )
```

#### Answer 19.2

```python
def setBit( store, index, value ):
    mask = 1<<index
    if value:
        store |= mask
    else:
        store &= ~mask
    return store

# getBit() returns 0 when the bit corresponding to index is set,
# and something else otherwise. As only 0 is interpreted as False
# this function can be used to test the value of the bit.
def getBit( store, index ):
    mask = 1<<index
    return store & mask

def displayBits( store ):
    for i in range( 8 ):
        index = 7 - i
        if getBit( store, index ):
            print( "1", end="" )
        else:
            print( "0", end="" )
    print()

store = 0
store = setBit( store, 0, True )
store = setBit( store, 1, True )
store = setBit( store, 2, False )
store = setBit( store, 3, True )
store = setBit( store, 4, False )
store = setBit( store, 5, True )
displayBits( store )

store = setBit( store, 1, False )
displayBits( store )
```

### Chapter 21

#### Answer 20.1

```python
from copy import copy

class Point:
    def __init__( self, x=0.0, y=0.0 ):
        self.x = x
        self.y = y
    def __repr__( self ):
        return "({}, {})".format( self.x, self.y )

class Rectangle:
    def __init__( self, point, width, height ):
        self.point = copy( point )
        self.width = abs( width )
        self.height = abs( height )
        if self.width == 0:
            self.width = 1
        if self.height == 0:
            self.height = 1
    def __repr__( self ):
        return "[{},w={},h={}]".format( self.point,
            self.width, self.height )
    def surface_area( self ):
        return self.width * self.height
    def circumference( self ):
        return 2*(self.width + self.height)
    def bottom_right( self ):
        return Point( self.point.x + self.width,
            self.point.y + self.height )
    def overlap( self,r ):
        r1, r2 = self, r
        if self.point.x > r.point.x or \
            (self.point.x == r.point.x and \
            self.point.y > r.point.y):
            r1, r2 = r, self
        if r1.bottom_right().x <= r2.point.x or \
            r1.bottom_right().y <= r2.point.y:
            return None
        return Rectangle( r2.point,
            min( r1.bottom_right().x - r2.point.x, r2.width ),
            min( r1.bottom_right().y - r2.point.y, r2.height ) )

r1 = Rectangle( Point( 1, 1 ), 8, 5 )
r2 = Rectangle( Point( 2, 3 ), 9, 2 )

print( r1.surface_area() )
print( r1.circumference() )
print( r1.bottom_right() )
r = r1.overlap( r2 )
if r:
    print( r )
else:
    print( "There is no overlap for the rectangles" )
```

#### Answer 20.2

Considering the list that must be displayed, I placed the `enroll()`
method in `Student`. For the birth date I use the `datetime` module; as
you have to calculate the student's age, you also need today's date,
which is found in the `datetime` module anyway.

```python
from datetime import date
from random import random

class Course:
    def __init__( self, name, number ):
        self.name = name
        self.number = number
    def __repr__( self ):
        return "{}: {}".format( self.number, self.name )

class Student:
    def __init__( self, lastname, firstname, birthdate, anr ):
        self.lastname = lastname
        self.firstname = firstname
        self.birthdate = birthdate
        self.anr = anr
        self.courses = []
    def __str__( self ):
        return self.firstname+" "+self.lastname
    def age( self ):
        today = date.today()
        years = today.year - self.birthdate.year
        if today.month < self.birthdate.month or \
            (today.month == self.birthdate.month \
            and today.day < self.birthdate.day):
            years -= 1
        return years
    def enroll( self, course ):
        if course not in self.courses:
            self.courses.append( course )

students = [
    Student( "Arkansas", "Adrian", date( 1989, 10, 3 ), 453211 ),
    Student( "Bonzo", "Beatrice", date( 1991, 12, 29 ), 476239 ),
    Student( "Continuum", "Carola", date( 1992, 3, 7 ), 784322 ),
    Student( "Doofus", "Dunce", date( 1993, 7, 11 ), 995544 ) ]
courses =[
    Course( "Vinology", 787656 ),
    Course( "Advanced spoon-bending", 651121 ),
    Course( "Research Skills: Babbling", 433231 )]

for student in students:
    for course in courses:
        if random() > 0.3:
            student.enroll( course )

for student in students:
    print( "{}: {} {} ({})".format( student.anr,
        student.firstname, student.lastname, student.age() ) )
    if len( student.courses ) == 0:
        print( "\tNo courses" )
    for course in student.courses:
        print( "\t{}".format( course ) )
```

### Chapter 22

#### Answer 21.1

```python
SUITS = ["Hearts","Spades","Clubs","Diamonds"]
RANKS = ["2","3","4","5","6","7","8","9","10",
    "Jack","Queen","King","Ace"]

class Card:
    def __init__( self, suit, rank ):
        self.suit = suit # used as index in the SUITS list
        self.rank = rank # used as index in the RANKS list
    def __repr__( self ):
        return "({},{})".format( self.suit, self.rank )
    def __str__( self ):
        return "{} of {}".format( RANKS[self.rank], \
            SUITS[self.suit] )
    def __eq__( self, c ):
        if isinstance( c, Card ):
            return self.rank == c.rank
        return NotImplemented
    def __gt__( self, c ):
        if isinstance( c, Card ):
            return self.rank > c.rank
        return NotImplemented
    def __ge__( self, c ):
        if isinstance( c, Card ):
            return self.rank >= c.rank
        return NotImplemented

c5 = Card( 2, 3 )
d5 = Card( 3, 3 )
sk = Card( 1, 11 )
print( "{}, {}, {}".format( c5, d5, sk ) )
print( c5 == d5 )
print( c5 == sk )
print( c5 > sk )
print( c5 >= sk )
print( c5 < sk )
print( c5 <= sk )
```

{:class="callout callout-info"}
> #### Note
> There is no need to implement `__ne__()`, `__lt__()`, or
> `__le__()`, as they are automatically changed into calls to the methods
> that have been implemented.

#### Answer 21.2

For readability, I deleted the methods from `Card` that are not needed
here.

```python
SUITS = ["Hearts","Spades","Clubs","Diamonds"]
RANKS = ["2","3","4","5","6","7","8","9","10",
    "Jack","Queen","King","Ace"]

class Card:
    def __init__( self, suit, rank ):
        self.suit = suit
        self.rank = rank
    def __str__( self ):
        return "{} of {}".format(
            RANKS[self.rank], SUITS[self.suit] )

class Drawpile:
    def __init__( self, pile=[] ):
        self.pile = pile
    def __len__( self ):
        return len( self.pile )
    def __getitem__( self, n ):
        return self.pile[n]
    def add( self, c ):
        self.pile.append( c )
    def draw( self ):
        if len( self ) <= 0:
            return None
        return self.pile.pop(0)
    def __repr__( self ):
        sep = ""
        s = ""
        for c in self.pile:
            s += sep + str( c )
            sep = ", "
        return s

dp1 = Drawpile( [Card(0,1), Card(0,5), Card(2,4), Card(1,12)] )
print( dp1 )
print( dp1[1] )
dp1.add( Card(3,12) )
print( dp1 )
print( dp1.draw() )
print( dp1 )
```

#### Answer 21.3

```python
SUITS = ["Hearts","Spades","Clubs","Diamonds"]
RANKS = ["2","3","4","5","6","7","8","9","10",
    "Jack","Queen","King","Ace"]

class Card:
    def __init__( self, suit, rank ):
        self.suit = suit
        self.rank = rank
    def __repr__( self ):
        return "({},{})".format( self.suit, self.rank )
    def __str__( self ):
        return "{} of {}".format(
            RANKS[self.rank], SUITS[self.suit] )
    def __eq__( self, c ):
        if isinstance( c, Card ):
            return self.rank == c.rank
        return NotImplemented
    def __gt__( self, c ):
        if isinstance( c, Card ):
            return self.rank > c.rank
        return NotImplemented
    def __ge__( self, c ):
        if isinstance( c, Card ):
            return self.rank >= c.rank
        return NotImplemented

class Drawpile:
    def __init__( self, pile=[] ):
        self.pile = pile
    def __len__( self ):
        return len( self.pile )
    def __getitem__( self, n ):
        return self.pile[n]
    def add( self, c ):
        self.pile.append( c )
    def draw( self ):
        if len( self ) <= 0:
            return None
        return self.pile.pop(0)
    def __repr__( self ):
        sep = ""
        s = ""
        for c in self.pile:
            s += sep + str( c )
            sep = ", "
        return s

dp1 = Drawpile( [Card(3,0), Card(0,11), Card(2,5)] )
dp2 = Drawpile( [Card(3,2), Card(3,1), Card(1,6)] )

i = 1
while len( dp1 ) > 0 and len( dp2 ) > 0:
    print( "Round", i )
    print( "Deck1:", dp1 )
    print( "Deck2:", dp2 )
    c1 = dp1.draw()
    c2 = dp2.draw()
    if c1 > c2:
        dp1.add( c1 )
        dp1.add( c2 )
    else:
        dp2.add( c2 )
        dp2.add( c1 )
    i += 1

print( "The game has ended" )
if len( dp1 ) > 0:
    print( "Deck1:", dp1 )
    print( "The first deck wins!" )
else:
    print( "Deck2:", dp2 )
    print( "The second deck wins!" )
```

#### Answer 21.4

Do not forget that in the `__add__()` and `__sub__()` methods you have
to create a (deep) copy of the fruit basket, which you change and
return. If you would change the `fruitbasket` itself instead of a deep
copy, `newbasket = fruitbasket + "apple"` would make `newbasket` an
alias for `fruitbasket`. It is unlikely that the programmer who uses the
class wants that. It is up to the programmer of the main program to
decide whether he wants to actually change the fruit basket, or just
wants to see what a changed version looks like.

However, in `__iadd__()` and `__isub__()` you are actually supposed to
change the fruit basket, and still return `self`. Because a statement
like `fruitbasket += "apple"` clearly is intended to change
`fruitbasket`.

The rest of the class is pretty straightforward, as long as you take
into account that you have to delete fruits when their number has
dropped to zero or less.

```python
from copy import deepcopy

class FruitBasket:

    def __init__( self, fruits={} ):
        self.fruits = fruits

    def __repr__( self ):
        s = ""
        sep = "["
        for fruit in self.fruits:
            s += sep + fruit + ":" + str( self.fruits[fruit] )
            sep = ", "
        s += "]"
        return s

    def __contains__( self, fruit ):
        return fruit in self.fruits

    def __add__( self, fruit ):
        fbcopy = deepcopy( self )
        fbcopy.fruits[fruit] = fbcopy.fruits.get( fruit, 0 ) + 1
        return fbcopy

    def __iadd__( self, fruit ):
        self.fruits[fruit] = self.fruits.get( fruit, 0 ) + 1
        return self

    def __sub__( self, fruit ):
        if fruit not in self.fruits:
            return self
        fbcopy = deepcopy( self )
        fbcopy.fruits[fruit] = fbcopy.fruits.get( fruit, 0 ) - 1
        if fbcopy.fruits[fruit] <= 0:
            del fbcopy.fruits[fruit]
        return fbcopy

    def __isub__( self, fruit ):
        self.fruits[fruit] = self.fruits.get( fruit, 0 ) - 1
        if self.fruits[fruit] <= 0:
            del self.fruits[fruit]
        return self

    def __len__( self ):
        return len( self.fruits )

    def __getitem__( self, fruit ):
        return self.fruits.get( fruit, 0 )

    def __setitem__( self, fruit, n ):
        if n <= 0:
            if fruit in self.fruits:
                del self.fruits[fruit]
        else:
            self.fruits[fruit] = n

fb = FruitBasket()
fb += "apple"
fb += "apple"
fb += "banana"
fb = fb + "cherry"
fb["orange"] = 20
print( len( fb ) )
print( fb )
print( "banana" in fb )
print( "durian" in fb )
fb -= "apple"
fb -= "banana"
fb = fb - "cherry"
fb -= "durian"
print( fb )
print( "banana" in fb )
fb["orange"] = 0
print( fb )
```

### Chapter 23

#### Answer 22.1

```python
class Rectangle:
    def __init__( self, x, y, w, h ):
        self.x, self.y, self.w, self.h = x, y, w, h
    def __repr__( self ):
        return "[({},{}),w={},h={}]".format( self.x, self.y,
          self.w, self.h )
    def area( self ):
        return self.w * self.h
    def circumference( self ):
        return 2*(self.w + self.h)

class Square( Rectangle ):
    def __init__( self, x, y, w ):
        super().__init__( x, y, w, w )

s = Square( 1, 1, 4 )
print( s, s.area(), s.circumference() )
```

#### Answer 22.2

```python
from math import pi

class Shape:
    def area( self ):
        return NotImplemented
    def circumference( self ):
        return NotImplemented

class Circle( Shape ):
    def __init__( self, x, y, r ):
        self.x, self.y, self.r = x, y, r
    def __repr__( self ):
        return "[({},{}),r={}]".format( self.x, self.y, self.r )
    def area( self ):
        return pi * self.r * self.r
    def circumference( self ):
        return 2 * pi * self.r

class Rectangle( Shape ):
    def __init__( self, x, y, w, h ):
        self.x, self.y, self.w, self.h = x, y, w, h
    def __repr__( self ):
        return "[({},{}),w={},h={}]".format( self.x, self.y,
            self.w, self.h )
    def area( self ):
        return self.w * self.h
    def circumference( self ):
        return 2*(self.w + self.h)

class Square( Rectangle ):
    def __init__( self, x, y, w ):
        super().__init__( x, y, w, w )

s = Square( 1, 1, 4 )
print( s, s.area(), s.circumference() )
c = Circle( 1, 1, 4 )
print( c, c.area(), c.circumference() )
```

#### Answer 22.3

I implemented a `MemoryStrategy` class to derive `TitForTat`,
`TitForTwoTats`, and `Majority` from. `MemoryStrategy` keeps track of
all the moves in the game. That is overdoing it a bit, as `TitForTat`
only needs to keep track of the last move, `TitForTwoTats` only needs to
keep track of the last two moves, and `Majority` could make do with just
a count of all the COOPERATEs and DEFECTs of the opponent. Still, if
more elaborate strategies need to be implemented, `MemoryStrategy` is a
good starting point.

One interesting thing to notice is that in any pairing `AlwaysDefect`
has a higher score than its opponent. However, if you let each strategy
play every other strategy and add up the scores, the only strategy that
does worse than `AlwaysDefect` is `Random`. If you want to know why that
is, take a course on Game Theory.

```python
from random import random

COOPERATE = 'C'
DEFECT = 'D'
ROUNDS = 100

class Strategy:
    def __init__( self, name="" ):
        self.name = name
        self.score = 0
    def choice( self ):
        # Should return COOPERATE or DEFECT
        return NotImplemented
    def lastmove( self, mymove, opponentmove ):
        # Gets passed the last move made, after call to choice()
        pass
    def incscore( self, n ):
        self.score += n

class AlwaysDefect( Strategy ):
    def choice( self ):
        return DEFECT

class Random( Strategy ):
    def choice( self ):
        if random() >= 0.5:
            return COOPERATE
        return DEFECT

class MemoryStrategy( Strategy ):
    def __init__( self, name="" ):
        super().__init__( name )
        self.history = []
    def lastmove( self, mymove, opponentmove ):
        self.history.append( (mymove, opponentmove) )

class TitForTat( MemoryStrategy ):
    def choice( self ):
        if len( self.history ) < 1:
            return COOPERATE
        return self.history[-1][1]

class TitForTwoTats( MemoryStrategy ):
    def choice( self ):
        if len( self.history ) < 2:
            return COOPERATE
        if self.history[-1][1] == DEFECT and \
            self.history[-2][1] == DEFECT:
            return DEFECT
        return COOPERATE

class Majority( MemoryStrategy ):
    def choice( self ):
        countD = 0
        for i in range( len( self.history ) ):
            if self.history[i][1] == DEFECT:
                countD += 1
        if countD > len( self.history ) / 2:
            return DEFECT
        return COOPERATE

strategy1 = AlwaysDefect( "Always Defect" )
strategy2 = Majority( "Majority" )

for i in range( ROUNDS ):
    c1 = strategy1.choice()
    c2 = strategy2.choice()
    if c1 == c2:
        strategy1.incscore( 3 if c1 == COOPERATE else 1 )
        strategy2.incscore( 3 if c2 == COOPERATE else 1 )
    else:
        strategy1.incscore( 0 if c1 == COOPERATE else 6 )
        strategy2.incscore( 0 if c2 == COOPERATE else 6 )
    strategy1.lastmove( c1, c2 )
    strategy2.lastmove( c2, c1 )

print( "Score of", strategy1.name, "is", strategy1.score )
print( "Score of", strategy2.name, "is", strategy2.score )
```

### Chapter 24

#### Answer 23.1

```python
from pcinput import getInteger

class NotDividableBy:
    def __init__( self ):
        self.seq = list( range( 1, 101 ) )
    def __iter__( self ):
        return self
    def __next__( self ):
        if len( self.seq ) > 0:
            return self.seq.pop(0)
        raise StopIteration()
    def process( self, num ):
        i = len( self.seq )-1
        while i >= 0:
            if self.seq[i]%num == 0:
                del self.seq[i]
            i -= 1
    def __len__( self ):
        return len( self.seq )

ndb = NotDividableBy()
while True:
    num = getInteger( "Give an integer: " )
    if num < 0:
        print( "Negative integers are ignored" )
        continue
    if num == 0:
        break
    ndb.process( num )

if len( ndb ) <= 0:
    print( "No numbers are left" )
else:
    for num in ndb:
        print( num, end=" " )
```

#### Answer 23.2

```python
def factorial():
    total = 1
    for i in range( 1, 11 ):
        total *= i
        yield total

fseq = factorial()
for n in fseq:
    print( n, end=" " )
```

#### Answer 23.3

```python
from itertools import permutations

word = input( "Please enter a word: " )
seq = permutations( word )
for item in seq:
    print( "".join( item ) )
```

#### Answer 23.4

The only change I made with respect to the previous answer is that I
cast the iterable to a set.

```python
from itertools import permutations

word = input( "Please enter a word: " )
seq = permutations( word )
for item in set( seq ):
    print( "".join( item ) )
```

#### Answer 23.5

```python
from itertools import combinations

numlist = [ 3, 8, -1, 4, -5, 6 ]
solution = []

for i in range( 1, len( numlist )+1 ):
    seq = combinations( numlist, i )
    for item in seq:
        if sum( item ) == 0:
            solution = item
            break
    if len( solution ) > 0:
        break

if len( solution ) <= 0:
    print( "There is no subset which adds up to zero" )
else:
    for i in range( len( solution ) ):
        if solution[i] < 0 or i == 0:
            print( solution[i], end="" )
        else:
            print( "+{}".format( solution[i] ), end="" )
    print( "=0" )
```

{:class="callout callout-info"}
> #### Note
> While this code seems to create all possible subsets, which is a
> number that rises exponentially with the size of `numlist`, since
> iterators are used no more than one subset is in memory at any time. So
> this solution works fine even for large lists of integers (though it may
> get slow, which cannot be helped as this is an NP-hard problem).

#### Answer 23.6

```python
from itertools import combinations

testdict = {"a":1, "b":2, "c":3, "d":4 }
result = [ {} ]

keylist = list( testdict.keys() )
for length in range( 1, len( testdict)+1 ):
    for item in combinations( keylist, length ):
        subdict = {}
        for key in item:
            subdict[key] = testdict[key]
        result.append( subdict )

print( result )
```

#### Answer 23.7

If rows and columns are numbered 0 to 7, then every row and column
number will occur exactly once in the solution. Take a list of the eight
possible column numbers, and consider the index in the list as the row
number. All potential solutions are represented by permutations of this
list. You only need to check these permutations until you find one where
never a diagonal is shared by two of the queens, i.e., where the
absolute difference between the row numbers of any two queens is equal
to the absolute difference of their column numbers.

```python
from itertools import permutations

SIZE = 8 # Board size.

def display_board( columns ):
    for i in columns :
        for j in range( len( columns ) ):
            if i == j:
                print( 'Q', end=" " )
            else:
                print( '-', end=" " )
        print()

def is_solution( columns ):
    for row in range( len( columns ) ):
        col = columns[row]
        for i in range( row+1, len( columns ) ):
            if i - row == abs( columns[i] - col ):
                return False
    return True

columns = list( range( SIZE ) )

for p in permutations( columns ):
    if is_solution( p ):
        display_board( p )
        break
else:
    print( "No solutions found" ) # Should not happen.
```

### Chapter 25

#### Answer 24.1

```python
import sys

total = 0
for i in sys.argv[1:]:
    try:
        total += float( sys.argv[i] )
    except TypeError:
        print( sys.argv[i], "is not a number." )
        sys.exit(1)

print( "The arguments add up to", total )
```

### Chapter 26

#### Answer 25.1

```python
import re

sentence = "The price of a 2-room apartment in Manhattan \
starts at 1 million dollars, and may actually be the 10-fold \
of that on 42nd Street."

pword = re.compile( r"[A-Za-z]+" )
wordlist = pword.findall( sentence )
for word in wordlist:
    print( word )
```

#### Answer 25.2

```python
import re

sentence = "The word ether can be found in my thesaurus \
using the archaic spelling 'aether'."

pthe = re.compile( r"\bthe\b", re.I )
thelist = pthe.findall( sentence )
print( len( thelist ) )
```

#### Answer 25.3

```python
import re

sentence = "Michael Jordan, Bill Gates, and the Dalai Lama \
decided to take a plane trip together."

pname = re.compile( r"\b([A-Z][a-z]*\s+[A-Z][a-z]*)\b" )
namelist = pname.findall( sentence )
for name in namelist:
    print( name )
```

#### Answer 25.4

```python
import re

sentence = "William Randolph Hearst attempted to destroy all \
copies of Orson Welles' masterpiece 'Citizen Kane', because he \
did not appreciate the fact that the protagonist Charles \
Foster Kane was a thinly disguised caricature of himself. I \
wonder whether William Henry Gates The Third would attempt to \
do the same."

pname = re.compile( r"\b([A-Z][a-z]*(\s+[A-Z][a-z]*)+)\b" )
namelist = pname.finditer( sentence )
for name in namelist:
    print( name.group(1) )
```

#### Answer 25.5

```python
import re

sentence = "Client: \"I wish to register a complaint! \
Hello miss!\"\n\
Shopkeeper: \"What do you mean, miss?\"\n\
Client: \"I am sorry, I have a cold.\"\n"

pspoken = re.compile( r"\"[^\"]*\"" )
spokenlist = pspoken.findall( sentence )
for text in spokenlist:
    print( text )
```

#### Answer 25.6

```python
import re

text = "<html><head><title>List of persons with ids</title>\
</head><body>\
<p><id>123123123</id><name>Groucho Marx</name>\
<p><id>123123124</id><name>Harpo Marx</name>\
<p><id>123123125</id><name>Chico Marx</name>\
<randomcrap>Etaoin<id>Shrdlu</id>qwerty</name></randomcrap>\
<nocrap><p><id>123123126</id><name>Zeppo Marx</name></nocrap>\
<address>Chicago</address>\
<morerandomcrap><id>999999999</id>nonametobeseen!\
</morerandomcrap>\
<p><id>123123127</id><name>Gummo Marx</name>\
<note>Look him up on <a href=\"http://www.google.com\">\
Google.</a></note>\
</body></html>"

pidname = re.compile( r"<id>([^<]+)</id><name>([^<]+)</name>" )
mlist = pidname.finditer( text )
for m in mlist:
    print( m.group(1), m.group(2) )
```

### Chapter 27

#### Answer 26.1

```python
from csv import reader, writer

fp = open( "pc_inventory.csv", newline='' )
fpo = open( "pc_writetest.csv", "w", newline='' )
csvreader = reader( fp )
csvwriter = writer( fpo, delimiter=' ', quotechar="'" )
for line in csvreader:
    csvwriter.writerow( line )
fp.close()
fpo.close()

fp = open( "pc_writetest.csv" )
print( fp.read() )
fp.close()
```

If you did it correctly, you notice the quotes around "Blue Stilton,"
which are there because it contains a space, which is the delimiter.

#### Answer 26.2

```python
from csv import reader
from json import dump

data = []

fp = open( "pc_inventory.csv", newline='' )
csvreader = reader( fp )
for line in csvreader:
    data.append( line )
fp.close()

fp = open( "pc_writetest.json", "w" )
dump( data, fp )
fp.close()

fp = open( "pc_writetest.json" )
print( fp.read() )
fp.close()
```

### Chapter 28

#### Answer 27.1

```python
from collections import Counter

sentence = "Your mother was a hamster and \
your father smelled of elderberries."
sentence2 = ""
for c in sentence.lower():
    if c >= 'a' and c <= 'z':
        sentence2 += c

clist = Counter( sentence2 ).most_common( 5 )
for c in clist:
    print( "{}: {}".format( c[0], c[1] ) )
```

#### Answer 27.2

```python
from collections import Counter
from pcinput import getInteger
from statistics import mean, median
from sys import exit

numlist = []
while True:
    num = getInteger( "Enter a number: " )
    if num == 0:
        break
    numlist.append( num )

if len( numlist ) <= 0:
    print( "No numbers were entered" )
    exit()

print( "Mean:", mean( numlist ) )
print( "Median:", median( numlist ) )

clist = Counter( numlist ).most_common()
if clist[0][1] <= 1:
    print( "There is no mode" )
else:
    mlist = [str( x[0] ) for x in clist if x[1] == clist[0][1] ]
    s = ", ".join( mlist )
    print( "Mode:", s )
```

For the mode I did a reasonably smart list comprehension, but you can
write this out as multiple lines of code, of course.
