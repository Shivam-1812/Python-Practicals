# 1. Positional Argument
def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")

# 2. Default Argument
def welcome(city="Pune"):
    print("Welcome to", city)

# 3. Keyword Argument
def display(name, course):
    print(f"Name: {name}, Course: {course}")

# 4. Variable-length Argument
def add_numbers(*nums):
    total = sum(nums)
    print("Sum:", total)

# Calling the functions
greet("Shivam", 19)                     # Positional
welcome()                              # Default
welcome("Mumbai")                      # Default with override
display(course="Python", name="Raj")   # Keyword
add_numbers(10, 20, 30, 40)            # Variable-length
