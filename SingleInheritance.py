# Base class
class Student:
    def getStudentInfo(self):
        self.name = input("Enter student name: ")
        self.roll_no = input("Enter roll number: ")
        self.course = input("Enter course: ")

# Derived class
class DisplayStudent(Student):
    def displayInfo(self):
        print("\n--- Student Information ---")
        print("Name     :", self.name)
        print("Roll No. :", self.roll_no)
        print("Course   :", self.course)

# Creating object of derived class
student1 = DisplayStudent()

# Calling methods
student1.getStudentInfo()   # Inherited from Student class
student1.displayInfo()      # Defined in DisplayStudent class
