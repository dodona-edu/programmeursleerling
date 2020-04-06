Using the operators you have learned about above, you can change the
variables in your code as many times as you want. You can assign new
values to existing variables. Very often, you want to make changes to
existing variables. For instance, it is common in code that you want to
add 1 to a number (you will find out why that is in a later chapter).
Since this occurs fairly often, Python offers some shorthand notation to
deal with changes to variables.

The following code:

```python
number_of_bananas = 100
number_of_bananas = number_of_bananas + 1
print( number_of_bananas )
```

is equivalent to:

```python
number_of_bananas = 100
number_of_bananas += 1
print( number_of_bananas )
```

The difference is in the second line. If you want to add something to a
variable, you can write `+=` as the assignment operator and to the
right-hand side of the `+=` the thing that you want to add to the
variable. This saves you the trouble of repeating the variable name at
the right-hand side, and tends to make your code more readable (because
programmers expect you to code "adding something to an existing
variable" with the `+=` operator).

Similar to the `+=` operator, you can use `-=` to subtract something
from a variable, `*=` to multiply a variable by something, `/=` to
divide a variable by something, `**=` to raise a variable to a power,
and `\%=` to turn a variable into itself modulo the right-hand side.
Most of these are uncommon, except for the `+=`, which is used a lot,
and the `-=`, which is used occasionally.

What will the code given below display? Run it to see if you are
correct.

```python
number_of_bananas = 100
number_of_bananas += 12
number_of_bananas -= 13
number_of_bananas *= 19
number_of_bananas /= number_of_bananas
print( number_of_bananas )
```
