import math

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError("The coordinates must be non-empty")
        except TypeError:
            raise TypeError("The coordinates must be iterable")

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def magnitude(self):
        return math.sqrt(sum([x * x for x in self.coordinates]))

    def normalize(self):
        try:
            return Vector.scalar_multiply(self, 1 / self.magnitude())
        except ZeroDivisionError:
            raise Exception("Cannot normalize the zero vector")

    @staticmethod
    def add(v1, v2):
        if v1.dimension != v2.dimension:
            raise ValueError("Both vectors must be the same dimension to be added together")
        return Vector([x + y for x, y in zip(v1.coordinates, v2.coordinates)])

    @staticmethod
    def subtract(v1, v2):
        if v1.dimension != v2.dimension:
            raise ValueError("Both vectors must be the same dimension to be added together")
        return Vector([x - y for x, y in zip(v1.coordinates, v2.coordinates)])

    @staticmethod
    def scalar_multiply(v1, scalar):
        return Vector([x * scalar for x in v1.coordinates])

    @staticmethod
    def dot_product(v1, v2):
        return sum([x * y for x, y in zip(v1.coordinates, v2.coordinates)])

    @staticmethod
    def angle(v1, v2, deg=False):
        angle = math.acos(Vector.dot_product(v1.normalize(), v2.normalize()))
        return angle * (180 / math.pi) if deg else angle

# these are likely wrong
    @staticmethod
    def parallel(v1, v2):
        return v1.normalize() == v2.normalize()

    @staticmethod
    def orthogonal(v1, v2):
        return Vector.dot_product(v1, v2) == 0

test1 = Vector([7.579, -7.88])
test2 = Vector([22.737, 23.764])
print(Vector.parallel(test1, test2))
print(Vector.orthogonal(test1, test2))

test1 = Vector([-2.029, 9.97, 4.172])
test2 = Vector([-9.231, -6.639, -7.245])
print(Vector.parallel(test1, test2))
print(Vector.orthogonal(test1, test2))
