
class Student:

    school = "BashOps"  # Static/Class Variable (defined outside method)

    def __init__(self, m1, m2, m3):
        # Below variables are Instance/Method Variables
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return round((self.m1 + self.m2 + self.m3) / 3, 2)

    def get_m1_mark(self):
        return self.m1

    def set_m1_mar(self, value):
        self.m1 = value

    # To invoke a class variable use 'cls' instead of 'self'
    @classmethod  # Decorator
    def get_school_name(cls):
        return cls.school

    @staticmethod  # which is independent method
    def info():
        print("This is example for static method..")


s1 = Student(88, 76, 75)
s2 = Student(99, 78, 65)
print(s1.avg())
print(s2.avg())

# # print the Class Variable from invoking 'info' method
# # failed with Error "TypeError: info() missing 1 required positional argument: 'cls'"
# print(Student.info())
# # As we are using 'cls' we have to mention 'info' method as 'Class Method' using 'Decorators'
print(Student.get_school_name())
