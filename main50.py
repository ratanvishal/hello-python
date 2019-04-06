class Employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        # self.email=f"{fname}.{lname}@vish.gmail.com"
    def explain(self):
        return f"This is Employee is {self.fname} {self.lname}"
    @property
    def email(self):
        if self.fname==None or self.lname==None:
            return "Email is not set plz set it is using setter"
        return f"{self.fname}.{self.lname}@pav.gmail.com"
    @email.setter
    def email(self,string):
        print("setting now")
        names=string.split("@")[0]
        self.fname=string.split(".")[0]
        self.lname=string.split(".")[1]
    @email.deleter
    def email(self):
        self.fname=None
        self.lname=None
skillf= Employee("skill","F")
# print(skillf.email)
o="this is all"
# print(dir(o))
# print(dir(skillf))
# print(id("this is vishal"))
# print(id("this is pavan"))
import inspect
print(inspect.getmembers(skillf))