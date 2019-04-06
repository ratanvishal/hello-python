# addition = lambda a,b,:a+b
# print(addition(2,3))
#
# def a_first(a):
#
#     return(a[1])
# a = [[1,2],[19,56],[56,6],[23,54],[12,23]]
# a.sort(key=a_first)
# print(a)
a = [[1,2],[19,56],[56,6],[23,54],[12,23]]
a.sort(key=lambda a:a[0])
print(a)