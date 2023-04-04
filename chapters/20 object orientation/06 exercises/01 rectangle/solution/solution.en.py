class Point:

    """
    >>> p = Point(3, 4)
    >>> p
    Point(3, 4)
    >>> print(p)
    Point(3, 4)
    """

    def __init__(self, x, y):

        self.x = x
        self.y = y

    def __repr__(self):

        return f'Point({self.x}, {self.y})'

    def __eq__(self, other):

        return (self.x, self.y) == (other.x, other.y)

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

        self.point = point
        self.width = width
        self.height = height

    def __repr__(self):

        return f'Rectangle({self.point!r}, {self.width}, {self.height})'

    def __eq__(self, other):

        return (self.point, self.width, self.height) == (other.point, other.width, other.height)

    def surface_area(self):

        return self.width * self.height

    def circumference(self):

        return 2 * (self.width + self.height)

    def bottom_right(self):

        return Point(self.point.x + self.width, self.point.y + self.height)

    def overlap(self, other):

        # determine top-left point
        x1 = max(self.point.x, other.point.x)
        y1 = max(self.point.y, other.point.y)

        # determine bottom-right point
        x2 = min(self.bottom_right().x, other.bottom_right().x)
        y2 = min(self.bottom_right().y, other.bottom_right().y)

        return Rectangle(Point(x1, y1), x2 - x1, y2 - y1) if x1 < x2 and y1 < y2 else None

if __name__ == '__main__':
    import doctest
    doctest.testmod()
