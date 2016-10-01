from mklibpy.common.vector import Vector, Vector2
from mklibpy.util.collection import format_dict_multiline

__author__ = 'Michael'

print(format_dict_multiline(Vector.__dict__))
print(format_dict_multiline(Vector2.__dict__))


@Vector2.convert_params("axes")
def get_pos(axes):
    return axes


@Vector2.convert_params("pos")
class C1(object):
    def __init__(self, pos):
        self.pos = pos

    def pr(self, pos):
        print(repr(pos))


print(repr(get_pos((1, 0))))

c1 = C1((1, 2))
print(repr(c1.pos))
c1.pr((6, 6))


@Vector2.convert_attr("pos")
class C2(object):
    def __init__(self):
        self.pos = (0, 0)


c2 = C2()
print(repr(c2.pos))
c2.pos = (3, 6)
print(repr(c2.pos))
