# Base class
class Person:
    def getPersonInfo(self):
        self.name = input("Enter your name: ")
        self.age = input("Enter your age: ")

# Derived class 1
class Student(Person):
    def getStudentInfo(self):
        self.roll_no = input("Enter your roll number: ")

# Derived class 2 (inherits from Student)
class CollegeStudent(Student):
    def getCollegeInfo(self):
        self.course = input("Enter your course: ")

    def displayInfo(self):
        print("\n--- College Student Information ---")
        print("Name     :", self.name)
        print("Age      :", self.age)
        print("Roll No. :", self.roll_no)
        print("Course   :", self.course)

# Creating object of derived-most class
student1 = CollegeStudent()

# Calling methods from all levels
student1.getPersonInfo()   # From Person class
student1.getStudentInfo()  # From Student class
student1.getCollegeInfo()  # From CollegeStudent class

# Displaying info
student1.displayInfo()
