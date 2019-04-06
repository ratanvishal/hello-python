class Employee:
    no_of_leaves = 14

    def __init__(self, n, s, r):
        self.name = n
        self.salary = s
        self.role = r

    def printdetails(self):
        return f" The name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_str(cls, string):
        # params=string.split("-")
        # print(params)
        # return cls(params[0],params[1],params[2])
        return cls(*string.split("-"))

    # @classmethod
    # def from_strslah(cls, strings):
    # #     # prams=strings.split("/")
    # #     # print(prams)
    # #     # return cls(prams[0],prams[1],prams[2])
    #     return cls(*strings.split("*"))

    @staticmethod
    def printgoood(string):
        print("this is a "+string)
        return 85


vishal = Employee("vishal", 85000, "dam coder")
rohan = Employee("rohan", 95000, "comunicator")
vikas = Employee.from_str("vikas-65000-batter")
# p= Employee.from_strslah("pavan*65000*bolwer")

# vishal.change_leaves(45)
print(rohan.printgoood("static method"))
