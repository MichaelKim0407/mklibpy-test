from mklibpy.common.string import *

__author__ = 'Michael'

c = AnyString(["a b", "b", "c"])

print(c == "b", bool("b" == c))
print(c.__contains__("a"), "a" in c)
print(c.split())
print("a" in c.split())

try:
    AnyString([1, 2])
except Exception as e:
    print(e)

s = String("a b c d")
sc = s.split()
print(sc)
print(sc.items())
print(s.startswith(sc))

sc += ".x"
print(sc)

sc.add("gh")
a = sc.endswith(".x")
print(a)
print(len(a))
