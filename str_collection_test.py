from mklibpy.common.collection import AnyCollection
from mklibpy.common.string import *

__author__ = 'Michael'

c = AnyCollection(["a b", "b", "c"])

print(c == "b", "b" == c)
print("a" in c)
print(c.split())
print("a" in c.split())

try:
    StringCollection([1, 2])
except Exception as e:
    print(e)

s = String("a b c d")
sc = s.split()
print(sc)
print(sc.items())
print(bool(s.startswith(sc)))
