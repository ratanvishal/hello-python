# def function1():
#     print("subscribe now")
# fun2= function1
# del function1
# fun2()
# def fun(num):
#     if num==0:
#         return print
#     if num==1:
#         return sum
# a=fun(1)
# print(a)
# def executor(fun):
#     fun("this")
# executor(print)

def dcc(fun1):
    def nowexe():
        print("Executing the program")
        fun1()
        print("Execution is completed")
    return nowexe
@dcc
def fun2():
    print("vishal is a good boy")
# fun2=dcc(fun2)
fun2()



