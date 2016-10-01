from mklibpy.common.vector import *

__author__ = 'Michael'

vec = Vector(1, 2, 3)
print(repr(vec))
print(vec.slice(1, 2))
print(vec.extend(5, Vector, 0))
print(-vec)
print(vec + Vector(4, 5, 6))
print(vec.length())
print(vec * 3)
print(3 * vec)


@Vector2.convert_attr("pos")
class A(object):
    def __init__(self, pos):
        self.pos = pos


a = A((0, 1))
print(a.pos.length())
a.pos = (5, 6)
print(repr(a.pos))
print(a.pos.length())

print(repr(Vector3.zero))
print(repr(Vector3.YUnit))
print(repr(Vector3(*a.pos, zero=0)))
