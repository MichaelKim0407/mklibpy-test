from mklibpy.common.collection import SortedList, SortedDict

__author__ = 'Michael'

l = SortedList([1, 5, 4])
print(l)

l.append(3)
print(l)

l += [0]
print(l)

l2 = SortedList(l, reverse=True)
print(l2)

d = SortedDict()
d[1] = 1
d[0] = 0

print(d)

d2 = SortedDict(reverse=True)("a", "c", "b", c=1, b=2, a=3)
print(d2)
