from mklibpy.common.collection import *
from mklibpy.util.collection import format_dict_multiline
from mklibpy.code import *

__author__ = 'Michael'

print(format_dict_multiline(UniqueList.__dict__))
print(format_dict_multiline(clazz.get_self_members(
    UniqueList,
    clazz.filter_name(lambda name: name not in LIST_METHOD_IGNORE),
    clazz.filter_item(types.is_class_method)
)))

l = UniqueList()
l.append(1)
l.extend([2, 3, 4])
l += [5]
l[0] = 6
print(l)
try:
    l.append(2)
except Exception as e:
    print(e)
print(l)

l2 = UniqueList([1, 2])
try:
    l2.append(1)
except Exception as e:
    print(e)
print(l2)
try:
    l2 += [2, 3]
except Exception as e:
    print(e)
print(l2)
print(type(l2))

print(l2 * 3 + [5])

l2 *= 0
print(l2)
