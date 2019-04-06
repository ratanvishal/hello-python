import math
import timeit
me= "vishal"
al =3
gh=45
# a="this is {2} {1} {0}"
# b= a.format(gh,me,al)
# print(b)
a= f"this is {me} {al} {gh} {45*45} {math.cos(45)} {math.atan(180)} "
timeit.timeit("-".join(str(n) for n in range(100)),number=10000)
# print(time.time(),time.clock())
# time.sleep(1)
# print(time.time(),time.clock())
print(a)
print(gh)