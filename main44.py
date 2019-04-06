class Employee:
    no_of_leaves=2
    var=8
    _protec_=9
    __private=98
    __pr=70

    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole
    def printdetails(self):
        return f"The name is {self.name},salary is {self.salary}, and the role is {self.role}"
    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves=newleaves
    @classmethod
    def from_dash(cls):
        return cls(*str.split("-"))
    @staticmethod
    def printgood(string):
        print("this is static"+string)
emp=Employee("vishal",55000,"programmer")
print(emp._Employee__pr)