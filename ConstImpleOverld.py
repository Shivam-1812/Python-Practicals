class Animal:
    # Base class constructor
    def __init__(self, name, species):
        self.name = name
        self.species = species
        print(f"Animal created: {self.name}, Species: {self.species}")

    def display(self):
        print(f"Name: {self.name}, Species: {self.species}")


class Dog(Animal):
    # Overriding the constructor in the Dog class
    def __init__(self, name, breed):
        # Calling the constructor of the parent class (Animal) using super()
        super().__init__(name, "Dog")
        self.breed = breed
        print(f"Dog created: {self.name}, Breed: {self.breed}")

    def display(self):
        super().display()  # Calling the parent class display method
        print(f"Breed: {self.breed}")


# Creating objects
animal1 = Animal("Tiger", "Panthera tigris")
dog1 = Dog("Buddy", "Golden Retriever")

# Displaying the details
animal1.display()
dog1.display()
