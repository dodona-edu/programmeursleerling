from copy import copy

class Point:

    """
    >>> p = Point(3, 4)
    >>> p
    Point(3, 4)
    >>> print(p)
    Point(3, 4)
    """

    def __init__(self, x=0.0, y=0.0):

        self.x = x
        self.y = y

    def __repr__(self):

        return f'Point({self.x}, {self.y})'

class Rectangle:

    """
    >>> r1 = Rectangle(Point(1, 1), 8, 5)
    >>> r2 = Rectangle(Point(2, 3), 9, 2)
    >>> r1
    Rectangle(Point(1, 1), 8, 5)
    >>> print(r2)
    Rectangle(Point(2, 3), 9, 2)
    >>> r1.surface_area()
    40
    >>> r1.circumference()
    26
    >>> r1.bottom_right()
    Point(9, 6)
    >>> r1.overlap(r2)
    Rectangle(Point(2, 3), 7, 2)
    >>> r2.overlap(Rectangle(Point(0, 0), 2, 2))

    >>> Rectangle(Point(3, 4), -2, 7)
    Traceback (most recent call last):
    AssertionError: invalid rectangle
    """

    def __init__(self, point, width, height):

        assert width > 0, 'invalid rectangle'
        assert height > 0, 'invalid rectangle'

        self.point = copy(point)
        self.width = width
        self.height = height

    def __repr__(self):

        return f'Rectangle({self.point!r}, {self.width}, {self.height})'

    def surface_area(self):

        return self.width * self.height

    def circumference(self):

        return 2 * (self.width + self.height)

    def bottom_right(self):

        return Point(self.point.x + self.width, self.point.y + self.height)

    def overlap(self, r):

        r1, r2 = self, r
        if (
            r1.point.x > r2.point.x or
            (
                r1.point.x == r2.point.x and
                r1.point.y > r2.point.y
            )
        ):
            r1, r2 = r, self

        if (
            r1.bottom_right().x <= r2.point.x or
            r1.bottom_right().y <= r2.point.y
        ):
            return None

        return Rectangle(
            r2.point,
            min(r1.bottom_right().x - r2.point.x, r2.width),
            min(r1.bottom_right().y - r2.point.y, r2.height)
        )


if __name__ == '__main__':
    import doctest
    doctest.testmod()
