class Student:
    def __init__(self, name=None, age=None):
        # Simulating constructor overloading
        if name is not None and age is not None:
            self.name = name
            self.age = age
        elif name is not None:
            self.name = name
            self.age = 18  # Default age if not provided
        elif age is not None:
            self.name = "Unknown"  # Default name if not provided
            self.age = age
        else:
            self.name = "Unknown"
            self.age = 18  # Default name and age if neither is provided

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")


# Creating instances with different numbers of arguments
student1 = Student("John", 20)  # Name and Age
student2 = Student("Alice")     # Name only, default age
student3 = Student(age=25)      # Age only, default name
student4 = Student()            # No arguments, default values

# Displaying student details
student1.display()
student2.display()
student3.display()
student4.display()
