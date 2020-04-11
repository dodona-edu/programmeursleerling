There are methods available to define what should happen when you
combine an instance of a class with a value using a regular calculation
operator. The most important of these are:

-   `__add__()` for addition (`+`)

-   `__sub__()` for subtraction (`-`)

-   `__mul__()` for multiplication (`*`)

-   `__truediv__()` for division (`/`)

-   `__floordiv__()` for integer division (`//`)

-   `__mod__()` for modulo (`\%`)

-   `__pow__()` for power (`**`)

-   `__lshift__()` for left shift (`<<`)

-   `__rshift__()` for right shift (`>>`)

-   `__and__()` for bitwise `and` (`\&`)

-   `__or__()` for bitwise `or` (`|`)

-   `__xor__()` for bitwise `xor` (`\^`)

For example, for quaternions the addition is defined as:
$(A + Bi + Cj + Dk) + (E + Fi + Gj + Hk) = (A+E) + (B+F)i + (C+G)j + (D+H)k$.
Naturally, you can also add integers and floats to quaternions. This can
be implemented as follows:

```python
class Quaternion:
    def __init__( self, a, b, c, d ):
        self.a, self.b, self.c, self.d = a, b, c, d
    def __repr__( self ):
        return "({},{}i,{}j,{}k)".format( self.a, self.b, 
            self.c, self.d )
    def __add__( self, n ):
        if isinstance( n, int ) or isinstance( n, float ):
            return Quaternion( n+self.a, self.b, self.c, self.d )
        elif isinstance( n, Quaternion ):
            return Quaternion( n.a + self.a, n.b + self.b, \
                n.c + self.c, n.d + self.d )
        return NotImplemented

c1 = Quaternion( 3, 4, 5, 6 )
c2 = Quaternion( 1, 2, 3, 4 )
print( c1 + c2 )
print( c1 + 10 )
```

If a calculation operator is used with your new class as the right
operand, and the left operand does not support the operator with your
new class (it returns `NotImplemented`), Python checks if your new class
supports the operation as the right operand. For that, you need to
implement extra methods, which have the same names as the methods above,
but with an `r` in front of the name, e.g., `__radd__()` is the addition
operator with corresponding object as the right operand (all the other
methods can be created in this way too).

The code above will actually produce a runtime error if you try to
calculate `10 + c1` (try it). You will have to implement `__radd__()` to
solve that.

```python
class Quaternion:
    def __init__( self, a, b, c, d ):
        self.a, self.b, self.c, self.d = a, b, c, d
    def __repr__( self ):
        return "({},{}i,{}j,{}k)".format( self.a, self.b, 
            self.c, self.d )
    def __add__( self, n ):
        if isinstance( n, int ) or isinstance( n, float ):
            return Quaternion( n+self.a, self.b, self.c, self.d )
        elif isinstance( n, Quaternion ):
            return Quaternion( n.a + self.a, n.b + self.b, \
                 n.c + self.c, n.d + self.d )
        return NotImplemented
    def __radd__( self, n ):
        return self.__add__( n )

c1 = Quaternion( 3, 4, 5, 6 )
print( 10 + c1 )
```

As you see, I resolved the problem by making `__radd__()` a direct call
to `__add__()`. You might wonder why Python does not do that
automatically. The reason is mathematical: while in many cases `+` is
"commutative," i.e., you can exchange the operands without the result
changing, this is definitely not always the case. But if your addition
operator is commutative, a simple call from `__radd__()` to `__add__()`
will do the trick.

For the shorthand operators `+=`, `-=`, `*=`, etcetera, you can also
define separate methods. These have the same names as the methods above,
but with an `i` in front of the name, e.g., `__iadd__()` implements the
`+=` operator (again, for all the other methods you can create this
variant too). These methods should actually modify `self`, and also
`return` the result (usually `self`). If they are not implemented,
Python reverts to the regular interpretation, i.e., if a statement is
`x += y`, then Python tries to execute `x.__iadd__(y)`, and if that
returns `NotImplemented`, it will execute `x = x.__add__(y)`. Thus, in
general you do not need to implement methods for the shorthand
operators.

Extend the `Quaternion` class with subtraction. Subtraction works
similar to addition, except all the pluses are replaced by minuses. Note
that subtraction is not commutative, so you cannot implement
`__rsub__()` by a simple call to `__sub__()`. However, it is not hard to
implement `__rsub__()`, so make sure that you do it.
