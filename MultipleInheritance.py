# First base class
class Person:
    def getPersonInfo(self):
        self.name = input("Enter your name: ")
        self.age = input("Enter your age: ")

# Second base class
class Student:
    def getStudentInfo(self):
        self.roll_no = input("Enter your roll number: ")
        self.course = input("Enter your course: ")

# Derived class (inherits from both Person and Student)
class CollegeStudent(Person, Student):
    def displayInfo(self):
        print("\n--- Student Full Information ---")
        print("Name     :", self.name)
        print("Age      :", self.age)
        print("Roll No. :", self.roll_no)
        print("Course   :", self.course)

# Creating object of derived class
student1 = CollegeStudent()

# Calling methods from both base classes
student1.getPersonInfo()
student1.getStudentInfo()

# Displaying info
student1.displayInfo()
