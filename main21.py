# Exercise 4
# Pattern Printing
# Input = Integer n
# Boolean = True or False
#
# True n=5
# v
# vv
# vvvv
# vvvvv
#
# False n=5
# vvvvv
# vvv
# vv
# v
print("star the v printing game")
a = int(input("please type the rows you wanna print\n"))
b = bool(int(input("pls 0=top-bottom or 1=bottom-up\n ")))
def vishal(a,b):
    if b==True:
        c=1
        while(c<=a):
            print(c*"v")
            c=c+1

    else:
        while(a>0):
         print(a*"v")
         a=a-1

vishal(a,b)



