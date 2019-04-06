class Employee:
    no_of_leaves = 8
    pass
vishal= Employee()
rohan=Employee()
vishal.name="vishal"
vishal.salary=45000
vishal.role="coder"
print(vishal.__dict__)
rohan.name="rohan"
rohan.salary=95000
rohan.role="instructor"
print(rohan.__dict__)
print(Employee.no_of_leaves)
rohan.no_of_leaves =14
print(rohan.__dict__)
print(rohan.no_of_leaves)
print(Employee.__dict__)