When you write Python programs with basic data types, without thinking
you use operators to add, subtract, multiply, and divide values, to
compare values, and to apply all kinds of standard functionalities. Such
interactions are not defined by default for classes you define yourself,
but Python allows you to specify what should happen when one applies
such an interaction to instances of your class. This is called "operator
overloading."

For instance, suppose that you define a class that represents
quaternions.[^11] You know that adding and multiplying quaternions are
well-defined operations. Therefore, you might want to define what
happens when you combine two of your quaternions with a $+$ operator.
Python allows you to specify that. In fact, Python allows you to specify
what the $+$ operator does for any of your new classes.

Isn't that great? You can define a class `Student`, and then define that
if you add two students together with a $+$ operator, that their ages
are added up. Wonderful, isn't it? No, it isn't. It obviously makes no
sense to add up two students. You might start thinking about what a
natural interpretation of adding up two students would entail, but the
answer is that everything that you can come up with is far-fetched. You
should not define an addition operator for classes which have no natural
addition defined. This is one of the dangers of operator overloading: if
you apply it without thinking, you get nonsensical programs.

Still, operator overloading has powerful applications. In the rest of
this chapter I will introduce some of the most common applications of
operator overloading.

By the way, operator overloading is a typical example of "polymorphism,"
a concept that allows a function to have different results depending on
the type of its arguments. Polymorphism is often hailed as one of the
powerful features of object orientation.

[^11]: Quaternions are an extension of complex numbers. They consist of
    4-dimensional numbers, with a real factor and three imaginary
    factors called `i`, `j`, and `k`, with specific definitions for the
    multiplication of these factors. Details are not important for this
    book, they are just an example of numbers that are not native to
    Python.
