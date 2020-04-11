An interface is a class that specifies attributes and methods without an
actual implementation of the methods. The idea is that subclasses
implement the methods, while functions can be defined as working on the
interface class, under the assumption that the methods will be filled
in. Such functions can then be called with instances of the subclasses.

For good understanding, it is probably better to give an example.

Suppose that I want to design an application that works with vehicles.
Maybe it is a travel-planning application that calculates how to get
from point A to point B. The application will have a map containing all
possible points and connections between the points. It will also have a
list of vehicles, with certain vehicles being restricted to specific
points, and connecting only specific points (e.g., planes will only be
available at airports, and only connect to specific other airports,
while boats are only found in harbors and connect to specific other
harbors). The application gets a start and end point as input, and
provides a list of the sort: take the car to drive from start point to
point X, take the plane to fly from point X to point Y, take the bus to
drive from point Y to point Z, and then walk from point Z to the end
point.

This application will need a definition of vehicles. To be able to come
to an optimal travel plan, it must know for each vehicle at what points
it is available, to what points it can travel, and the average speed of
travel (so that you do not get a travel plan that says "walk from
Amsterdam to Moscow"). It might also be a good idea to include a verb
that is used when the plan refers to travel with a vehicle (e.g.,
"walk," "drive," or "fly"). You might need to think a lot about how to
implement such vehicles. A possible approach is to supply each vehicle
with a method that gets a point as argument and that returns whether or
not the vehicle is available at that point, a method that gets a point
as argument and that returns whether or not the vehicle travels to that
point, a method that gets two points and returns the average speed of
travel of the vehicle between those two points, and a method that
returns the verb (I am not saying that this implementation is a good
idea, just that it could potentially be used).

So you can implement a `Vehicle` class as follows:

```python
class Vehicle:
    def __init__( self ):
        self.startpoint = []
        self.endpoints = []
        self.verb = ""
        self.name = ""
    def __str__( self ):
        return self.name
    def isStartpoint( self, p ):
        return NotImplemented
    def isEndpoint( self, p ):
        return NotImplemented
    def travel_speed( self, p1, p2 ):
        return NotImplemented
    def travelVerb( self ):
        return NotImplemented
```

A class like this is called an interface or "abstract class" (there are
subtle differences between interfaces and abstract classes in
computational theory, but for Python these do not matter). It is not to
be used as a class of which you create instances, which is why all
methods return `NotImplemented`. Instead, it is to be used as a template
to inherit subclasses from, that will all create implementations for the
predefined methods. This means that regardless which vehicle subclass
you define later, you will always have to make sure the methods of the
`Vehicle` class are implemented. So functions that make use of instances
of subclasses of `Vehicle` may count on these methods being available.
