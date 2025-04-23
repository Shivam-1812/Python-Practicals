# Input from the user
num = int(input("Enter a number: "))
reverse = 0
original = num  # Save original number for display

# Reversing the number using loop
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

# Output
print(f"Reversed number of {original} is: {reverse}")
