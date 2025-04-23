class Student:
    # Parameterized constructor
    def __init__(self, name, age, grade):
        self.name = name   # Assign the 'name' to the instance variable
        self.age = age     # Assign the 'age' to the instance variable
        self.grade = grade # Assign the 'grade' to the instance variable

    # Method to display student information
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grade: {self.grade}")

# Creating objects with specific parameters
student1 = Student("Alice", 20, "A")
student2 = Student("Bob", 22, "B")

# Calling the display method to print the details of the students
student1.display()
student2.display()
