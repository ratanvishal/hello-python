import time

initial = time .time()
print(initial)
k=0
initial1=time.time()
while k<45:
    print("this is vishal")
    time.sleep(1)
    k+=1
print("while loop in the printing",time.time()-initial1,"mili seconds")
initial2= time.time()
for i in range (45):
    print("this is pavan")
    time.sleep(1)
print("while loop in the printing",time.time()-initial2,"mili seconds")
initial3=time.time()
print("\ntotal time of execution\n",f"{time.time()+initial1+initial2}")
print("\nthe average time for execution\n",f"{(time.time()+initial1+initial2)/3}")









