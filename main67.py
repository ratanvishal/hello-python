#
# a=input("what is your name\n")
# b=input("how much do u earn\n")
# if int(b)==0:
#     raise ZeroDivisionError("b is 0 so stopping the program")
# if a.isnumeric():
#     raise Exception("number are not allowed")
# # print(f"hello {a}, you have attrative salary {b}$/-")
# c=input("Enter your name")
# try:
#     print(a)
# except Exception as e:
#  if c=="vishal":
#     raise  ValueError("Vishal is blocked he is not allowed")
# print("Exception handled")

v = input("tell ur bad name\n")
try:
    print(a)
except Exception as e:
  if v == "bye":
    raise AttributeError("bye is not a bad name")
  print("Exception handling")




