Now the basic philosophies of object orientation are out of the way, I
am going to discuss how to use object orientation in Python. It starts
with creating new classes using the keyword `class`.

### `class`

A class can be considered a new data type. Once a class is created, you
can assign instances of the class to variables. To start simple, I am
going to create a class that represents a point in 2D space. I name this
class `Point` (the naming of classes is restricted to the same
requirements as the naming of variables, and it is convention to let the
names of classes start with a capital). Creating this class in Python is
incredibly easy:

```python
class Point:
    pass
```

The keyword `pass` in the class definition means "do nothing." This
keyword can be used wherever you need to place a statement, but you have
nothing yet to place there. You cannot just leave it empty or give a
comment and nothing else. But as soon as statements are added, you no
longer need `pass`.

To create an object that is an instance of the class, I assign to a
variable the name of the class, with parentheses after it, as if it is a
function call (you can have arguments between the parenthesis, which
will be discussed a bit later in this chapter).

```python
class Point:
    pass

p = Point()
print( type( p ) )
```

Of course, a point is more than just an object. A point has an x and a y
coordinate. Since Python is a soft-typed language, you need to assign
values to attributes to create them. This is done in a special
initialization method in the class.

![OO](media/OO.png "OO"){:width="70%"}

### `__init__()`

The initialization method of a class has the name `__init__` (that's two
underscores, followed by the word `init`, followed by two more
underscores). Even if the `__init__()` method is not defined explicitly
for the class, it still exists. You use the `__init__()` method to
initialize everything that you want to initialize upon creation of an
instance of the class.

In the case of `Point`, `__init__()` should assure that any `Point`
object has an `x` and a `y` coordinate. This is implemented as follows:

```python
class Point:
    def __init__( self ):
        self.x = 0.0
        self.y = 0.0

p = Point()
print( "({}, {})".format( p.x, p.y ) )
```

Study the code above closely. You see that `__init__()` is defined just
as you would define a function, inside the class definition.

`__init__()` gets one parameter, which is called `self`. Every method
that you define, always gets at least one parameter, which will get
filled with a reference to the object for which the method is called. By
convention, this first parameter is always called `self`. That is not
mandatory, but everybody always does it like this. If you forget to
include that first parameter, you will get a runtime error. If you
forget to include the first parameter `self` but you do have other
parameters, Python will fill the first of the parameters that you do
list with a reference to the object, and you will probably also get a
runtime error (as you did not expect that that would happen).

In the `__init__()` method for `Point`, the object that is created gets
two attributes, which are variables that are part of the object. They
are called `x` and `y`, and since they are part of the object, you refer
to them as `self.x` and `self.y`. They both get initial value 0.0, which
makes them floats.

To refer to these attributes when the object has been created, you use
the syntax `<object>.<attribute>`, as you can see on the last line of
the code, where the object that has just been created is used in a
`print()` statement.

You might wonder if you can only create attributes for an object in the
`__init__()` method. The answer is: no, you can create attributes in
other methods too, and even outside the class definition.

```python
class Point:
    def __init__( self ):
        self.x = 0.0
        self.y = 0.0

p = Point()
p.z = 0.0
print( "({}, {}, {})".format( p.x, p.y, p.z ) )
```

Most Python programmers (including me) would consider what happens in
the code above bad form. It is good practice to create all the
attributes that you need exclusively in the `__init__()` method (though
you can change their values elsewhere), so that you know that every
instance of the class has them, and no instances have more.

If you do need a version of the class with extra attributes, you can use
"inheritance" to create new classes based on existing ones, which do
have these extra attributes. Inheritance will be discussed in a later
chapter. For now, make sure that you create classes with all their
attributes defined in the `__init__()` method.

Like any method, `__init__()` can get arguments. You can use such
arguments to initialize (some of) the attributes. For instance, if I
want to create an instance of `Point` while immediately specifying the
values for the `x` and `y` coordinates, I can use the following class
definition:

```python
class Point:
    def __init__( self, x, y ):
        self.x = x
        self.y = y

p = Point( 3.5, 5.0 )
print( "({}, {})".format( p.x, p.y ) )
```

`__init__()` is now defined with three parameters. The first is still
`self`, as it always has to be there. The second and third are called
`x` and `y`. I could have called them anything I like (within the
boundaries of variable naming), but I went for `x` and `y` as these are
the most logical names. I assign `x` to `self.x`, and `y` to `self.y`.

I call the creation of a point now with values for the `x` and `y`
coordinates as arguments. The first argument will be passed to the
method in the second parameter, and the second in the third parameter,
as the first parameter will be used to pass the reference to the object
itself.

If you want to make it optional for the programmer to pass such values,
you can give the parameters default values using an assignment in the
parameter specification, as follows:

```python
class Point:
    def __init__( self, x=0.0, y=0.0 ):
        self.x = x
        self.y = y

p1 = Point()
print( "({}, {})".format( p1.x, p1.y ) )

p2 = Point( 3.5, 5.0 )
print( "({}, {})".format( p2.x, p2.y ) )
```

Create a list of all the points with integer coordinates, with both
their `x` and `y` coordinates ranging from 0 to 3.

### `__repr__()` and `__str__()`

In the code above, I print the point attributes. What happens if I try
to print the point itself?

```python
class Point:
    def __init__( self, x=0.0, y=0.0 ):
        self.x = x
        self.y = y

p = Point( 3.5, 5.0 )
print( p )
```

Try it, and you will agree that the result is not very informative. When
I print a point, I want to see the coordinates. Python offers another
predefined method for that, which is `__repr__()`. `__repr__()` should
return a string, which contains what you want to see when an object is
displayed.

```python
class Point:
    def __init__( self, x=0.0, y=0.0 ):
        self.x = x
        self.y = y
    def __repr__( self ):
        return "({}, {})".format( self.x, self.y )

p = Point( 3.5, 5.0 )
print( p )
```

That looks much better.

Python offers yet another standard method for creating a string version
of an object, namely `__str__()`. `__str__()` is the same as
`__repr__()`, but it is only used when the object is being printed or
passed to a `format()` method. If `__str__()` is not defined, it is the
same as `__repr__()` (but not vice versa). If `__str__()` is defined,
you can ensure that something different is shown when `print()` is used,
than what is shown in other places.

You now might think: "what other places?" The main "other place" where
objects are displayed is in the command shell, when you just type the
name of the variable that contains an object.

It is commonly understood that in the `__repr__()` method you are
supposed to return a string that contains each and every bit of
information that is needed to recreate an object, while in `__str__()`
you can just return a string that contains a nicely formatted
representation of the most important information that you want to see in
the program. Very often, these two are the same.

Many programmers ignore `__repr__()` altogether and only define
`__str__()`. I think this is the wrong way around: you should always
define `__repr__()`, while `__str__()` is optional. If you use
`__repr__()`, make sure that you indeed return all details of an object.
If you leave things out, it is better to just use `__str__()`.

Expand the `Point` class with a `color` attribute. A `color` is
represented by a number between 0 and $$2^{24}-1$$. Make sure the color is
used both in the `__init__()` method and in the `__repr__()` method.
