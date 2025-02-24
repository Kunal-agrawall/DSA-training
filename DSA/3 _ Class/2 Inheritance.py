# Single
class Ryukendo:
    def Shot(self):
        print("I am Owner.")

class GekkiRyuken(Ryukendo):
    def Weapon(self):
        print("I am inheriting my Owner.")

Kenji = GekkiRyuken()
Kenji.Shot()
Kenji.Weapon()


# Multi Level
class A:
    def m1(self):
        print("A executed.")

class B(A):
    def m2(self):
        print("B executed.")

class C(B):
    def m3(self):
        print("C executed.")

class D(C):
    def m4(self):
        print("D executed.")

obj = D()
obj.m1()
obj.m2()
obj.m3()
obj.m4()


# Multiple
class X:
    def m1(self):
        print("X executed.")

class Y:
    def m2(self):
        print("Y executed.")

class Z(X,Y):
    def m3(self):
        print("Z executed.")

obj2 = Z()
obj2.m1()
obj2.m2()
obj2.m3()


# Hierarchical
class P:
    def m1(self):
        print("P executed.")

class Q(P):
    def m2(self):
        print("Q executed.")

class R(P):
    def m3(self):
        print("R executed.")

ob2 = R()
ob2.m3()


# Hybrid
class A:
    def m1(self):
        print("A executed.")

class B(A):
    def m2(self):
        print("B executed.")

class C(A):
    def m3(self):
        print("C executed.")

class D(B,C):
    def m4(self):
        print("D executed.")

obj = D()
obj.m1()