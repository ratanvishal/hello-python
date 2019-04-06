s = set()
l=([1,2,3,4,5,6,7])
print(type(s))
s_from_list = set(l)
print(s_from_list)
print(l)
print(len(l))
print(type(l))
print(type(s_from_list))
s.add(10)
s.add(11)
s.add(12)
s.remove(11)
s.add(11)
s1= s.union({20,21,22})
print(s,s1)
print(len(s1),max(s1),min(s1),type(s1))
print(s.isdisjoint(s1))
print(sorted(s1))









