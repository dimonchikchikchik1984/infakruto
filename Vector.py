import numpy as np


class Vector:
    x = None
    y = None
    z = None

    v = np.zeros((1, 1))

    def __init__(self, *args, **kwargs):

        self.v = np.array(*args, **kwargs)

        try:
            if type(args[0]) == str:
                self.v = np.array([float(x) for x in args[0].split(',')])
        except IndexError:
            pass

        try:
            self.x, self.y, self.z = self.v[0], self.v[1], self.v[2]
        except IndexError:
            pass

    def __str__(self):
        return self.v.__str__()

    def __repr__(self):
        return self.v.__repr__()

    def __and__(self, other):
        return Vector(np.cross(self.v, other.v))

    def __mul__(self, other):
        return np.dot(self.v, other.v)

    def __add__(self, other):
        return Vector(self.v + other.v)

    def T(self):
        return Vector(self.v.T)

    def shape(self):
        return self.v.shape

    def norm(self):
        return np.linalg.norm(self.v)

    def __sub__(self, other):
        return Vector(self.v - other.v)

    def __eq__(self, other):
        return self.v == other.v

    def ravel(self):
        return Vector(self.v.ravel())

    def conj(self):
        return Vector(self.v.conj())

    def copy(self, **kwargs):
        return Vector(self.v.copy(**kwargs))

    def reshape(self, shape, **kwargs):
        return Vector(self.v.reshape(shape, **kwargs))

    def sort(self, **kwargs):
        return Vector(self.v.sort(**kwargs))

    def trace(self, **kwargs):
        return Vector(self.v.trace(**kwargs))

    def all(self, **kwargs):
        return self.v.all(**kwargs)

    def any(self, **kwargs):
        return self.v.any(**kwargs)