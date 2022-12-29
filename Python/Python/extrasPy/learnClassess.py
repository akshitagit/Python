class EmpDetails:
    name = "xEmployee"
    surname = "yEmployee"
    empId = 123

Nitkarsh = EmpDetails()
Purshotam = EmpDetails()
Pallavi = EmpDetails()
Rohit = EmpDetails()

Nitkarsh.name = "Nitkarsh Chourasia"
Purshotam.name = "Purshotam Bohra"
Pallavi.name = "Pallavi Chaurasiya"
Rohit.name = "Rohit Chourasia"
Nitkarsh.surname = "NC"
Purshotam.surname = "PBJI"
Pallavi.surname = "egoistic"
Rohit.surmane = "RC"
Nitkarsh.empId = 1
Nitkarsh.empId = 2
Purshotam.empId = 3
Pallavi.empId = 4
Rohit.empId = 5

print(Nitkarsh.name)
print(Nitkarsh.surname)
print(Nitkarsh.empId)
print(Purshotam.name)
print(Purshotam.surname)
print(Purshotam.empId)
print(Pallavi.name)
print(Pallavi.surname)
print(Pallavi.empId)
print(Rohit.name)
print(Rohit.surname)
print(Rohit.empId)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)
p2 = Person("Nitkarsh", 22)
p3 = Person("Pallavi", 24)

print(p1.name)
print(p1.age)
print(p2.name)
print(p2.age)
print(p3.name)
print(p3.age)


