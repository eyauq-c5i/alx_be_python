import math

class Shape:
    def area(self):
        """Base method to be overridden by subclasses."""
        raise NotImplementedError("Subclasses must override area()")


class Rectangle(Shape):
    def __init__(self, length, width):
        """Initialize rectangle with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Calculate area of rectangle: length × width."""
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        """Initialize circle with radius."""
        self.radius = radius

    def area(self):
        """Calculate area of circle: π × radius²."""
        return math.pi * self.radius ** 2