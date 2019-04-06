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


hindustani_supporter=Employee("hindustani","supporter")
nikhil_rak=Employee("nikil","raj")
print(hindustani_supporter.email)
hindustani_supporter.fname="USA"
print(hindustani_supporter.email)
hindustani_supporter.email= "this.that@vish.gmail.com"
print(hindustani_supporter.email)
del hindustani_supporter.email
print(hindustani_supporter.email)
hindustani_supporter.email="vishal.sagar@pav.gmail.com"
print(hindustani_supporter.email)
print(nikhil_rak.email)



