# numbers=["67","78","89","75","45"]
# numbers=list(map(int, numbers))
# # for i in range(len(numbers)):
# #     numbers[i]=int(numbers[i])
# numbers[2]=numbers[2]+10
# # print(numbers[2])
# def cubic(a):
#     return  a*a*a
# # num=[2,3,6,8,7,1]
# # cubic = list(map(cubic, num))
# # print(cubic)
#
# num=[2,3,6,8,7,1]
# cubic = list(map(lambda b:b*b*b, num))
# print(cubic)
# import time
# m=time.time()
# v=f"{m}","secound's"
# print(v)
# def one(a):
#     return a
# def sq(a):
#     return a*a
# def cube(a):
#     return a*a*a
# def fou(a):
#     return a*a*a*a
# def fiv(b):
#     return b*b*b*b*b
# vishal=[one, sq, cube, fou,fiv]
# for i in range(101):
#     value = list(map(lambda b:b(i),vishal))
#     print(value)
# print(time.time(),"secound's")

# kist=[1,2,3,4,5,6,7,8,9,10,11,12,13,45,4,61,6835,35468,1354,531681,21354,134,1351,5458,135,64,6,43,516,4,35,484,98798,4,54]
# # n=sorted(list(kist))
# # print(n)
# def greater_than10(n):
#     return n>50
# greater_than10=list(filter(greater_than10, kist))
# b=sorted(list(greater_than10))
# print(b)




from functools import reduce

kist1=[4,5,6,2,3,8,6,4,1,2,3,6,4,7,8,9]

num=reduce(lambda a,b:a+b, kist1)

# num=0
# for i in kist1:
#     num=num+i
print(num)

















