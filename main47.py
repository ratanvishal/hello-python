class Employee:
    no_of_leaves=7
    def __init__(self,n,s,r):
        self.name=n
        self.salary=s
        self.role=r
    def printdetails(self):
        return f"The name is {self.name},salary is {self.salary} and the role is {self.role} "
    @classmethod
    def change_leaves(cls,newleaves):
        cls.change_leaves=newleaves
    def __add__(self, other):
        return self.salary + other.salary
    def __truediv__(self, other):
        return self.salary / other.salary
    def __repr__(self):
        return self.printdetails()
    def __str__(self):
        return f"the name is {self.name},salary in {self.salary}$,and the role is {self.role}"
emp1=Employee("vishal",55000,"programmer")
emp2=Employee("pavan",65000,"gamer")
print(emp1)