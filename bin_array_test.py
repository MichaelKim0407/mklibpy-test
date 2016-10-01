from mklibpy.common.collection import BinaryArray

__author__ = 'Michael'

l = BinaryArray([True, False])
print(l.to_int())

try:
    l.append(1)
except TypeError as e:
    print(repr(e))
finally:
    print(l)

print(BinaryArray.from_int(15, 7))

for ba in BinaryArray.iter_all(5):
    print(ba, ba.to_int())

print(BinaryArray.from_int(2 ** 15 + 132, 16).split(4))
