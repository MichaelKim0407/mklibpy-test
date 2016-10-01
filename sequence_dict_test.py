from mklibpy.common.collection import SequenceDict

__author__ = 'Michael'

d = SequenceDict("x", "y", x=3)
print(d)

d["0"] = 2
d["x"] = 5
print(d)

d.insert(1, "2", 3)
print(d)

d.sort()
print(d)

d.reverse()
print(d)

print(d.pop_at(0))
print(d)

print(d.keys())
print(d.values())

del d['x']
print(d)

print(d.index('0', 1))

d["3"] = 100
d.sort_by_value(reverse=True)
print(d)
