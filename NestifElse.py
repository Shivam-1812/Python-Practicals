# Input from the user
marks = int(input("Enter your marks (0-100): "))

# Outer if-else to check valid range
if 0 <= marks <= 100:
    if marks >= 90:
        print("Grade: A+")
    elif marks >= 75:
        print("Grade: A")
    elif marks >= 60:
        print("Grade: B")
    elif marks >= 40:
        print("Grade: C")
    else:
        print("Grade: F (Fail)")
else:
    print("Invalid marks! Please enter marks between 0 and 100.")
