# def function_name(a,b,c,d,e):
#     print(a,b,c,d,e)
# function_name("vishal","pavan","krupa","rohan","roshan")
def funargs(normal,*argsvish,**kwargs):
    print(type(argsvish))
    print(normal)
    for item in argsvish:
        print(item)
    print("\nnow the words of the meaning are: ")
    for key,values in kwargs.items():
        print(f"{key} is a {values}")

har=["vishal","pavan","krupa","rohan","roshan"]
normal="this is normal art"
kw={"good":"bad","holi":"festival","joker":"cards"}
funargs(normal,*har,**kw)




