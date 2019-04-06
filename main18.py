# with open("fileio2.text") as f:
#         a=f.readlines()
#         print(a)

# x=10
# def function1(n):
#     print(n,"this is printed")
# function1("this is vishal")
# function1("this is vishal")
# function1("vishal")
# function1("this is ishal")
# function1("this is v")

# x=10 #global variavble
# def function1(n):
#     #x=45
#     z=35
#     global x
#     x=x+39
#
#     print(x,z)
#     print(n,"this printed")
# function1("vishal is great")
# print(x)
x=67
def vishal():
    x=20
    def rohan():
      global x
      x=45
    print("before calling rohan",x)
    rohan()
    print("after callig rohan",x)
vishal()
print(x)















