

def getdate():
    import datetime
    return datetime.datetime.now()


def gettime():
    import datetime
    return datetime.datetime.now()


def take(v):
    if v==1:
        c = int(input("enter number 1 for execersie,2 for food\n"))
        if (c==1):
          value=input("Type here\n")
          with open("vishal-exe.text","a") as op:
            op.write(str([str(gettime())])+": "+value+"\n")
          print("sucessfully written")
        elif (c==2):
          value=input("Type here\n")
          with open("vishal-food.text","a") as op:
           op.write(str([str(gettime())])+": "+value+"\n")
           print("sucessfully written")
    elif v==2:
        c = int(input("enter number 1 for execersie,2 for food\n"))
        if c == 1:
            value = input("Type here\n")
            with open("pavan-exe.text", "a") as op:
                op.write(str([str(gettime())])+": "+value+"\n")
                print("sucessfully written")
        elif c == 2:
            value = input("Type here\n")
            with open("pavan-food.text", "a") as op:
                op.write(str([str(gettime())])+": "+value+"\n")
                print("sucessfully written")
    elif v==3:
        c = int(input("enter number 1 for execersie,2 for food\n"))
        if c == 1:
            value = input("Type here\n")
            with open("krupa-exe.text", "a") as op:
                op.write(str([str(gettime())]), ":"+value+"\n")
                print("sucessfully written")
        elif c == 2:
            value = input("Type here\n")
            with open("krupa-food.text", "a") as op:
                op.write(str([str(gettime())]), ":"+value+"\n")
                print("sucessfully written")
    else:
        print("enter the valid input 1[vishal],2[pavan],3[krupa]")
def retrive(v):
    if v==1:
        c = int(input("enter 1 for exersize, 2 for food\n"))
        if c==1:
            with open("vishal-exe.text") as op:
                for i in op:
                    print(i,end="")
        elif c==2:
            with open("vishal-food.text") as op:
                for i in op:
                    print(i,end="")
    elif v==2:
        c = int(input("enter 1 for exersize, 2 for food\n"))
        if c==1:
            with open("pavan-exe.text") as op:
                for i in op:
                    print(i,end="")
        elif c==2:
            with open("pavan-food.text") as op:
                for i in op:
                    print(i,end="")
    elif v==3:
        c = int(input("enter 1 for exersize, 2 for food\n"))
        if c==1:
            with open("krupa-exe.text") as op:
                for i in op:
                    print(i,end="")
        elif c==2:
            with open("krupa-food.text") as op:
                for i in op:
                    print(i,end="")
    else:
      print("enter the valid input {vishal},{pavan},{krupa}")
print("THE HEALTH MANAGEMENT SYSTEM")
a=int(input("press 1 for log the value, press 2 to retrieve the value\n"))
if a==1:
    b=int(input("press 1[vishal],2[pavan],3[krupa]\n"))
    take(b)
else:
    b=int(input("press 1[vishal],2[pavan],3[krupa]\n"))
    retrive(b)
