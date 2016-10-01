import mklibpy

__author__ = 'Michael'


class A(mklibpy.data.obj.DataObject):
    KeyMap = {"key": "id"}

    def r2(self):
        return self.x ** 2 + self.y ** 2 + self.z ** 2


data = mklibpy.data.load_files(".", ".txt", data1=("A", A))

print(data)
print(data.A)
print(data.A[0].r2())
x = data.A.column("x")
print(x)
print(x.average())
print(data.A.column("r", lambda d: d.r2() ** 0.5).average())
