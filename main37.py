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
vishal=Employee("vishal", 85000 ,"dam coder")
rohal=Employee("rohan",95000,"comunicator")
vishal.change_leaves(45)
print(vishal.no_of_leaves)