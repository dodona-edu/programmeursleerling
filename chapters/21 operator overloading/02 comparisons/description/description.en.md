In Chapter
21
I discussed that objects can be aliases of each other, but that you can
also make actual copies. What happens if you try to compare them?

```python
class Point:
    def __init__( self, x=0.0, y=0.0 ):
        self.x = x
        self.y = y
    def __repr__( self ):
        return "({}, {})".format( self.x, self.y )

p1 = Point( 3, 4 )
p2 = Point( 3, 4 )
p3 = p1
print( p1 is p2 )
print( p1 is p3 )
print( p1 == p2 )
print( p1 == p3 )
```

The keyword `is` compares object identities. Since `p3` is an alias for
`p1`, `p1 is p3` returns `True`, while `p1 is p2` returns `False`.
However, since `p1` and `p2` refer to the same point in 2D space, it
would be nice if `p1 == p2` would return `True`, i.e., that the `==`
would do a value comparison (as you would expect). It does not. That is
not surprising, as Python does not know how to compare the values of
`Point`s, and therefore the `==` does the only comparison that Python
knows how to do, namely an identity comparison. However, you can
instruct Python how to compare two points using the == operator, by
defining an `__eq__()` method:

```python
class Point:
    def __init__( self, x=0.0, y=0.0 ):
        self.x = x
        self.y = y
    def __repr__( self ):
        return "({}, {})".format( self.x, self.y )
    def __eq__( self, p ):
        return self.x == p.x and self.y == p.y

p1 = Point( 3, 4 )
p2 = Point( 3, 4 )
p3 = p1
print( p1 is p2 )
print( p1 is p3 )
print( p1 == p2 )
print( p1 == p3 )
```

The `__eq__()` method tells Python, in this case, what to do when two
objects of the type `Point` are compared with `==`. It returns `True`
when their `x` and `y` coordinates are equal, `False` otherwise. In this
example, the interpretation of the comparison operator `==` is
"overloaded" by defining the `__eq__()` method.

You can also overload the other comparison operators `\`=!, `>`, `>=`,
`<`, and `<=`:

-   `__eq__()` for equality (`==`)

-   `__ne__()` for inequality (`\`=!)

-   `__gt__()` for greater than (`>`)

-   `__ge__()` for greater than or equal to (`>=`)

-   `__lt__()` for less than (`<`)

-   `__le__()` for less than or equal to (`<=`).

If you specify the `__eq__()` method but not the `__ne__()` method, the
`__ne__()` method will automatically return the opposite of what the
`__eq__()` method returns. None of the other methods have such an
automatic interpretation.

You are not limited to comparing only objects that are instances of the
same class. For instance, when I define a class `Quaternion` that
implements a quaternion, I might want to compare a quaternion with an
integer or a float. That is possible:

```python
class Quaternion:
    def __init__( self, a, b, c, d ):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    def __repr__( self ):
        return "({},{}i,{}j,{}k)".format( self.a, self.b,
            self.c, self.d )
    def __eq__( self, n ):
        if isinstance( n, int ) or isinstance( n, float ):
            if self.a == n and self.b == 0 and \
                self.c == 0 and self.d == 0:
                return True
            else:
                return False
        elif isinstance( n, Quaternion ):
            if self.a == n.a and self.b == n.b and \
                self.c == n.c and self.d == n.d:
                return True
            else:
                return False
        return NotImplemented

c1 = Quaternion( 1, 2, 3, 4 )
c2 = Quaternion( 1, 2, 3, 4 )
c3 = Quaternion( 3, 0, 0, 0 )
if c1 == c2:
    print( c1, "==", c2 )
else:
    print( c1, "!=", c2 )
if c1 == c3:
    print( c1, "==", c3 )
else:
    print( c1, "!=", c3 )
if c3 == 1:
    print( c3, "==", 1 )
else:
    print( c3, "!=", 1 )
if c3 == 3:
    print( c3, "==", 3 )
else:
    print( c3, "!=", 3 )
if c3 == 3.0:
    print( c3, "==", 3.0 )
else:
    print( c3, "!=", 3.0 )
if c3 == "3":
    print( c3, "== \"3\"" )
else:
    print( c3, "!= \"3\"" )
if 3 == c3:
    print( 3, "==", c3 )
else:
    print( 3, "!=", c3 )
```

The implementation of the `__eq__()` method in the code above checks if
the value the comparison is made with is a `Quaternion`, an integer, or
a float. If so, it makes the comparison and returns `True` or `False`.
If not, it returns `NotImplemented`. `NotImplemented` is a special value
that indicates that the comparison has no sensible outcome. While the
`__ne__()` method automatically inverts the result of the `__eq__()`
method, it will not (and cannot) invert `NotImplemented`.

The last comparison in the code above is noteworthy. It executes
comparison `3 == c3`. Normally, when the comparison operator is defined,
it will be executed for the left operand, i.e., the comparison operator
of the integer 3 is executed, with `c3` as argument. However, integers
have not defined the `__eq__()` method for `Quaternion`, and thus this
returns `NotImplemented`. If that happens, Python inverts the operands,
so in this case executes the comparison `c3 == 3`. This comparison leads
to a result as for `Quaternion` the comparison with an integer is
defined. The same happens with the `\`=! operator. Something similar is
done for the other comparison operators, but when the operands are
inverted, `<` is swapped with `>`, and `<=` is swapped with `>=`, just
as you would expect.

In Chapter
21,
a `Rectangle` class was defined. Add to this class operators to test for
equality of rectangles (two rectangles are equal if they have exactly
the same shape), and greater/smaller operators (a rectangle is smaller
than another rectangle if it has a smaller surface area). Test the new
operators. Note: I am a bit on the fence on whether these are acceptable
definitions for equality and the other comparisons, but for practice
they are okay.

There is one special comparison I want to bring up, and that is testing
whether an object is `True` or `False`. Many objects are considered to
be `False` in particular circumstances; for instance, and empty list
evaluates to `False`. This was briefly discussed in Chapter
7.

```python
buffer = []
if buffer:
    print( buffer )
else:
    print( "buffer is empty" )
```

You can define your own evaluation of an object that is called when the
object is used as condition. This is the `__bool__()` method.

`__bool__()` is called when an object is treated as a condition. It must
return `True` or `False`. If `__bool__()` is not implemented,
`__len__()` is called (see below), which will evaluate to `False` if
`__len__()` returns zero. If neither `__bool__()` nor `__len__()` is
implemented, the object is always `True` when used as condition.
