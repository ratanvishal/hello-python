# def factorial_iterartive(n):
#     fac =1
#     for i in range(n):
#      fac = fac*(i+1)
#      return fac
# number = int(input("enter the numer\n"))
# print(factorial_iterartive(number),"the value are came from factorial itatrative",number)
def factorial_itrative(n):
     fac = 1
     for i in range(n):
      fac = fac * (i+1)
     return fac
def factiorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n * factiorial_recursive(n - 1)
def fibonnaci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonnaci(n-1)+fibonnaci(n-2)

number=int(input("enter the number\n"))
print("iterative",factorial_itrative(number))
print("recursive",factiorial_recursive(number))
print("fibonnacci", fibonnaci(number))

