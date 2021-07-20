
class Student:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()   # Constructing Object of an inner class in Outer Class

    def show(self):
        print(self.name, self.rollno)

    class Laptop:

        def __init__(self):
            self.brand = "HP"
            self.cpu = "i7"
            self.ram = "16GB"

        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = Student("Sachin", 101)
s2 = Student("Dhoni", 102)

# print(s1.name, s1.rollno)
# print(s2.name, s2.rollno)
s1.show()
s2.show()

# Object created for inner Class inside Outer Class
print("Object inside class")
print(s1.lap.brand)
# OR
lap1 = s1.lap
lap2 = s2.lap
print(lap1.cpu)
print(lap2.cpu)
s1.lap.show()

# Object Creating for inner Class outside Class
print("Object outside Class")
lap1 = Student.Laptop()
print(lap1.brand)
lap1.show()