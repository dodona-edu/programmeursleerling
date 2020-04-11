Unary operators are operators which work only on the object itself, so
not in combination with another object. A typical example is using the
minus (`-`) sign in front of a number to turn it into a negative number.
You can overload some of the unary operators, and also some of the basic
functions that work on an object.

-   `__neg__()` implements the negation (`-`) of an object

-   `__pos__()` implements placing a plus (`+`) in front of an object
    (usually without effect)

-   `__invert__()` implements the bitwise `not` (`\~`)

-   `__abs__()` implements taking the object's absolute value when using
    the `abs()` function

-   `__int__()` implements taking the (rounded down) integer value of an
    object when using the `int()` function; must return an integer

-   `__float__()` implements taking the floating-point value of an
    object when using the `float()` function; must return a float

-   `__round__()` implements rounding using the `round()` function. An
    optional second argument can be given to specify the number of
    decimals; must return an integer or a float

-   `__bytes__()` implements representing the object as a byte string.
    It is in that respect similar to the `__str__()` method which was
    discussed in Chapter
    <a href="#ch:objectorientation" data-reference-type="ref" data-reference="ch:objectorientation">21</a>

```python
class Quaternion:
    def __init__( self, a, b, c, d ):
        self.a, self.b, self.c, self.d = a, b, c, d
    def __repr__( self ):
        return "({},{}i,{}j,{}k)".format( self.a, self.b, 
            self.c, self.d )
    def __neg__( self ):
        return Quaternion( -self.a, -self.b, -self.c, -self.d)
    def __abs__( self ):
        return Quaternion( abs( self.a ), abs( self.b ), 
            abs( self.c ), abs( self.d ) )
    def __bytes__( self ):
        return self.__str__().encode( "utf-8" )

c1 = Quaternion( 3, -4, 5, -6 )
print( c1 )
print( -c1 )
print( abs( c1 ) )
print( bytes( c1 ) )
```

{:class="callout callout-info"}
> #### Note
> You might think it would be a good idea to also implement the
> `__int__(),` `__float__()`, and `__round__()` methods, that,
> respectively, use the `int()`, `float()`, and `round()` functions on
> `self.a`, `self.b`, `self.c`, and `self.d`. Unfortunately, that cannot
> be done, as these methods must return integers or floats, and not
> `Quaternion`s. Other than what I propose, I see no sensible
> interpretation of `int()`, `float()`, and `round()` for `Quaternion`, so
> these methods should not be implemented.
