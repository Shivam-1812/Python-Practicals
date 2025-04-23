# Input from user
num = int(input("Enter a 4-digit number: "))
sum_digits = 0
original = num  # To display later

# Check if it's a 4-digit number
if 1000 <= num <= 9999:
    while num > 0:
        digit = num % 10
        sum_digits += digit
        num = num // 10
    print(f"Sum of digits of {original} is: {sum_digits}")
else:
    print("Please enter a valid 4-digit number!")
