# Input from user
num = int(input("Enter a number: "))

# Reverse the number
reverse = int(str(num)[::-1])

# Check if the number is a palindrome
if num == reverse:
    print(f"{num} is a Palindrome")
else:
    print(f"{num} is NOT a Palindrome")
