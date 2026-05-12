class A:
    label = "A: Base Class"

class B(A):
    label  = "B:  B Class"

class C(A):
    label = " C: C Class"

class D(B,C):
    pass

cup = D()

print(cup.label)
print(D.__mro__)
# Method Resoultion Order