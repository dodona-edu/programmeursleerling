Tuples are not used often in Python code (except as return values of
functions). A logical application of tuples would be to deal with values
that always occur in small collections. However, object orientation
(Chapter
<a href="#ch:objectorientation" data-reference-type="ref" data-reference="ch:objectorientation">21</a>
and further) offers many tools and techniques to deal with such small
collections, which means that programmers usually revert to object
orientation when they need something like that.

For the moment, here is an example of the use of tuples in an
application. Suppose that you have to write a program that deals with
geometric figures in 2-dimensional space. A concept that you need is
that of a point: a location in 2D space that is identified by two
coordinates. Rather than write functions that always require a separate
X-coordinate and a separate Y-coordinate, you can specify that
coordinates are always communicated in the form of tuples.

```python
from math import sqrt

# Returns the distance between two points in 2-dimensional space.
# The points are the parameters of the function; each point is a 
# tuple of two numeric values.
def distance( p1, p2 ):
    return sqrt( (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 )

point1 = (1,2)
point2 = (5,5)
print( "Distance between", point1, "and", point2, "is", 
    distance( point1, point2 ) )
```

An advantage of using tuples to communicate coordinates is that it is
relatively easy to write functions that can deal with coordinates in
higher-dimensional spaces too.

```python
from math import sqrt

# Distance between two points in N-dimensional space.
# The points should have the same dimension, i.e., they are tuples 
# of numeric values, and they should have the same length.
def distance( p1, p2 ):
    total = 0
    for i in range( len( p1 ) ):
        total += (p1[i] - p2[i])**2
    return sqrt( total )

# 1-dimensional space
point1 = (1,)
point2 = (5,)
print( "1D: Distance between", point1, "and", point2, "is", 
    distance( point1, point2 ) )

# 2-dimensional space
point1 = (1,2)
point2 = (5,5)
print( "2D: Distance between", point1, "and", point2, "is", 
    distance( point1, point2 ) )

# 3-dimensional space
point1 = (1,2,4)
point2 = (5,5,8)
print( "3D: Distance between", point1, "and", point2, "is", 
    distance( point1, point2 ) )
```
