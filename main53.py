# ls=[]
# for i in range(1000):
#     if i%3==0:
#         ls.append(i)
# print(ls)
#
# ls=[i for i in range(100)if i%3==0]
# print(ls)


# dict1={i:f"item {i}" for i in range(1001) if i%100==0}
# dict1={i:f"item {i}" for i in range(10)}
# dict2={value:key for key, value in dict1.items()}
# print(dict1,"\n", dict2)
# dresses= {dress for dress in ["dress1","dress1","dress1","dress2","dress2"]}
# print(type(dresses))

evens=(i for i in range(100) if i%2==0)
# print(evens.__next__())
# print(evens.__next__())
# print(evens.__next__())
for item in evens:
    print(item)

user1=(1 for list in range(100) if list%3==0)
print(user1)