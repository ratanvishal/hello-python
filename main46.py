class A:
    def met(self):
        print("This is the methodfrom class A")
class B(A):
    def met(self):
        print("This is the methodfrom class B")
class C(A):
    def met(self):
        print("This is the methodfrom class C")
class D(C,B):
    def met(self):
        print("This is the methodfrom class D")
a=A()
b=B()
c=C()
d=D()

d.met()

