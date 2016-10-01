from mklibpy.code.clazz import get_self_members, get_all_members
from mklibpy.code.types import is_class_method
from mklibpy.util.collection import format_dict_multiline

__author__ = 'Michael'


class A(list):
    def f(self):
        pass


print(format_dict_multiline(get_self_members(A)))
print(format_dict_multiline(get_all_members(A)))


def f(name, item):
    return is_class_method(item)


print(format_dict_multiline(get_all_members(A, f)))
