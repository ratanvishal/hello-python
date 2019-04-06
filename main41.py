class Employee:

    no_of_leaves=14
    var=8
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

# class programmer(Employee):
#     no_of_holiday =56
#     def __init__(self,n,s,r,l):
#         self.name = n
#         self.salary = s
#         self.role = r
#         self.language=l
#
#     def printprog(self):
#         return f"the programmer's name is {self.name}.salary is {self.salary},and the role is {self.role},the languges are {self.language}"
class Player:
    var=9
    no_of_games=4

    def __init__(self,n,g):
        self.name=n
        self.game=g
    def printdeatails(self):
        return f"the name is {self.name} and the game is {self.game}"
class coolProgrammer(Player,Employee):
    # 555
    language="c++"
    host="good"
    def printlanguage(self):
        print(self.language)

vishal=Employee("vishal", 85000 ,"dam coder")
rohan=Employee("rohan",95000,"comunicator")
shubham=Player("subham",["footbool"])
karan=coolProgrammer("karan",["cricket"],)
# det= karan.printdetails()
# print(det)
# print(karan.no_of_holiday)
print(karan.var)
print(karan.language)
print(karan.host)
