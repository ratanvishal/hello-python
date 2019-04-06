class Employee:

    no_of_leaves=14

    def __init__(self,n,s,r):
        self.name=n
        self.salary=s
        self.role=r

    def printdetails(self):
        return f" The name is {self.name}. Salary is {self.salary} and role is {self.role}"
    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves = newleaves
    @classmethod
    def from_dash(cls,string):
        return cls(*string.split("-"))
    @staticmethod
    def printgood(string):
        print("this is a "+string)
        # return 85

class programmer(Employee):
    no_of_holiday =56
    def __init__(self,n,s,r,l):
        self.name = n
        self.salary = s
        self.role = r
        self.language=l

    def printprog(self):
        return f"the programmer's name is {self.name}.salary is {self.salary},and the role is {self.role},the languges are {self.language}"


vishal=Employee("vishal", 85000 ,"dam coder")
rohan=Employee("rohan",95000,"comunicator")
shubham=programmer("subham",555000,"programmer",["python"])
karan=programmer("karan",88000,"hacker",["python","c++"])

print(karan.no_of_holiday)

