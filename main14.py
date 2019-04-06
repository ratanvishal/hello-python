f=open ("fileio.text","rt")
print("fileio.text")
print(f.readlines(),end="")
print(f"readlines()")
# print(f.readline(),end="")
# print(f.readline(),end="")


#content =f.read()
#for line in f:
#    print(line,end="")

#print(content)
#content = f.read(4)
#print("1",content)
#content=f.read(23)
#print("2",content)
f.close()
