# v="vishal"
# ier=iter(v)
#
# print(ier.__next__())
# print(ier.__next__())
# print(ier.__next__())
# print(ier.__next__())

# item=12
# print(item.__getitem__())

def gen(n):
    for i in range(n):
        yield i
g=gen(7)
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
for i in g:
    print(i)