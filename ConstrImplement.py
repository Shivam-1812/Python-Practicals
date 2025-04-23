class Person:
    # Constructor method (__init__)
    def __init__(self, name, age):
        self.name = name  # Assign the value of 'name' to the instance variable 'self.name'
        self.age = age    # Assign the value of 'age' to the instance variable 'self.age'

    # Method to display information
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

# Creating an object of the class 'Person' by passing parameters to the constructor
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# Calling the display method to print the information of both objects
person1.display()
person2.display()
